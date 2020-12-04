import os
import shutil
import subprocess
import mysql.connector

def getData():
    data = []
    lb = 0
    try:
        for i in os.listdir("weather/raw"):
            path1 = "weather/raw/" + str(i)
            for j in os.listdir(path1):
                path2 = path1 + "/" +j
                for k in os.listdir(path2):
                    plik = open(path2 + "/" + k)
                    for linia in plik:
                        dane = linia.split(sep=",")
                        data.append(dane)
                        lb = lb + 1
                        print(f"Załadowano danych: {lb}")
        return data, lb
    except:
        print("Wystąpił błąd podczas pobierania danych")
        return 0, 0


def sendData(dane, lb):
    mydb = mysql.connector.connect(
        host="ssh.kubaczak.com",
        user="pythondb",
        passwd="pythondb_pass",
        database="pythondb"
    )

    cursor = mydb.cursor()
    l = 0
    for i in dane:
        try:
            sql = "INSERT INTO weather (data, inHumidity, inTemperature, outHumidity, outTemperature, pressure, windSpeed, gust, windDirection, idk, rainFall) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            var = (i[0], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            cursor.execute(sql, var)
            mydb.commit()
            l = l + 1
            print(f"Wyslano danych: {l}/{lb}")
        except:
            print(f"Wystąpił problem przy próbie wysłania lini nr. {i}")

if __name__ == "__main__":
    dane, lb = getData()
    if dane != 0:
        sendData(dane, lb)
        print("Zakoczono powodzeniem!")

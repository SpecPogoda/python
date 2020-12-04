import configparser
import os
import shutil
import subprocess
import mysql.connector

def init():
    if not os.path.isdir("weather"):
        os.mkdir("weather")
    else:
        shutil.rmtree("weather")
        os.mkdir("weather")
    
    try:
        subprocess.run('python3 -mpywws.logdata -vvv weather', shell=True, check=True, text=True)
    except:
        print("")

    a = """[paths]
work = /tmp/pywws
datastoretype = filedata

[config]
usb activity margin = 3.0
ws type = 1080
pressure offset = 21
logdata sync = 1"""

    p = open("weather/weather.ini", "w")
    p.write(a)

    subprocess.run('python3 -mpywws.logdata -vvv weather', shell=True, check=True, text=True)

def getData():
    data = []
    lb = 0
    try:
        for i in os.listdir("weather/raw/"):
            path1 = "weather/raw/" + str(i)
            for j in os.listdir(path1):
                path2 = path1 + j
                for k in os.listdir(path2):
                    plik = open(k)
                    for linia in plik:
                        dane = linia.split(sep=",")
                        data.append(dane)
                        os.system('clear')
                        lb = lb + 1
                        print(f"Załadowano danych: {lb}")
        return data, lb
    except:
        print("Wystąpil błąd podczas pobierania danych")

def sendData(dane, lb):
    mydb = mysql.connector.connect(
        host="ssh.kubaczak.com",
        user="pythondb",
        passwd="pythondb_pass",
        database="pythondb"
    )
skri
    cursor = mydb.cursor()
    l = 0
    for i in dane:
        try:
            sql = "INSERT INTO weather (data, inHumidity, inTemperature, outHumidity, outTemperature, pressure, windSpeed, gust, windDirection, idk, rainFall) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            var = (dane[i][0], dane[i][2], dane[i][3], dane[i][4], dane[i][5], dane[i][6], dane[i][7], dane[i][8], dane[i][9], dane[i][10], dane[i][11])
            cursor.execute(sql, var)
            mydb.commit()
            os.system('clear')
            l = l + 1
            print(f"Wyslano danych: {l}/{lb}")
        except:
            print(f"Wystąpił problem przy próbie wysłania lini nr. {i}")

if __name__ == "__main__":
    init()
    dane, lb = getData()
    sendData(dane, lb)

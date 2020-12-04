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
p.close()
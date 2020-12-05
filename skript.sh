if [ -d "weather/" ]; then
    rm -r weather
fi
mkdir weather
python3 -m pywws.logdata -vvv weather
python3 editcfg.py
python3 -m pywws.logdata -vvv weather
python3 main.py

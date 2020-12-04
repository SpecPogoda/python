if [ -d "weather/" ]; then
    rm -r weather
fi
mkdir weather
python3 -m pywws.logdata -vvv weather
python3 -m editcfg.py
python3 -m pywws.logdata -vvv weather
python3 -m main.py

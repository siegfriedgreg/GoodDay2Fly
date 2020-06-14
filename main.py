#==================================================================================
##
#
#    Author: Greg Siegfried
#    Date: 5/16/2020
#    Project: FlyToday App in Python
#
#    Purpose: wuing a wuer supplied api key, zip code, and desired environment
#            variables, the program will get the local weather information from
#            'openweathermap.org'; and based on that information and the wuer
#            defined environment variables, will suggest if it is a good day
#            to fly or not. 
#
#    Features: Supports current weather information. Working on the forcast method
#            to be able to give you days and times to expect a good flight.
#
##
####

import json
import requests
from info_data import Weather as wu
from module1 import User as us

################################################################################
####------------>>>>            MAIN PROGRAM
################################################################################

# Old Version of program/
def mainWeather():
    #### PART 1: GET AND SET WEATHER RESPONSE
    with requests.get(wu.urlWeather(wu)) as rx:
        kx = rx.json()
    #### PART 2: IF VALID RESPONSE WRITE TO FILE
    if(kx["cod"] != 404):
        with open(wu.fileName, 'w') as output:
            json.dump(kx, output, sort_keys=True, indent=2)
    #### PART 3: ELSE wuE LAST SAVED RESPONSE
    else:
        print("\t -- Invalid Response, wuing Last Known Values -- \n")
    #### PART 4: OPEN SAVED FILE
    with open(wu.fileName, 'r') as input:
        kx = json.load(input)
    #### PART 5: SET RESPONSE VALUES
    try:
        # CLOUDS
        wu.evalClouds(kx["clouds"])
        wu.parseClouds(kx["clouds"])
        # DT
        wu.parseDT(kx["dt"])
        # MAIN
        wu.evalTemp(kx["main"])
        wu.parseTemp(kx["main"])
        # SYS
        wu.parseSys(kx["sys"])
        # VISIBILITY
        wu.parseVis(kx["visibility"])
        # WEATHER
        wu.evalWeather(kx["weather"])
        wu.parseWeather(kx["weather"])
        # WIND
        wu.evalWind(kx["wind"])
        wu.parseWind(kx["wind"])
    except:
        print("CDMSWW Not Found")
    #### PART 6: PRINT FORMATTED DATA
    wu.printReport()
    #### PART 7: TEST RESPONSES AND PRINT MESSAGE
    fly = wu.testCheck(wu)
    wu.printCheck(fly)


# New Version of Program\
def updateForcast():
    x = us.getURL()
    with requests.get(x) as rx:
        kx = rx.json( )

    with open(us._fileName, 'w') as output:
        json.dump(kx, output, sort_keys=True, indent=2)

def parseCurrentWeather():
    with open(us._fileName, 'r') as input:
        kx = json.load(input)
        try:
            us.parseCurrent( kx["current"], kx["daily"][0] )
        except Exception as e:
            print(e)

def parseTomorrowsWeather():
    with open(us._fileName, 'r') as input:
        kx = json.load(input)
        try:
            us.parseNextDay( kx["daily"][1] )
        except Exception as e:
            print(e)

def parseWeekOut():
    with open(us._fileName, 'r') as input:
        kx = json.load(input)
        try:
            us.parseWeekOutlook( kx["daily"] )
        except Exception as e:
            print(e)

def parse3DaysOut():
    with open(us._fileName, 'r') as input:
        kx = json.load(input)
        try:
            us.parse3DayOutlook( kx["daily"], kx["hourly"] )
        except Exception as e:
            print(e)


# RUN NEW VERSION
if __name__ == "__main__":
    updateForcast()
    parseCurrentWeather()
    parseTomorrowsWeather()
    parseWeekOut()
    parse3DaysOut()


################################################################################
####                             END PROGRAM                                ####
################################################################################
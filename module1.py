#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

from time import localtime, strftime

class User(object):

    # User required/desired variables
    _fileName = "forcast_backup.txt"
    _apiKey = "b65e161b18736e911c299c20fd7858cc"
    _units = "imperial"
    _lat = "35.95"
    _lon = "-78.95"
    _link = "https://api.openweathermap.org/data/2.5/onecall?"
    _desired = {'temp_min':50, 'temp_max':99, 'wind_max':22, 'clouds':83 }
    _weatherID = {800:"no clouds", 801:"few clouds", 802:"scattered clouds", 
                 803:"broken clouds", 804:"overcast clouds" }

    # Create a list and return a formatted URL string.
    def getURL():

        x = [User._link, User._lat, User._lon, User._units, User._apiKey]

        return '{0[0]}lat={0[1]}&lon={0[2]}&units={0[3]}&appid={0[4]}'.format(x)
 
    # Convert the wind_degree value into a wind direction icon.
    # Format is meant to indicate direction of wind travel. NE would indicate 
    # that the wind is traveling from north to south, and east to west.
    # The pictogram is meant to illustrate the direction of travel with
    # with keyboard characters. 
    def convertWind(value):

        if (22 <= value <=68):
            return "NE /< "
        elif ( 69 <= value <= 114):
            return "E << "
        elif ( 115 <= value <= 160):
            return "SE ^< "
        elif ( 161 <= value <= 206):
            return "S ^^ "
        elif ( 207 <= value <= 252):
            return "SW ^> "
        elif ( 253 <= value <= 298):
            return "W >> "
        elif ( 299 <= value <= 344):
            return "NW \> "
        else:
            return "N || "

    # Convert from epoch time to a local date format
    def convertDate(value):

        x = localtime(value)

        return strftime("%a, %B %d ", x)

    # Convert from epoch time to a local time format 12hr.
    def convertTime(value):

        x = localtime(value)

        return strftime("%I:%M:%S %p", x)

    # Print out the current day formatted data.
    def parseCurrent( x, y, **ka ):

        # Load Variables
        lt = [ User.convertDate(x["dt"]), User.convertTime(x["dt"]) ]
        dl = [ User.convertTime(x["sunrise"]), User.convertTime(x["sunset"])]
        ltemp = [ x["temp"] , x["feels_like"] ]
        rtemp = [ y["temp"]["min"], y["temp"]["max"] ]
        wind = [ x["wind_speed"], User.convertWind(x["wind_deg"]) ]
        visUv = [ round(x["visibility"] / 5280 , 2), x["uvi"] ]
        desc = [ x["weather"][0]["main"], x["weather"][0]["description"] ]

        # Print Variables
        print("          Current Weather: ")
        print('    Date: {0[0]}        Time: {0[1]}'.format(lt))
        print('    Sunrise: {0[0]}      Sunset: {0[1]}'.format(dl))
        print('    Current Temp: {0[0]} F     Feels Like: {0[1]} F'.format(ltemp))
        print('    Minimum Temp: {0[0]} F     Maximum Temp: {0[1]} F'.format(rtemp))
        print('    Wind Speed: {0[0]} mph      Wind Direction: {0[1]}'.format(wind))
        print('    Visibility: {0[0]} mi       UV Index: {0[1]}'.format(visUv))
        print('    Description: {0[0]} : {0[1]}'.format(desc))
        print("\n")

    # Print out the next day formatted data.
    def parseNextDay( x, **ka ):

        # Load Variables
        lt = [ User.convertDate(x["dt"]), User.convertTime(x["dt"]) ]
        dl = [ User.convertTime(x["sunrise"]), User.convertTime(x["sunset"])]
        ttemp = [ x["temp"]["min"], x["temp"]["max"] ]
        fltemp = [ x["feels_like"]["morn"], x["feels_like"]["eve"] ]
        wind = [ x["wind_speed"], User.convertWind(x["wind_deg"]) ]
        cldUv = [ x["clouds"], x["uvi"] ]
        desc = [ x["weather"][0]["main"], x["weather"][0]["description"] ]

        # Print Variables
        print("          Tomorrows Weather: ")
        print('    Date: {0[0]}        Time: {0[1]}'.format(lt))
        print('    Sunrise: {0[0]}      Sunset: {0[1]}'.format(dl))
        print('    Min Temp: {0[0]} F         Max Temp: {0[1]} F'.format(ttemp))
        print('    Morning Temp: {0[0]} F     Evening Temp: {0[1]} F'.format(fltemp))
        print('    Wind Speed: {0[0]} mph      Wind Direction: {0[1]}'.format(wind))
        print('    Cloudiness: {0[0]} %          UV Index: {0[1]}'.format(cldUv))
        print('    Description: {0[0]} : {0[1]}'.format(desc))
        print("\n")

    # Print the hourly outlook for the next 3 days.
    def parse3DayOutlook( x, y, **ka ):

        print("          3 Day Outlook: ")

        # Get Valid Sunrise/Sunset values for good weather for the next 3 days.
        for i in range(1,4):
            print('  {}:  '.format( User.convertDate(x[i]["dt"]) ) )

            # Filter by weatherID and Cloud values.
            if( x[i]["weather"][0]["id"] in User._weatherID 
               and x[i]["clouds"] <= User._desired["clouds"] ):

                # Take Filtered Value and Print the Hours within Sunrise to Sunset.
                for j in range(0,47):

                    if( x[i]["sunrise"] <= y[j]["dt"] <= x[i]["sunset"] ):

                        print('  Time: {}  Temp: {}  Clouds: {}  Wind: {}  Weather: {} '.format(
                              User.convertTime(y[j]["dt"]), y[j]["temp"], y[j]["clouds"],
                                y[j]["wind_speed"], y[j]["weather"][0]["description"] ) )

    # Print the outlook for the next week.
    def parseWeekOutlook( x, **ka ):

        print("          Weekly Outlook: ")

        for i in x:

            if( i["weather"][0]["id"] in User._weatherID and i["clouds"] <= User._desired["clouds"] ):
                print('    :GOOD:  {} : {}; clouds: {}'.format(
                    User.convertDate(i["dt"]), i["weather"][0]["description"], i["clouds"] ) )

            elif i["weather"][0]["id"] in User._weatherID:
                print('    :MAYBE: {} : {}; clouds: {}'.format(
                    User.convertDate(i["dt"]), i["weather"][0]["description"], i["clouds"] ) )

            else:
                print('    :BAD:   {} : {}; clouds: {}'.format(
                    User.convertDate(i["dt"]), i["weather"][0]["description"], i["clouds"] ) )

        print("\n")











#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
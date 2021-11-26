################################################################################
# ------------>>>>            GD2FLY.PY
################################################################################

######## Author: Greg Siegfried
######## Project: Good Day 2 Fly
######## Use: Display weather data in CLI or MOTD applications
######## Process: Openweathermap.org is queried with user data and a JSON response.
######## Modify: Output colors can be formatted, see `USER VARIABLES`
######## Modify: Output can be Current Weather &|or Current Forecast. see `MAIN`

import json
import requests
from time import localtime, strftime
from colorama import Fore, Back, init, Style

init(autoreset=True)

################################################################################
# ------------>>>>            USER VARIABLES
################################################################################

# SETTINGS
api_key = "b65e161b18736e911c299c20fd7858cc"
zip_code = "27707"
units = "imperial"
option = ["weather", "forecast"]
link = "http://api.openweathermap.org/data/2.5/"
s_time = "12:00:00"
# clouds = % of clouds in the sky.
desired = { "temp_min": 40, "temp_max": 99, "wind_max": 18, "clouds": 83 } 

# COLOR FORMATTING.
# Fore|Back = BLACK, WHITE, BLUE, GREEN, RED, YELLOW, MAGENTA
# Style = DIM, NORMAL, BRIGHT
# ----> Weather
MJR = Style.BRIGHT + Fore.CYAN
MNR = Style.NORMAL + Fore.WHITE
LO = Style.BRIGHT + Fore.BLUE 
HI = Style.BRIGHT + Fore.RED
CRT = Style.BRIGHT + Fore.YELLOW
FLT = Style.BRIGHT + Fore.GREEN
# ----> Forecast
HC = Style.BRIGHT + Fore.CYAN
LC = Style.NORMAL + Fore.WHITE
GD = Style.BRIGHT + Fore.GREEN
BD = Style.BRIGHT + Fore.RED

################################################################################
# ------------>>>>            FUNCTIONS
################################################################################

# Create the desired HTML link. Weather = 0 | Forecast = 1
def create_link(value):
    
    html_list = [link, option[value], zip_code, units, api_key]
    
    return '{0[0]}{0[1]}?zip={0[2]}&units={0[3]}&appid={0[4]}'.format(html_list)
    
# Convert from epoch time to a local date format
def convert_date(value):

    return strftime("%a, %B %d ", localtime(value))

# Convert from epoch time to a local time format 12hr.
def convert_time(value):

    return strftime("%I:%M:%S %p", localtime(value))

# Convert the wind_degree value into a wind direction icon.
def convert_wind(value):

    if (22 <= value <= 68):
        return " SW -> NE "
    elif (69 <= value <= 114):
        return " W -> E "
    elif (115 <= value <= 160):
        return " NW -> SE "
    elif (161 <= value <= 206):
        return " N -> S "
    elif (207 <= value <= 252):
        return " NE -> SW "
    elif (253 <= value <= 298):
        return " E -> W "
    elif (299 <= value <= 344):
        return " SE -> NW "
    else:
        return " S -> N"

# Format and Print the current weather data.
def print_weather(args):

    # Load Variables
    c_date = convert_date(args['dt'])
    c_time = convert_time(args['dt'])
    c_temp = str(round(args['main']['temp'], 1)) + " F "
    c_fltemp = str(round(args['main']['feels_like'], 1)) +" F "
    c_minT = str(round(args['main']['temp_min'], 1)) +" F "
    c_maxT = str(round(args['main']['temp_max'], 1)) +" F "
    c_windS = str(args['wind']['speed']) +" MPH "
    c_windD = convert_wind(args['wind']['deg'])
    c_rise = convert_time(args['sys']['sunrise'])
    c_set = convert_time(args['sys']['sunset'])
    c_vis = str(round(args['visibility'] / 5280, 2))
    c_main = args['weather'][0]['main']
    c_desc = args['weather'][0]['description']

    # Print Variables in format; See User Variables to Adjust Colors.
    print( MJR + "\t\tCurrent Weather: " )
    print( MJR + "\tDate: " + MNR + c_date + MJR + "\t Time: " + MNR + c_time)
    print( MJR + "\tSunrise: " + MNR + c_rise + MJR+ "\t Sunset: " + MNR + c_set)
    print( MJR + "\tCurrent Temp: " + CRT + c_temp + MJR + "\t Feels Like: " + FLT + c_fltemp)
    print( MJR + "\tMinimum Temp: " + LO + c_minT + MJR + "\t Maximum Temp: " + HI + c_maxT)
    print( MJR + "\tWind Speed: " + MNR + c_windS + MJR + "\t Wind Direction: " + MNR + c_windD)
    print( MJR + "\tVisibility: " + MNR + c_vis + " MI")
    print( MJR + "\tMain: " + MNR + c_main + " = " + c_desc)

# Format and Print the current forecast data.
def print_forecast(args):
    
    # DATE, FEELSLIKE, WINDSPEED, DESCRIPTION
    Count = 0
    fct = [["",0.0, 0.0, ""],["",0.0, 0.0, ""],["",0.0, 0.0, ""],["",0.0, 0.0, ""]]
    
    for hours in args['list']:
        temp = hours['dt_txt'].split(' ')[1]
        if ((s_time == temp) & (Count <= 3)):
            fct[Count][1] = round(hours['main']['feels_like'], 1)
            fct[Count][2] = round(hours['wind']['speed'], 1)
            fct[Count][3] = hours['weather'][0]['description']
            
            if hours['clouds']['all'] <= desired['clouds'] & (desired['temp_min'] <= fct[Count][1] <= desired['temp_max']) & (fct[Count][2] <= desired['wind_max']):
                fct[Count][0] = GD + convert_date(hours['dt'])
            else:
                fct[Count][0] = BD + convert_date(hours['dt'])
            Count += 1

    print( HC + "\t\tForecast: ")
    print( HC + "\tDate: " + fct[0][0] + HC + " Temp: " + LC + str(fct[0][1]) + HC + " Wind: " + LC + str(fct[0][2]) + HC + " Desc: " + LC + fct[0][3] )
    print( HC + "\tDate: " + fct[1][0] + HC + " Temp: " + LC + str(fct[1][1]) + HC + " Wind: " + LC + str(fct[1][2]) + HC + " Desc: " + LC + fct[1][3] )
    print( HC + "\tDate: " + fct[2][0] + HC + " Temp: " + LC + str(fct[2][1]) + HC + " Wind: " + LC + str(fct[2][2]) + HC + " Desc: " + LC + fct[2][3] )
    print( HC + "\tDate: " + fct[3][0] + HC + " Temp: " + LC + str(fct[3][1]) + HC + " Wind: " + LC + str(fct[3][2]) + HC + " Desc: " + LC + fct[3][3] )

# CURRENT WEATHER WRAPPER
def curr_weather():
    
    kx = {}
    html_link = create_link(0)
    try:
        with requests.get(html_link) as rx:
            kx = rx.json()
            
        print_weather(kx) 
    except Exception as e:
        print(e)
        return -1

    return 0

# CURRENT FORECAST WRAPPER
def curr_forecast():
      
    kx = {}
    html_link = create_link(1)
    try:
        with requests.get(html_link) as rx:
            kx = rx.json()
            
        print_forecast(kx) 
    except Exception as e:
        print(e)
        return -1

    return 0

################################################################################
# ------------>>>>            MAIN
################################################################################

curr_weather()
print('\n') 
curr_forecast()

################################################################################
# ------------>>>>            END GD2FLY.PY
################################################################################
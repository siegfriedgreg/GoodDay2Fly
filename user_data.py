################################################################################
# ------------>>>>            USER_DATA.PY
################################################################################

import json
import requests
import os.path as osp
from time import localtime, strftime, time

################################################################################
# ------------>>>>            START USER CLASS
################################################################################


class User:

    def __init__(self):

        self.backup = "_backup.txt"
        self.api_key = "b65e161b18736e911c299c20fd7858cc"
        self.zip_code = "27707"
        self.option = ['weather', 'forecast']
        self.units = "imperial"
        self.link = "http://api.openweathermap.org/data/2.5/"
        self.desired = {'temp_min': 50, 'temp_max': 99,
                        'wind_max': 22, 'clouds': 83}
        self.weather_id = {800: "no clouds", 801: "few clouds",
                           802: "scattered clouds", 803: "broken clouds",
                           804: "overcast clouds"}

    # Create the specific Weather/Forcast link to get the correct information
    def update_file(self, args=0):

        # Create a list of the required Open Weather API variables.
        s_list = [self.link, self.option[args],
                  self.zip_code, self.units, self.api_key]
        # Create a formatted string with list data.
        html_string = '{0[0]}{0[1]}?zip={0[2]}&units={0[3]}&appid={0[4]}'.format(
            s_list)
        # Create the file string depending on Weather/Forcast variable
        file_string = self.option[args] + self.backup

        # Request the API data for the file_name
        with requests.get(html_string) as rx:
            kx = rx.json()
        # Write the new data to the file_name
        with open(file_string, 'w') as output:
            json.dump(kx, output, sort_keys=True, indent=2)

    # Convert the wind_degree value into a wind direction icon.
    # The pictogram is meant to illustrate the direction of travel with
    # keyboard characters.
    def convert_wind(self, value):

        if (22 <= value <= 68):
            return "NE"
        elif (69 <= value <= 114):
            return "E << "
        elif (115 <= value <= 160):
            return "SE"
        elif (161 <= value <= 206):
            return "S ^^ "
        elif (207 <= value <= 252):
            return "SW"
        elif (253 <= value <= 298):
            return "W >> "
        elif (299 <= value <= 344):
            return "NW"
        else:
            return "N vv "

    # Convert from epoch time to a local date format
    def convert_date(self, value):

        return strftime("%a, %B %d ", localtime(value))

    # Convert from epoch time to a local time format 12hr.
    def convert_time(self, value):

        return strftime("%I:%M:%S %p", localtime(value))

    # Print out the current weather formatted data.
    def print_current_day(self, args):

        # Load Variables
        lt = [self.convert_date(args['dt']), self.convert_time(args['dt'])]
        dl = [self.convert_time(args['sys']["sunrise"]),
              self.convert_time(args['sys']["sunset"])]
        ltemp = [args['main']['temp'], args['main']['feels_like']]
        rtemp = [args['main']['temp_min'], args['main']['temp_max']]
        wind = [args['wind']['speed'], self.convert_wind(args['wind']['deg'])]
        vis = [round(args["visibility"] / 5280, 2)]
        desc = [args["weather"][0]["main"], args["weather"][0]["description"]]

        # Print Variables
        print("          Current Weather: ")
        print('    Date: {0[0]}        Time: {0[1]}'.format(lt))
        print('    Sunrise: {0[0]}      Sunset: {0[1]}'.format(dl))
        print(
            '    Current Temp: {0[0]} F     Feels Like: {0[1]} F'.format(ltemp))
        print(
            '    Minimum Temp: {0[0]} F     Maximum Temp: {0[1]} F'.format(rtemp))
        print(
            '    Wind Speed: {0[0]} mph      Wind Direction: {0[1]}'.format(wind))
        print('    Visibility: {0[0]} mi     '.format(vis))
        print('    Description: {0[0]} : {0[1]}'.format(desc))
        print("\n")

    # Print the outlook for the next week.
    def print_week_outlook(self, args):

        print("          Weekly Outlook: ")

        for i in args:

            if(i["weather"][0]["id"] in self.weather_id and i["clouds"]["all"] <= self.desired["clouds"]):
                print('    :GOOD:  {}  {}  -> vis: {} mi  -> temp: {} F'.format(
                    i['dt_txt'], i['weather'][0]['description'],
                    round(i["visibility"] / 5280, 2), i['main']['feels_like']))

            elif i["weather"][0]["id"] in self.weather_id:
                print('    :MAYBE:  {}  {}  -> vis: {} mi  -> temp: {} F'.format(
                    i['dt_txt'], i['weather'][0]['description'],
                    round(i["visibility"] / 5280, 2), i['main']['feels_like']))
            else:
                print('    :BAD:   {}  {}  -> vis: {} mi  -> temp: {} F'.format(
                    i['dt_txt'], i['weather'][0]['description'],
                    round(i["visibility"] / 5280, 2), i['main']['feels_like']))
            
            # Checks for end of day to print new line for the next day
            if strftime("%H", localtime(i['dt']))== '17':
                print("\n")

        print("\n")

    # Current Weather function
    def current_weather(self):

        delta_tee = 0
        file_string = self.option[0] + self.backup

        try:
            delta_tee = time() - osp.getmtime(file_string)
        except OSError:
            self.update_file(0)
        finally:
            if delta_tee >= 600.1:
                self.update_file(0)

        with open(file_string, 'r') as input:
            kx = json.load(input)
            try:
                self.print_current_day(kx)
            except Exception as e:
                print(e)

    # Week Outlook Function
    def week_out(self):

        file_string = self.option[1] + self.backup

        with open(file_string, 'r') as input:
            kx = json.load(input)
            try:
                self.print_week_outlook(kx["list"])
            except Exception as e:
                print(e)

################################################################################
# ------------>>>>            END USER CLASS
################################################################################

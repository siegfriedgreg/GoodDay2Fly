#================================================================================
##
#
#    Author: Greg Siegfried
#    Date: 5/16/2020
#    Project: GoodDay2Fly App in Python
#
#    Purpose: To give the user planning ability on finding the best times to fly.
#            Intent is for RC enthusiests to have better insight into their 
#            preferred weather, to be able to get equipment ready in time.
#
#    Features: The free version of OpenWeatherMap.org provides current weather
#           and a 5 day three hour block forcast.  The app will display current
#           current weather variables, and based on user defined values, can 
#           look through the 5 day forcast and find days/times that would good to
#           plan for. Obviously the forcast can only be so accurate, but it can
#           give enough detail to plan for events.  This app is designed to give
#           flight recommendations during daylight hours.
#
#    Recent Updates: 
#           8/20/21 - fixed most problems from api changes, working on cleaning 
#                     up more, and adding more functionality.
#
##
####

import os
from user_data import User as us


def screen_clear():
       # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


################################################################################
####------------>>>>            MAIN PROGRAM
################################################################################

if __name__ == "__main__":

    # Create User
    md = us()
    repeat = True

    while repeat:

        # Display Menu
        print(" Please choose a display option: ")
        print("\t Current Weather = 1 ")
        print("\t   5 Day Outlook = 5 ")
        print("\t --- Quit Program! = 9 ")

        # Ask for input
        input_var = input("Choice:  ")

        # Clear the command|terminal
        screen_clear()

        # Filter input to proper request
        if input_var == '1':
            md.current_weather()
        elif input_var == '5':
            md.week_out()
        elif input_var == '9':
            repeat = False
        else:
            print("---- Please Input A Valid Choice! ----\n")

    # Clean Up!
    del(md)

################################################################################
####                             END PROGRAM                                ####
################################################################################

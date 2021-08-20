#================================================================================
##
#
#    Author: Greg Siegfried
#    Date: 5/16/2020
#    Project: FlyToday App in Python
#
#    Purpose: To give the user plnning ability on finding the best times to fly.
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
##
####

from user_data import User as us

################################################################################
####------------>>>>            MAIN PROGRAM
################################################################################

# RUN MAIN
if __name__ == "__main__":

    # Create User
    md = us()
    repeat = True

    while repeat:

        print(" Please choose a display option: ")
        print("\t Current Weather = 1 ")
        print("\t 3 Day Outlook = 2 ")
        print("\t 5 Day Outlook = 3 ")
        print("\t Quit Program! = 9 ")

        input_var = input("Choice:  ")

        if input_var == '1':
            md.current_weather()
        elif input_var == '2':
            md.three_days_out()
        elif input_var == '3':
            md.week_out()
        elif input_var == '9':
            repeat = False
        else:
            print("---- Please Input A Valid Choice! ----\n")

################################################################################
####                             END PROGRAM                                ####
################################################################################

#================================================================================
##
#
#    Author: Greg Siegfried
#    Date: 5/16/2020
#    Project: FlyToday App in Python
#
#    Purpose: using a us supplied api key, zip code, and desired environment
#            variables, the program will get the local weather information from
#            'openweathermap.org'; and based on that information and the wuer
#            defined environment variables, will suggest if it is a good day
#            to fly or not. 
#
#    Features: Supports current weather information. Working on the forcast 
#          methodto be able to give you days and times to expect a good flight.
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

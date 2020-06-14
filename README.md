# GoodDay2Fly
"Stay out of clouds. The silver lining everyone keeps talking about might be another airplane going in the opposite direction. Reliable sources also report that mountains have been known to hide out in clouds." - pilot quote.

GoodDay2Fly is a python weather app that uses openweathermap.com API to get weather data for a specific GPS position. The data response is saved in a JSON format as a user specified file. The user should input their own API key in the respective module file. The user will also be able to set their own desired weather parameters. Allowing for a custom outlook of desireable future days to enjoy a flight.

Output consists of the current weather, tomorrows weather, a weekly outlook, and an hourly outlook for the next three days.

          Current Weather:
    Date: Sat, June 13         Time: 10:41:11 PM
    Sunrise: 05:58:44 AM      Sunset: 08:33:22 PM
    Current Temp: 67.35 F     Feels Like: 63.75 F
    Minimum Temp: 63.03 F     Maximum Temp: 67.35 F
    Wind Speed: 8.05 mph      Wind Direction: E <<
    Visibility: 3.05 mi       UV Index: 8.96
    Description: Clouds : few clouds


          Tomorrows Weather:
    Date: Sun, June 14         Time: 01:00:00 PM
    Sunrise: 05:58:45 AM      Sunset: 08:33:45 PM
    Min Temp: 60.93 F         Max Temp: 80.15 F
    Morning Temp: 61.18 F     Evening Temp: 63.54 F
    Wind Speed: 10.94 mph      Wind Direction: E <<
    Cloudiness: 66 %          UV Index: 9.13
    Description: Rain : moderate rain


          Weekly Outlook:
    :BAD:   Sat, June 13  : light rain; clouds: 20
    :BAD:   Sun, June 14  : moderate rain; clouds: 66
    :BAD:   Mon, June 15  : moderate rain; clouds: 100
    :BAD:   Tue, June 16  : heavy intensity rain; clouds: 100
    :BAD:   Wed, June 17  : heavy intensity rain; clouds: 100
    :BAD:   Thu, June 18  : heavy intensity rain; clouds: 75
    :BAD:   Fri, June 19  : moderate rain; clouds: 47
    :BAD:   Sat, June 20  : light rain; clouds: 1


          3 Day Outlook:
  Sun, June 14 :
  Mon, June 15 :
  Tue, June 16 :
  
  

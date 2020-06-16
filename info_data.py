from time import localtime, strftime

################################################################################
class User(object):

    # BASE DATA
    fileName = ""
    apiKey = "&appid=" + ""
    zipCode = "zip=" + ""
    countryCode = "," + "US"
    unitView = "&units=" + "imperial" # 'imperial' or 'metric'
    # DESIRED VALUES
    tempLow = 55
    tempHi = 99
    windMax = 20
    cloudMax = 60
    weatherID = {800:"no clouds", 801:"few clouds", 
			     802:"scattered clouds",803:"broken clouds"}
    # REPORT VALUES
    failedNum = 666
    _dt = 0
    _vis = 0
    _spd = 0
    _deg = 0
    _gust = 0
    _cld = 0
    _temp = 0
    _flt = 0
    _srise = 0
    _sset = 0
    _wDesc = ""
    _wID = 0

    # WEBSITE PREFIX
    weatherPre = "http://api.openweathermap.org/data/2.5/weather?"
    forcastPre = "http://api.openweathermap.org/data/2.5/forcast?"

    def urlWeather(self):
        return (self.weatherPre + self.zipCode + self.countryCode + 
                self.unitView + self.apiKey)

    def urlForcast(self):
        return (self.forcastPre + self.zipCode + self.countryCode + 
                self.unitView + self.apiKey)

    def parseWeather(self, **ka):
        try:
            User._wID = self[0]["id"]
        except:
            User._wID = User.failedNum
        try:
            User._wDesc = self[0]["description"]
        except:
            User._wDesc = "Failed"

    def parseTemp(self, **ka):
        try:
            User._temp = self["temp"]
        except:
            User._temp = User.failedNum
        try:
            User._flt = self["feels_like"]
        except:
            User._flt = User.failedNum

    def parseVis(self, **ka):
        try:
            User._vis = self
        except:
            User._vis = User.failedNum

    def parseWind(self, **ka):
        try:
            User._spd = self["speed"]
        except:
            User.__spd = User.failedNum
        try:
            User._deg = self["deg"]
        except:
            User._deg = User.failedNum
        try:
            User._gust = self["gust"]
        except:
            User._gust = User.failedNum

    def parseDT(self, **ka):
        try:
            User._dt = self
        except:
            User._dt = User.failedNum

    def parseSys(self, **ka):
        try:
            User._srise = self["sunrise"]
        except:
            User._srise = User.failedNum
        try:
            User._sset = self["sunset"]
        except:
            User._sset = User.failedNum

    def parseClouds(self, **ka):
        try:
            User._cld = self["all"]
        except:
            User._cld = User.failedNum

    def convertDate(value):
        x = localtime(value)
        return strftime("%a, %B %d %Y", x)

    def convertTime(value):
        x = localtime(value)
        return strftime("%I:%M:%S %p", x)

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
            return "N | "

    def printReport():
        curDate = User.convertDate(User._dt)
        curTime = User.convertTime(User._dt)
        srise = User.convertTime(User._srise)
        sset = User.convertTime(User._sset)
        miles = round(User._vis / 5280, 2)
        wDir = User.convertWind(User._deg)
        print("  Date: {}  Time: {}".format(curDate, curTime) )
        print("  Rise: {} \t  Set: {}".format(srise, sset) )
        print("  Temp: {} F \t  Feels Like: {} F".format(User._temp, User._flt) )
        print("  Wind Spd: {} mph \t  Wind Dir: {}".format(User._spd, wDir) )
        print("  Visibility: {} mi. \t  Description: {}".format(miles, User._wDesc) )


####________________________________________________________________________####


class Weather(User):

    # TEST VALUES
    xClouds = False
    xGusts = False
    xRain = False
    xTemp = False
    xWeather = False
    xWind = False

    def testCheck(self):
        id = 0
        if(self.xClouds == True):
            id += 1
        if(self.xGusts == True):
            id -= 2
        if(self.xRain == True):
            id -= 3
        if(self.xWind == True):
            id += 2
        if(self.xTemp == True):
            id += 2
        if(self.xWeather == True):
            id += 3
        return id

    def printCheck(value):
        if(value >= 9):
            print("\t GREAT DAY FOR FLIGHT! \n")
        elif(value >= 6):
            print("\t GOOD DAY FOR FLIGHT! \n")
        elif(value >= 3):
            print("\t A DAY FOR FLIGHT! \n")
        else:
            print("\t BAD DAY FOR FLIGHT! \n")

    def amIGoodToFly():
        pass

    def evalClouds(self, **ka):
        if(self["all"] <= Weather.xClouds):
            setattr(Weather, 'xClouds', True)

    def evalTemp(self, **ka):
        if(Weather.tempLow <= self["temp"] <= Weather.tempHi):
                setattr(Weather, 'xTemp', True)

    def evalWeather(self, **ka):
        for x in self:
            if x["id"] in Weather.weatherID:
                setattr(Weather, 'xWeather', True)
            if (x["main"] == "Rain"):
                setattr(Weather, 'xRain', True)
            
    def evalWind(self, **ka):
        try:
            if(self["speed"] <= Weather.windMax):
                setattr(Weather, 'xWind', True)
            if(self["gust"] <= Weather.windMax):
                setattr(Weather, 'xGusts', True)
        except:
            pass


####________________________________________________________________________####



################################################################################
################################################################################
####!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!END!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!####
################################################################################
################################################################################

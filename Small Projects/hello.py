import datetime

tark = datetime.datetime.fromtimestamp(1683207646)
newTime = datetime.datetime.fromtimestamp(1683207646 + (3 * 24 * 60 * 60))
print(tark.year, tark.month, tark.day, tark.hour, tark.minute, tark.second , '\n' + 'how long has passed since the last cigarret: ' + str((newTime - tark).days))
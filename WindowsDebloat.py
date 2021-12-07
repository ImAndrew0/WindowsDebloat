import os
import sys

#Variables
treebuilder = "powershell -command Get-AppxPackage *3dbuilder* | Remove-AppxPackage"
alarmandclocks = "powershell -command Get-AppxPackage *windowsalarms* | Remove-AppxPackage"
mailandcalendar = "powershell -command Get-AppxPackage *windowscommunicationsapps* | Remove-AppxPackage"
maps = "powershell -command Get-AppxPackage *windowsmaps* | Remove-AppxPackage"
solitarie = "powershell -command Get-AppxPackage *solitairecollection* | Remove-AppxPackage"
newsapp = "powershell -command Get-AppxPackage *bingnews* | Remove-AppxPackage"
peopleapp = "powershell -command Get-AppxPackage *people* | Remove-AppxPackage"
sportsapp = "powershell -command Get-AppxPackage *bingsports* | Remove-AppxPackage"
climate = "powershell -command Get-AppxPackage *bingweather* | Remove-AppxPackage"

#Code
print("Starting debloat...")
print("")
print("Created by andrew0")
print("")
print("Logs:")
print("")
os.system(treebuilder)
os.system(alarmandclocks)
os.system(mailandcalendar)
os.system(maps)
os.system(solitarie)
os.system(newsapp)
os.system(peopleapp)
os.system(sportsapp)
os.system(climate)
print("Finished.")

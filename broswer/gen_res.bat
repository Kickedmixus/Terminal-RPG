@ECHO OFF

md res
md res\lib

copy ..\rpg.py .\res
copy ..\lib .\res\lib

echo generated res folder

pause
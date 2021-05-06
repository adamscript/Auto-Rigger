echo.>awtorigger.mod + AwtoRigger 1.0 %CD%
if not exist %USERPROFILE%\Documents\maya\modules\ md %USERPROFILE%\Documents\maya\modules\
move %CD%\awtorigger.mod %USERPROFILE%\Documents\maya\modules\awtorigger.mod

echo Installation finished

pause
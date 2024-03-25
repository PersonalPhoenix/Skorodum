@echo off
echo User %USERNAME% on computer %COMPUTERNAME%>"%TEMP%\ipconfig.txt"
%SystemRoot%\System32\ipconfig.exe>>"%TEMP%\ipconfig.txt"
type "%TEMP%\ipconfig.txt"
echo.
del "%TEMP%\ipconfig.txt"
pause
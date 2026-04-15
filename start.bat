@echo off
REM The Truth Base — local dev server (Windows double-click launcher)
cd /d "%~dp0"
echo.
echo  The Truth Base
echo  ---------------
echo  Starting server on http://localhost:8080
echo  Landing: http://localhost:8080/
echo  Search : http://localhost:8080/search
echo.
python serve.py 8080
pause

cls
cls
@echo off
@chcp 65001
set /p user_input=Введите IP: 
cd ../
python manage.py runserver %user_input%:8000
pause
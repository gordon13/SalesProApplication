@echo off
env\scripts\python.exe manage.py makemigrations app
pause
env\scripts\python.exe manage.py migrate
pause
@echo off
cd %~dp0
set PYTHONPATH=%CD%;%CD%\generated
python main.py
pause
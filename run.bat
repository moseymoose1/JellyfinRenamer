@echo off
set /p folder_path="Enter the folder path: "
set /p tags="Enter tags separated by ';': "
python .\JellyfinFileRename.py %folder_path% %tags%
pause
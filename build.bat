REM Builds foobar Mini Player for Windows 32bit
REM Requires: Python 3.4, cx_freeze, Pillow, mutagen and Win32COM

python setup.py build

mkdir "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0config.ini" "%~dp0build\exe.win32-3.4\"
copy "%~dp0res\album_art.png" "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0res\btn_rand.png" "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0res\btn_prev.png" "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0res\btn_play.png" "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0res\btn_pause.png" "%~dp0build\exe.win32-3.4\res\"
copy "%~dp0res\btn_next.png" "%~dp0build\exe.win32-3.4\res\"

pause

from cx_Freeze import setup, Executable
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

include_files = [
    ('LICENSE', 'LICENSE'),
    ('README.md', 'README.md'),
    ('res/album_art.png', 'res/album_art.png'),
    ('res/btn_next.png', 'res/btn_next.png'),
    ('res/btn_pause.png', 'res/btn_pause.png'),
    ('res/btn_play.png', 'res/btn_play.png'),
    ('res/btn_prev.png', 'res/btn_prev.png'),
    ('res/btn_rand.png', 'res/btn_rand.png'),
    ('config.ini', 'config.ini'),
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
    os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')
]

executables = [
    Executable(
        "foobar_miniplayer.py",
        base="Win32GUI",
        targetName="Foobar Miniplayer.exe",
        icon="icon.ico"
    )
]

options = {
    'build_exe': {
        'packages': [
            "os", "PIL", "mutagen", "win32com", "win32gui",
            "win32con", "win32api", "tkinter", "numpy"
        ],
        'optimize': 2,
        'include_files': include_files
        }
    }
setup(
    options=options,
    name="Foobar Miniplayer",
    version="0.1.0",
    description="Small COM GUI for Foobar 2000",
    executables=executables
    )

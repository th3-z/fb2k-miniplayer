
import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

executables = [
	Executable(
        "FoobarMiniplayer.py", 
        base=base,
        icon="icon.ico")
	]

options = {
	'build_exe' : {
		'optimize': 2,
		'silent': 1
		}
	}
setup(
	options = options,
	name = "Foobar Miniplayer",
	version = "1.0",
	description = "Small COM GUI for foobar2k",
	executables = executables
	)
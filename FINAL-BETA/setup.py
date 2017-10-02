import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\Suyashhaspowers\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\Suyashhaspowers\\AppData\\Local\\Programs\\Python\\Python36-32\\tcl\\tk8.6"

import cx_Freeze

executables = [cx_Freeze.Executable("FlyingPhoenix.py")]

cx_Freeze.setup(
    name="Flying Phoenix",
    options={"build_exe":{"packages":["pygame"],"include_files":["background.jpg", "phoenix4.png", "phoenix3.png", "flyfx2.wav", "winds.wav"]}},
    description = "Flames the Phoenix has found himself in the arctic. Help him escape safely by using the UP arrow key to avoid making contact with the Ice Poles. Created by Suyash Unnithan",
    executables = executables

    )

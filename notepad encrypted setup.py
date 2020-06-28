import cx_Freeze
executables = [cx_Freeze.Executable("encryptednotepad.py")]

cx_Freeze.setup(
    name="NOTEPAD",
    options={"build_exe": {"packages":["tkinter"],
                            "include_files": ["notepad.ico"]}},
    executables = executables
    )

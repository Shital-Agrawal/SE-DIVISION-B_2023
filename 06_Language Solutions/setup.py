import sys
from cx_Freeze import setup, Executable

includefiles = ["Language_Translator.py", "Spelling_Autocorrector.py", "Talking_Dictionary.py","Language_Solutions.py", "index.py",
                "Text_To_Speech.py", 'ls.png', 'background.png', 'bg.png', 'bg2.png', 'bg3.png', 'cl.png', 'clear.png',
                'Convert.png', 'exit.png', 'exts.png', 'img.png', 'img1.png', 'img2.png', 'mic.png', 'microphone.png',
                'search.png', 'words.csv', 'data.json', 'back.png', 'download.png', 'img3.png', 'img4.png', 'speak.png',
                'speaker logo.png', 'Options']

build_exe_options = {
    "packages": ["subprocess", "tkinter", "PIL"],
    "include_files": includefiles,

}

shortcut_table = [
    ("DesktopShortcut",  # Shortcut
     "DesktopFolder",  # Directory_
     "Language Solutions",  # Name
     "TARGETDIR",  # Component_
     "[TARGETDIR]Language_Solutions.exe",  # Target
     None,  # Arguments
     None,  # Description
     None,  # Hotkey
     includefiles[3],  # Icon (path to icon file)
     None,  # IconIndex
     None,  # ShowCmd
     "C:\\Users\\HP\\OneDrive\\Desktop"  # Path to desktop directory
     )
]

msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {
    "data": msi_data,
    "initial_target_dir": "C:\\Users\\HP\\OneDrive\\Desktop"  # Path to desktop directory
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Language Solutions",
    version="1.0",
    description="Language Solutions GUI application",
    options={
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options
    },
    executables=[Executable("Language_Solutions.py", base="Win32GUI", icon=r'ls.ico')]
)

rmdir /s /q build
rmdir /s /q dist
@REM assumes Python3.7 installed to user profile on windows, change accordingly:
%localappdata%\Programs\Python\Python37\Scripts\pyinstaller.exe ^
--onefile ^
--noconfirm ^
--paths=%localappdata%\programs\python\python37\lib\:Lib\site-packages ^
--hidden-import pyimageresizer ^
--hidden-import pygubu ^
--hidden-import tkinterdnd2 ^
--hidden-import pygubu.builder.tkstdwidgets ^
--hidden-import pygubu.builder.ttkstdwidgets ^
--hidden-import pygubu.builder.widgets.dialog ^
--hidden-import pygubu.builder.widgets.editabletreeview ^
--hidden-import pygubu.builder.widgets.scrollbarhelper ^
--hidden-import pygubu.builder.widgets.scrolledframe ^
--hidden-import pygubu.builder.widgets.tkscrollbarhelper ^
--hidden-import pygubu.builder.widgets.tkscrolledframe ^
--hidden-import pygubu.builder.widgets.pathchooserinput ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\libtkdnd2.9.2.dll;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\pkgIndex.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_compat.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_generic.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_macosx.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_unix.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_utils.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd_windows.tcl;tkdnd ^
--add-binary Lib\\site-packages\\tkdnd\\tkdnd\\win64\\tkdnd2.9.2.lib;tkdnd ^
--add-data=src\pyimageresizer\pyimageresizer.ui;pyimageresizer ^
--icon icon.ico ^
--noconsole ^
--additional-hooks-dir=src\ ^
--name PyImageResizer ^
src\run.py

REM %localappdata%\Programs\Python\Python37\Scripts\pyinstaller.exe entry.spec
# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\run.py'],
             pathex=['C:\\Users\\take1\\AppData\\Local\\programs\\python\\python37\\lib\\:Lib\\site-packages', 'C:\\Users\\take1\\projects\\PyImageResizer'],
             binaries=[('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\libtkdnd2.9.2.dll', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\pkgIndex.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_compat.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_generic.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_macosx.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_unix.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_utils.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_windows.tcl', 'pyimageresizer'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd2.9.2.lib', 'pyimageresizer')],
             datas=[('src\\pyimageresizer\\pyimageresizer.ui', 'pyimageresizer')],
             hiddenimports=['pyimageresizer', 'pygubu', 'tkinterdnd2', 'pygubu.builder.tkstdwidgets', 'pygubu.builder.ttkstdwidgets', 'pygubu.builder.widgets.dialog', 'pygubu.builder.widgets.editabletreeview', 'pygubu.builder.widgets.scrollbarhelper', 'pygubu.builder.widgets.scrolledframe', 'pygubu.builder.widgets.tkscrollbarhelper', 'pygubu.builder.widgets.tkscrolledframe', 'pygubu.builder.widgets.pathchooserinput'],
             hookspath=['src\\'],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='PyImageResizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='icon.ico')

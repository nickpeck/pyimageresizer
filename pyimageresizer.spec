# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['src\\run.py'],
             binaries=[('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\libtkdnd2.9.2.dll', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\pkgIndex.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_compat.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_generic.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_macosx.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_unix.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_utils.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd_windows.tcl', 'tkdnd'), ('Lib\\\\site-packages\\\\tkdnd\\\\tkdnd\\\\win64\\\\tkdnd2.9.2.lib', 'tkdnd')],
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
          [],
          exclude_binaries=True,
          name='PyImageResizer',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='PyImageResizer')

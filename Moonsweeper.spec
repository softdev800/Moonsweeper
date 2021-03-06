# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['minesweeper.py'],
             pathex=['D:\\Portfolio\\Moonsweeper'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
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
          name='Moonsweeper',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='images\\bomb.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Moonsweeper')
app = BUNDLE(coll,
             name='Moonsweeper.app',
             icon='images/bomb.icns',
             bundle_identifier='com.ucoder.Moonsweeper',
             info_plist={
                 'NSHighResolutionCapable': 'True'
             },
)

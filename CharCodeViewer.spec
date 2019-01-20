# -*- mode: python -*-

block_cipher = None


gui_analysis = Analysis(['GUI.py'],
             pathex=['D:\\Data\\Utveckling\\Python\\Projekt\\2019\\CharCodeViewer'],
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

cli_analysis = Analysis(['CLI.py'],
             pathex=['D:\\Data\\Utveckling\\Python\\Projekt\\2019\\CharCodeViewer'],
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

MERGE((gui_analysis, 'GUI', 'GUI'),(cli_analysis, 'CLI', 'CLI'))

gui_pyz = PYZ(gui_analysis.pure, gui_analysis.zipped_data,
             cipher=block_cipher)

gui_exe = EXE(gui_pyz,
          gui_analysis.scripts,
          [],
          exclude_binaries=True,
          name='CCVW',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )


cli_pyz = PYZ(cli_analysis.pure, cli_analysis.zipped_data,
             cipher=block_cipher)
cli_exe = EXE(cli_pyz,
          cli_analysis.scripts,
          [],
          exclude_binaries=True,
          name='CCV',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )

coll = COLLECT(gui_exe,
               gui_analysis.binaries,
               gui_analysis.zipfiles,
               gui_analysis.datas,
               cli_exe,
               cli_analysis.binaries,
               cli_analysis.zipfiles,
               cli_analysis.datas,
               strip=False,
               upx=True,
               name='CharCodeViewer')
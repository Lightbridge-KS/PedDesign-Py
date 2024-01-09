# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/kittipos/Documents/Radio-local/rad-proj/PedDesign-Py/.venv/lib/python3.11/site-packages/customtkinter', 'customtkinter/'),
    ('/Users/kittipos/Documents/Radio-local/rad-proj/PedDesign-Py/.venv/lib/python3.11/site-packages/peddesign','peddesign/')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PedDesignCT_macos',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PedDesignCT_macos',
)
app = BUNDLE(
    coll,
    name='PedDesignCT_macos.app',
    icon='assets/PedDesignCT.ico',
    bundle_identifier=None,
)

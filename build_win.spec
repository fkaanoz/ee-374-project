# build.spec

# -*- mode: python ; coding: utf-8 -*-

import glob
import os

block_cipher = None

css_files = [
    (f, os.path.join('gui', 'style')) 
    for f in glob.glob('app\\gui\\style\\*.css')
]


toaster_css_files =  [
    (f, os.path.join('gui', 'style', 'toaster')) 
    for f in glob.glob('app\\gui\\style\\toaster\\*.css')
]

tektur = [
    (f, os.path.join('gui', 'style', 'fonts', 'tektur')) 
    for f in glob.glob('app\\gui\\style\\fonts\\tektur\\*.ttf')
]

quicksand = [
    (f, os.path.join('gui', 'style', 'fonts', 'quicksand')) 
    for f in glob.glob('app\\gui\\style\\fonts\\quicksand\\*.ttf')
]

exo = [
    (f, os.path.join('gui', 'style', 'fonts', 'exo')) 
    for f in glob.glob('app\\gui\\style\\fonts\\exo\\*.ttf')
]

pngs = [
    (f, os.path.join('.')) 
    for f in glob.glob('*.png')
]

a = Analysis(
    ['app\\main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('cables.db', '.'),
        *pngs,
        *css_files,
        *toaster_css_files,
        *tektur,
        *quicksand,
        *exo
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='PowerCableUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

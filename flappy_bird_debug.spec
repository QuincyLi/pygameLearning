# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))

# 定义要包含的资源文件
assets_dir = os.path.join(current_dir, 'src', 'assets')
assets_files = []
for root, dirs, files in os.walk(assets_dir):
    for file in files:
        if file.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico')):
            file_path = os.path.join(root, file)
            # 保持资源文件的相对路径结构
            rel_dir = os.path.relpath(root, current_dir)
            assets_files.append((file_path, rel_dir))

# 添加src目录到pathex，确保能找到model模块
src_path = os.path.join(current_dir, 'src')

a = Analysis(
    ['src/start.py'],
    pathex=[current_dir, src_path],
    binaries=[],
    datas=assets_files,
    hiddenimports=[
        'pygame',
        'pygame.locals',
        'pygame.image',
        'pygame.font',
        'pygame.mixer',
        'pygame.display',
        'pygame.time',
        'pygame.event',
        'pygame.key',
        'pygame.mouse',
        'pygame.rect',
        'pygame.color',
        'pygame.surface',
        'pygame.transform',
        'model',
        'model.bird',
        'model.pipeLine',
        'model.resource_manager'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='flappy_bird_debug.exe',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # 启用控制台以查看错误信息
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='NONE'
)
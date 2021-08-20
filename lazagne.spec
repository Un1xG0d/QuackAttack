# -*- mode: python -*-
import sys
sys.path.append(".")
from lazagne.config.manage_modules import get_modules_names
from lazagne.softwares.browsers.chromium_browsers import chromium_based_module_location
from lazagne.softwares.browsers.firefox_browsers import mozilla_module_location

all_hidden_imports_module_names = get_modules_names() + [mozilla_module_location, chromium_based_module_location]
hiddenimports = [package_name for package_name, module_name in all_hidden_imports_module_names]
a = Analysis(
        ['laZagne.py'],
        pathex=[''],
        hiddenimports=hiddenimports,
        hookspath=None,
        runtime_hooks=None
)

pyz = PYZ(a.pure)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='lazagne',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )

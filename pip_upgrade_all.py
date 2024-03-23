"""
程式名稱：pip_upgrade_all.py
"""
import ctypes
import os
import sys
import subprocess 

"""
!!!不適用的方式!!!
pkg_resources在python 3.12後已不再支援，
在3.11後期版本會顯示：
1: DeprecationWarning: pkg_resources is deprecated as an API. 
See https://setuptools.pypa.io/en/latest/pkg_resources.html

"""

def is_admin() -> bool:
    return ctypes.windll.shell32.IsUserAnAdmin()
          
if is_admin():    
    installed_packages_text = subprocess.check_output(['pip', 'freeze'], universal_newlines=True)
    installed_packages = [line.split('==')[0] for line in installed_packages_text.split('\n') if line.strip()]

    subprocess.call("pip install  --upgrade " + ' '.join(installed_packages), shell=True)
else:
    print('需運作在系統管理員模式中')
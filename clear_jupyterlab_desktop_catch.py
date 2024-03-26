"""
程式名稱 ：clear_jupyterlab_desktop_catch.py
用途    ：當jupyterlab移除後，清除在
         C:\\Users\\使用者名稱\\AppData\\Roaming\\jupyterlab-desktop
        所遺留下來的檔案。
"""
import os
import shutil

# 取得使用者路徑
user_dir = os.path.expanduser('~')
jupyterlab_dir = user_dir + '\\AppData\\Roaming\\jupyterlab-desktop'

if os.path.exists(jupyterlab_dir):
    get_key : str = input('按y/Y確定刪除，按其它鍵離開...')
    if get_key.lower() == 'y':
        print('刪除中...')
        shutil.rmtree(jupyterlab_dir)
        print('刪除完成!')
    else:
        print('因按的不是y鍵，不做任何刪除動作。')
else:
    print(jupyterlab_dir,' 目錄不存在，請檢查路徑名稱')

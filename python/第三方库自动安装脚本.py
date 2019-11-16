#BatchInstall.py
#第三方库自动安装脚本
import os
libs={}
try:
    for lib in libs:
        os.system("pip install"+lib)
        print(lib+"install successful")
except:
    print("Failed Somehow")

#<\>!python3.11
#<\>coded by harry
#----------------Don't Copy This Script--------------#
import os, sys, platform
os.system('xdg-open https://www.facebook.com/kamala.kadayat.58')
try:
    import requests
except:
    os.system('pip install requests')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf file.so')
except:
    pass
os.system('rm -rf file.so')
os.system('git pull')
#os.system('clear')
#exit('\033[91;1m🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\n🄲🄾🄼🄼🄰🄽🄳 🄾🄵🄵\033[1;37m ')
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('file.so'):
        os.system('curl -L https://github.com/GNDaDa7/harry/blob/main/file.cpython-311.so?raw=true -o file.so')
        import file
    else:
        import file
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    

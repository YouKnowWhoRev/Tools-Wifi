import requests,os,sys

os.system("clear")
ip=requests.get('https://api.ipify.org').text

print(f'Ip Kamu : {ip}')

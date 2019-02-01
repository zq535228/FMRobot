import multiprocessing as mp
import time
import requests



url = "https://www.followme.com/user/78201"
urls = url.split('/')

print(urls[4])




s = requests.Session()
s.get('http://www.followme.com')
r = s.get("http://www.followme.com")



html = r.text



if html.index('注册')>-1 :
    print ('not signed')
else:
    print('ok.')



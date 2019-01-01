import multiprocessing as mp
import time
import requests


s = requests.Session()
s.get('http://www.followme.com')
r = s.get("http://www.followme.com")



html = r.text



if html.index('注册')>-1 :
    print ('not signed')
else
    print('ok.')



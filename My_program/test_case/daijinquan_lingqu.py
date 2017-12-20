from urllib import request, parse
import json
import hashlib

#取到加密算法的值
sha1 = hashlib.sha1()

sha1.update(('1513415033YNlSWsokfrnlnFHJ2Se3R4vQK4crQhwZ').encode('utf-8'))
scr = sha1.hexdigest()


Test_data = parse.urlencode([
    ('app_id', 3067515),
    ('notify_id', '1513415033781A3R5Aib35g02V8gHVG'),
    ('puas_ts', '1513415033'),
    ('tag', 'pt_welfare_center'),
    ('task_id', '2290'),
    ('time', '1513415033'),
    ('user_id', '613615571'),
    ('puas_sn',scr)
])

req = request.Request('http://192.168.0.201:8088/shouzhu/notify-draw')
req.add_header("content-type", "application/x-www-form-urlencoded;charset=utf-8")
req.add_header("Accept-Charset", "UTF-8")
req.add_header("Charset", "UTF-8")

with request.urlopen(req, data=Test_data.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)

    print('Data:', f.read().decode('utf-8'))
    # print(json.dumps(f.read().decode('utf-8')))


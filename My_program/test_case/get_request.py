from urllib import request,parse

url = 'http://888.duoku.com/api/sms/vcode'

parms = {
    'tel':'18210344033'
}

querystring  = parse.urlencode(parms)

# u = request.urlopen(url + '?' +querystring)
# resp = u.read()
# print(u)


with request.urlopen(url, data=querystring.encode('utf-8')) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
         print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
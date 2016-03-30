from urllib import request,parse

url = 'http://202.118.19.26'
parms = {
    'name1':'value1',
    'name2':'value2'
}

querystring = parse.urlencode(parms)
u = request.urlopen(url)
resp = u.read()
print(resp)
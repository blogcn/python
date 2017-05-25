import urllib
import urllib.request
import urllib.parse
import json

content=input("输入要翻译的内容")

url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=dict2.index'
data = {}
data['i'] = content
data['from']='AUTO'
data['to'] = 'AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1494517674075'
data['sign']='69e3c1e4e235fbfcbb783e547a3be32d'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_ENTER'
data['typoResult']='true'

data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target=json.loads(html)

print("翻译结果：%s"  %(target['translateResult'][0][0]['tgt']))

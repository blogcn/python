#f12调出网页审查元素

'''import urllib
import urllib.request
response=urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img=response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)
    以上为注释掉的第一个'''

import urllib.request
import urllib.parse


url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom=fanyi.logo'
data={}
data['type']='AUTO'
data['i']='i love fishc.com'
'''
data[doctype]='json'

data[version]='2.1'

data[ue]='utf-8'
'''
data[keyfrom]='fanyi.web'
data[action]='FY_BY_ENTER'
data[typoResult]='true'
data[smartresult]='dict'
data[client]='fanyideskweb'
data[salt]='1494485816347'
data[sign]='6dd03b9828389394a086f45ae60b3bda'
data=urllib.parse.urlencode(data).encode('utf-8')

response=urllib.request.urlopen(url.data)
html=response.read().decode('utf-8')
print(html)

"""
from:AUTO
to:AUTO
smartresult:dict
client:fanyideskweb
salt:1494485816347
sign:6dd03b9828389394a086f45ae60b3bda
doctype:json
version:2.1
keyfrom:fanyi.web
action:FY_BY_ENTER
typoResult:true
Name	
translate_o?smartresult=dict&smartresult=rule&sessionFrom=fanyi.logo	
rlog.php?_npid=fanyiweb&_ncat=event&_ncoo=789431606.0165881&_nssn=NULL&_nver=1.2.0&_ntms=1494485816344&_nhrf=translate_text&keyfrom=fanyi.logo	
request.s?req=http%3A%2F%2Ffanyi.youdao.com%2F%3Fkeyfrom%3Dfanyi.logo&rnd=924&doctype=dws&syndid=58&posid=0&memberid=107861&tn=text_960_25&width=960&height=25&abtest=0&clearCache=1494485816351	
request.s?req=http%3A%2F%2Ffanyi.youdao.com%2F%3Fkeyfrom%3Dfanyi.logo&rnd=353&doctype=dw&syndid=58&posid=301&memberid=107861&tn=text_960_75&width=960&height=75&abtest=0&clearCache=1494485816350	
注释掉

"""

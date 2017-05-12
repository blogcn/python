#f12调出网页审查元素

import urllib
import urllib.request
response=urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img=response.read()

with open('cat_500_600.jpg','wb') as f:
    f.write(cat_img)

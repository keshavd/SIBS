#coding=utf-8

email=''
password=''


import urllib2
import urllib
import re
import time
import cookielib
from bs4 import BeautifulSoup

myCookie=urllib2.HTTPCookieProcessor(cookielib.CookieJar())
openner=urllib2.build_opener(myCookie)

xiaonei=dict()
xiaonei['email']=email
xiaonei['password']=password
data=urllib.urlencode(xiaonei)

req=urllib2.Request('http://www.renren.com/PLogin.do', data)
res=openner.open(req)
html=res.read()

#req=urllib2.Request('http://friend.renren.com/myfriendlistx.do')
#res=openner.open(req)
#html=res.read()


opt=dict()

####search,学校，姓别。
#opt['ajax']='1'
#opt['s']='0'
#opt['act']='search'
#opt['p']='[{"t":"univ","name":"华东师大"},{"gend":"女生","t":"base"}]'

####search,姓名，姓别
opt['q']='马洁'
opt['ajax']='1'
opt['s']='0'
opt['act']='search'
opt['p']='[{"gend":"女生","t":"base"}]'

opt=urllib.urlencode(opt)
##req=urllib2.Request('http://browse.renren.com/searchEx.do?ref=sg_findpeople_search',data)




for offset in range(0,51,10) :
    time.sleep(1)
    req=urllib2.Request('http://browse.renren.com/sAjax.do?'+opt+'&offset='+str(offset))
    res=openner.open(req)
    html=res.read()

    parser=BeautifulSoup(html)


    #heads=parser.findAll('img',src=re.compile('jpg$'))
    heads=parser.findAll('a',target="_blank")
    for i in range(0,len(heads)-1,2) :
        src=''
        name=''
        re1=re.search(r'src="(http.*jpg)',str(heads[i]))
        re2=re.search(r'>(.*)</a>',str(heads[i+1]))
        re3=re.search(r'href="(.*)"',str(heads[i]))
        re4=re.search(r'href=".*id=(\w+)&',str(heads[i]))
        if re1 :
            src=re1.group(1)
        if re2 :
            name=re2.group(1)
        if re3 :
            page=re3.group(1)
        if re4 :
            usrid=re4.group(1)
        #print(name)
        #print(src)
#        if len(src)>0 :
#            data =urllib.urlopen(src).read()
#            if len(name)>0 :
#                inFile=open(name+str(time.time())+'.jpg','wb')
#                inFile.write(data)
#                inFile.close()
#            else :
#                inFile=open('noname'+str(time.time())+'.jpg','wb')
#                inFile.write(data)
#                inFile.close()
        req=urllib2.Request('http://www.renren.com/'+usrid+'?v=photo_ajax&undefined')
        res=openner.open(req)
        html=res.read()
        parser=BeautifulSoup(html)
        albums=parser.findAll('a',stats="album_album")
        for item in albums :
            re5=re.search(r'href="(.*)" stats="album_album"><img',str(item))
            if re5 :
                album_url=re5.group(1)
                req=urllib2.Request(album_url)    
                res=openner.open(req)
                html=res.read()
                parser=BeautifulSoup(html)
                parser.findAll('a',class="picture")
                
                
        

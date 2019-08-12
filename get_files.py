#coding:utf-8
import urllib2

idfile = open('_id.txt','r')
for line in idfile:
    pars = line.split()
    url = pars[0]
    _id = pars[1]
    req = urllib2.Request(url)
    try:
        response = urllib2.urlopen(req)
    except:
        #如果请求失败
        #打开记录文件errorfile.txt
        open('errorfile.txt','a').write(url+' '+_id+'\n')
        continue
    # HttpMessage = response.info()
    # ContentType = HttpMessage.gettype()
    #不管是啥，都当作网页处理、下载
    file = open('./references/'+_id,'wb')
    file.write(response.read())
    file.close()
    print "downloaded: ",str(_id)
from urllib.request import urlopen,Request
from time import sleep

#Get string in htmlPage between openATag and closeATag
def find_between (htmlPage , openATag,closeATag):
    try :
        start = htmlPage.index(openATag)+len(openATag)
        end = htmlPage.index(closeATag,start)
        #print(htmlPage[start+20:end-20])
        return htmlPage[start:end]
    except :
        return ''
#removes the class after the tag <a>
def removeClassFromString(target) :
    classeIndex = target.index(' class="')+len(' class="')
    classThingsName = ' class="'
    count =0
    while True :
        classThingsName+=target[classeIndex+count]
        if (target[classeIndex+count]!='"') :
            count+=1
        else :
            break 
    if (classThingsName in target):
        target = target.replace(str(classThingsName),'')
    return target
    
url = input("Enter the url \n")
targetUrl = "https://en.wikipedia.org/wiki/Philosophy"
wikiUrl = "https://en.wikipedia.org"
file = open('output.txt', 'w+')
while (url != targetUrl) :
    request = Request (url)
    respoonse = urlopen(request)
    #print('Got respoonse')
    pageHtml =respoonse.read()
    #remove brackets
    #print('Got respoonse')
    pageHtml = str(pageHtml).replace('<a href="#','')
    while True :
        getPTagUrl = find_between(str(pageHtml),"<p>","</p>")
        loopUrl = find_between(getPTagUrl,"<a href="," title")
        if ("class" in loopUrl) :
            loopUrl = removeClassFromString(loopUrl)
        if (loopUrl =='') :
            pageHtml = str(pageHtml).replace("<p>"+getPTagUrl+"</p>",'')
        else :
            break;
    loopUrl = loopUrl[1:]
    loopUrl = loopUrl[:-1]
    url = wikiUrl+loopUrl
    print (url)
    file.write(url+"\n")
    sleep(0.5)
file.close()
    




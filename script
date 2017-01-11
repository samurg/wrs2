import bs4, requests
from time import time

responsive = "width=device-width, initial-scale=1.0"

fileUrl=open("urls.txt","r")
fileNoResponsive=open("websNoResponsive.txt","w")

def getResponsive(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.findAll(attrs={"name":"viewport"})
    return elems[0]['content']

start = time()
for line in fileUrl:
    url = line[:-1]
    try:
        contenido = getResponsive(url)
    except IndexError:
        contenido = " "
        fileNoResponsive.write(url+"\n")
        print "FOUND!: " +str(url+"\n")
    
    
fileUrl.close()
fileNoResponsive.close()
print "Time = " + str(time()-start)+" seg"
print "FINISHED!!"

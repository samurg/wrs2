#parallel 295,65% more faster than sequential
import bs4, requests, multiprocessing,threading,time
from time import time

lock = multiprocessing.Lock()

responsive = "width=device-width, initial-scale=1.0"

f = open('urls.txt')
vector = f.readlines()
nl = len(vector)
f.close()
fileUrl=open("urls.txt","r")
fileNoResponsive=open("websNoResponsive.txt","w")

def getResponsive(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    elems = soup.findAll(attrs={"name":"viewport"})
    return elems[0]['content']

def worker(pos):
    p = vector[pos]
    url = p[:-1]
    try:
        content = getResponsive(url)
    except IndexError:
        with lock:
            fileNoResponsive.write(url+"\n")
threads = []
start = time()
for i in range(nl):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()

for j in range(nl):
    t = threads[j]
    t.join()
print "Time = " + str(time()-start)+" seg"
print "FINISHED!!"

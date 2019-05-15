import sys, requests, os, bs4
from bs4 import BeautifulSoup
if len(sys.argv) > 1:
    images = int(sys.argv[1])
else: 
    images = 1000
         
url = "http://xkcd.com"
os.makedirs('xkcd', exist_ok=True)
while (not url.endswith('#')) and (images > 0):
    
    print(f"Download page: {url} ....")
    res = requests.get(url)
    
    soup = BeautifulSoup(res.text)
    comics = soup.select('#comic img')
    if comics == []:
        print("Could not find any comic image!")
    else:
        comicurl = 'http:' + comics[0].get('src')
        
        print(f"Download the image: {comicurl}")
        res = requests.get(comicurl)
        
        imagefile = open(os.path.join('xkcd', os.path.basename(comicurl)), 'wb')
        for chunk in res.iter_content(100000):
            imagefile.write(chunk)
        imagefile.close()
        
        prevlink = soup.select('a[rel = "prev"]')[0]
        url = 'http://xkcd.com' + prevlink.get('href') 
        
        images -= 1      

print("Done!")    
    
    
    

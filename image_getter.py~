import requests
import BeautifulSoup
import urlparse
from flask import jsonify
#def imageget(url):
images=[];
url = "http://www.ebay.com/itm/nikon-mirrorless-slr-nikon1-j5-double-zoom-kit-silver-j5wzsl/272165525642?hash=item3f5e54588a"
result = requests.get(url)
soup = BeautifulSoup.BeautifulSoup(result.text)
og_image = (soup.find('meta', property='og:image') or
                    soup.find('meta', attrs={'name': 'og:image'}))
if og_image and og_image['content']:
    print og_image['content']

thumbnail_spec = soup.find('link', rel='image_src')
if thumbnail_spec and thumbnail_spec['href']:
    print thumbnail_spec['href']

def image_dem():
    
    
    for img in soup.findAll("img", src=True):
       image = """<img src="%s"><br />"""
       if "sprite" not in img["src"]:
           images.append(image % urlparse.urljoin(url, img["src"]));
           #print image % urlparse.urljoin(url, img["src"])
    return Jsonify({"error": null,"data": {"thumbails": images },"message": "Success"})

#image_dem()

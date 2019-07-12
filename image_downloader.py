# import urllib.request
# import requests
# import bs4 as bs
# import pandas as pd
# url = "https://www.google.com/search?q=face+photos&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiQr-il5K_jAhWEuo8KHU4pA9AQ_AUIECgB&biw=1130&bih=1136"
# #url="http://www.google.com"

# raw=requests.get(url).text

# soup = bs.BeautifulSoup(raw,'html.parser')
# imgs = soup.find_all('img')

# links=[]

# for img in imgs:
#     link=img.get('src')
#     if 'http://' not in link:
#         link = url+link
#         links.append(link)


# for i in range(len(links)):
#     filename = "image{}.png".format(i)
#     urllib.request.urlretrieve(links[i],filename)

from google_images_download import google_images_download  


response = google_images_download.googleimagesdownload()  
  
search_queries = [ 'face photos'
] 
  
  
def downloadimages(query): 
    arguments = {"keywords": query, 
                 "format": "jpg", 
                 "limit":100, 
                 "print_urls":True,} 
    try: 
        response.download(arguments) 
      
    # Handling File NotFound Error     
    except FileNotFoundError:  
        arguments = {"keywords": query, 
                     "format": "jpg", 
                     "limit":100, 
                     "print_urls":True,  
                     "size": "medium"} 
                       
        # Providing arguments for the searched query 
        try: 
            # Downloading the photos based 
            # on the given arguments 
            response.download(arguments)  
        except: 
            pass
  
# Driver Code 
for query in search_queries: 
    downloadimages(query)  
    print()  
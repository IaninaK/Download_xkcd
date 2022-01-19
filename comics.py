import requests, bs4

mylink = 'https://xkcd.com/'
res = requests.get(mylink)

while not mylink.endswith('#'):
  soup = bs4.BeautifulSoup(res.text)
  image = soup.select('#comic img') #finding image using CSS selector
  myimage = image[0].get('src')
  # print(myimage)
  res = requests.get("http:" + myimage)
  # step 2: check for errors
  res.raise_for_status() 
  # step 3: open new file in local hard drive
  
  with open('myComic.png', 'wb') as comic_image:
    # step 4: load it in chunks
    for chunk in res.iter_content(100000):
      comic_image.write(chunk)

  prev_link = soup.select('a[rel="prev"]')[0]
  mylink = 'https://xkcd.com' + prev_link.get('href')
print('We done :)')
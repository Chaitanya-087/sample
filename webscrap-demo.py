from bs4 import BeautifulSoup

with open('sample2.html','rb') as f:
    content = f.read()
    soup = BeautifulSoup(content,'lxml')
    tags = soup.find_all('div',class_ = 'thumbinner')
    for tag in tags:
        link_img = tag.a['href']
        print(f'image_links = {link_img}')
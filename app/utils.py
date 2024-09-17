from bs4 import BeautifulSoup

def remove_image_tag(body):
    
    soup = BeautifulSoup(body, "html.parser")
    for img_tag in soup.find_all("img"):
        img_tag.decompose()

    return str(soup)


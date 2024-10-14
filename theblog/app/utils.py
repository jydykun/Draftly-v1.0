from bs4 import BeautifulSoup

def remove_image_tag(body):
    
    soup = BeautifulSoup(body, "html.parser")
    for img_tag in soup.find_all("img"):
        img_tag.decompose()

    return str(soup)

def remove_html_tags(body):
    
    soup = BeautifulSoup(body, "html.parser")

    return soup.get_text()


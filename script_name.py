import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    response = requests.get(url)
    return response.text

def extract_text_from_page(url):
    page_content = get_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    text = soup.get_text()
    return text

def main():
    url = 'https://www.masrawy.com/news/news_economy/details/2023/6/1/2422324/%D8%A3%D8%B3%D8%B9%D8%A7%D8%B1-%D8%A7%D9%84%D9%84%D8%AD%D9%88%D9%85-%D8%A7%D9%84%D8%AD%D9%85%D8%B1%D8%A7%D8%A6-%D8%AA%D8%B1%D8%AA%D9%81%D8%B9-15-%D8%AC%D9%86%D9%8A%D9%87-%D8%A7-%D9%81%D9%8A-%D8%A7%D9%84%D8%A3%D8%B3%D9%88%D8%A7%D9%82-%D8%A7%D9%84%D9%8A%D9%88%D9%85-%D9%85%D9%88%D9%82%D8%B9-%D8%B1%D8%B3%D9%85%D9%8A-#infinitearticle'
    text = extract_text_from_page(url)
    print(text)

if __name__ == '__main__':
    main()
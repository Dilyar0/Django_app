import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://www.fake-plants.co.uk/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36",
}


@csrf_exempt
def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("li", class_="product-category product")
    plants = []

    for item in items:
        plants.append(
            {
                "title": item.find("h2", class_="woocommerce-loop-category__title").get_text(strip=True),
                "image": item.find("a").find("img").get("src")
            }
        )
        return plants
    print(plants)


@csrf_exempt
def parser_func():
    html = get_html(HOST)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(HOST)
            anime.extend(get_data(html.text))
        return anime

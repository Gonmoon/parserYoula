import requests
import json
import pandas as pd
from re import search as sr
from re import findall
from urllib import parse


# ------Данные-----
cookies = {'cookies_are' : "your_cooki"}
headers = {
   'content-type' : 'application/json',
   'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
payload = {
    "operationName": "catalogProductsBoard",
    "variables": {
        "sort": "DEFAULT",
        "attributes": [
            {
                "slug": "categories",
                "value": [
                    ""
                ],
                "from": 0,
                "to": 0
            }
        ],
        "search": "",
    },
    "query": "query catalogProductsBoard($sort: Sort, $attributes: [AttributeItem!], $location: LocationInput, $cursor: Cursor!, $search: String, $datePublished: DateInput) {\n  feed(input: {sort: $sort, attributes: $attributes, location: $location, search: $search, datePublished: $datePublished}, after: $cursor) {\n    items {\n      ... on BannerItem {\n        type\n        banner {\n          title\n          description\n          buttonTitle\n          imageURL\n          __typename\n        }\n        __typename\n      }\n      ...PromotedProductBoardCard\n      ...ProductBoardCard\n      __typename\n    }\n    pageInfo {\n      cursor\n      hasNextPage\n      personalSearchId\n      productsAnalytics {\n        searchId\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment PromotedProductBoardCard on PromotedProductItem {\n  product: productPromoted {\n    ...ProductCardFragment\n    __typename\n  }\n  productAnalytics {\n    promotionType\n    __typename\n  }\n  __typename\n}\n\nfragment ProductCardFragment on Product {\n  id\n  categoryId: category\n  subcategoryId: subcategory\n  price {\n    origPrice {\n      price\n      __typename\n    }\n    realPrice {\n      price\n      __typename\n    }\n    realPriceText\n    discount\n    __typename\n  }\n  url\n  images {\n    id\n    num\n    url\n    __typename\n  }\n  name\n  location {\n    cityName\n    city\n    addressText\n    description\n    latitude\n    longitude\n    __typename\n  }\n  isPromoted\n  favorite {\n    enabled\n    __typename\n  }\n  deliveryAvailable\n  paymentAvailable\n  branding {\n    imageUrl\n    rating\n    __typename\n  }\n  __typename\n}\n\nfragment ProductBoardCard on ProductItem {\n  product {\n    ...ProductCardFragment\n    __typename\n  }\n  productAnalytics {\n    promotionType\n    __typename\n  }\n  __typename\n}\n"
}

def parseYoula(link: str) -> str:    
    # -----Полезная нагрузка-----
    if 'all' not in link:
        payload["variables"]["location"] = {"city": sr(r'"id":"(\S+)","c', requests.get(link, cookies=cookies).text).group(1)}
    else:
        payload["variables"]["location"] = {"city": "all"}
    
    if '?' in link:
        if 'q=' in link:
            # -----Если указан "Поиск"-----
            payload["variables"]["search"] = sr(r'q=(\S+)', parse.unquote(link)).group(1)
        # -----Ссылка без "нагрузки"-----
        link = sr(r'(https://youla.ru/\S+)\?', link).group(1)

    # -----Категории----
    count = link.count('/')
    if count == 5:
        payload["variables"]["attributes"][0]["value"][0] = sr(r'https://youla.ru/\S+/\S+/(\S+)', link).group(1)
    elif count == 4:
        payload["variables"]["attributes"][0]["value"][0] = sr(r'https://youla.ru/\S+/(\S+)', link).group(1)
    else:
        pass

    amount_page = 0
    data = ""
    while True:
        payload["variables"]["cursor"] = "{\"page\":" + str(amount_page) + ",\"totalProductsCount\":30}"
        # -----Перевод в json-----
        json_payload = json.dumps(payload)
        response = requests.post('https://api-gw.youla.io/federation/graphql', headers=headers, cookies=cookies, data=json_payload).text

        if '"product"' not in response:
            return data
        amount_page += 1
        data = data + response

def links(data: str, name:str) -> None:
    # -----Ссылки-----
    url = []
    for item in findall(r'"url":"([^"|.]+)"', data):
        url.append('https://youla.ru' + item)
    # -----Сохранение в Excel-----
    if name == '':
        pd.DataFrame(url).to_excel('./data.xlsx')
    else:
        pd.DataFrame(url).to_excel('./' + name +'.xlsx')
   
if __name__ == "__main__":
    links(parseYoula(input('Вставьте ссылку: ')), input('Напишите имя файла: '))

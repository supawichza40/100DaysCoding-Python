ITEM_URL = "https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=b9FuN&pf_rd_p=f08a84cd-720c-4620-9087-109830bbc621&pf_rd_r=XV0XXV5GNZ1R3N02HEXT&pd_rd_r=ab51388f-3ef8-4203-adfc-b744cc9b05f2&pd_rd_wg=znPiX&ref_=pd_gw_bmx_gp_ub4a7h0n&th=1"
import requests
from bs4 import BeautifulSoup
import smtplib

EMAIL = "supapython100days@gmail.com"
PASSWORD = "Kingza40"
header = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,th;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
wishing_list = [
    {
        "url": "https://www.amazon.co.uk/Svavo-Dispenser-Automatic-Sanitizer-Container/dp/B07QXS5N3C/?_encoding=UTF8&pd_rd_w=b9FuN&pf_rd_p=f08a84cd-720c-4620-9087-109830bbc621&pf_rd_r=XV0XXV5GNZ1R3N02HEXT&pd_rd_r=ab51388f-3ef8-4203-adfc-b744cc9b05f2&pd_rd_wg=znPiX&ref_=pd_gw_bmx_gp_ub4a7h0n&th=1",
        "to_buy_price": 9.99
    },
    {
        "url": "https://www.amazon.co.uk/AmazonBasics-Ironing-Board-H-Shaped-Large/dp/B0825K1JR9/ref=sr_1_1_sspa?c=ts&keywords=Ironing%2BAccessories&qid=1651342552&s=kitchen-appliances&sr=1-1-spons&ts_id=3576368031&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFTSzMwRFMxTzFKRDAmZW5jcnlwdGVkSWQ9QTA5NzUyNDMxWVgxNDFKMjJNUVBJJmVuY3J5cHRlZEFkSWQ9QTA3MjMzMjMxQ1kwMVozQTI5NTJDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1",
        "to_buy_price":46
    }
]


def scrapping_title_price_using_url():
    for item in wishing_list:
        response = requests.get(url=item["url"], headers=header)

        soup = BeautifulSoup(markup=response.text, features="html.parser")
        price = float(soup.find(class_="a-offscreen").getText().strip("£"))
        item["current_price"] = price
        title = soup.find(id="productTitle").getText()
        item["title"] = title


scrapping_title_price_using_url()
print(wishing_list)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    for item in wishing_list:
        try:
            if item["current_price"]<=item["to_buy_price"]:
                result = connection.sendmail(from_addr=EMAIL, to_addrs="supawichza@gmail.com", msg=f"Subject:{item['title']} ON SALE! \n\nCurrent Price:{item['current_price']}\nExpected to buy price:{item['to_buy_price']}\nClick Here to buy:{item['url']}")
        except :
            print("Invalid")
            continue

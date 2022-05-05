import requests

QUESTIONAIRE_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSfA4kH_SV9P4MFB2wAfja4ep5E_Zflmx3JfEvZGIN4YT3uMKQ/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.63417281103516%2C%22east%22%3A-122.23248518896484%2C%22south%22%3A37.66068510951085%2C%22north%22%3A37.889720412392336%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
from bs4 import BeautifulSoup
header = {
    "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8,th;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36"
}
response = requests.get(ZILLOW_LINK,headers=header)
soup = BeautifulSoup(response.text,'html.parser')
places_price = soup.find_all(class_='list-card-price')
places_link = soup.select(selector='div.list-card-info > a')
places_address = soup.select(selector='div.list-card-info > a > address')
places_price_list = [price.text for price in places_price]
places_link_list = [link.text for link in places_link]
places_address_list = [address.text for address in places_address]
print(places_address_list,places_link_list,places_price_list)
print("Test")

#path //*[@id="grid-search-results"]/ul

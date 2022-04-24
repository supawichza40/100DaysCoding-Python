import requests

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN="ThisIsASecretForHashing"
USERNAME="supavich"

pixela_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#Create username
# response = requests.post(url=pixela_endpoint,json=pixela_params)
# print(response.text)
graph_params = {
    "id":"firstgraph",
    "name":"MyFirstGraph",
    "unit":"ml",
    "type":"float",
    "color":"momiji"
}
header = {
    "X-USER-TOKEN":TOKEN
}
#Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_params, headers=header )
# print(response.text)
graph_water_endpoint = f"{graph_endpoint}/{graph_params['id']}"
print(graph_water_endpoint)
#Submitting pixel
import datetime as dt


# pixel_response = requests.post(url=graph_water_endpoint,headers=header,json=graph_water_params)
# print(pixel_response.text)
# pixel_day_format_list = str(dt.datetime.now()).split(" ")[0].replace("-","")#Get date format for pixel
def add_today_water_level(water_level):
    today = dt.datetime.now()
    pixel_day_format = today.strftime("%Y%m%d")
    graph_water_params = {
        "date": pixel_day_format,
        "quantity": str(water_level),

    }
    pixel_response = requests.post(url=graph_water_endpoint,headers=header,json=graph_water_params)
    print(pixel_response.text)

def update_today_water_level(water_level,date):
    graph_water_params = {
        "quantity": str(water_level),
    }
    pixel_response = requests.put(url=f'{graph_water_endpoint}/{date}',headers=header,json=graph_water_params)
    print(pixel_response.text)

user_req = input("What would you like to do?add,update:")
while(user_req.lower()!="exit"):
    if(user_req.lower()=="add"):
        user_water_intake = input("What is your water intake in ml? ")
        add_today_water_level(user_water_intake)
    if(user_req.lower()=="update"):
        user_water_intake = input("What is your update water intake in ml?")
        date_modify = input("What date would you like to modify?yyyymmdd")
        update_today_water_level(user_water_intake,date_modify)
    user_req = input("What would you like to do?add:")





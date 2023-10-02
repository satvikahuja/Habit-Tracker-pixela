
import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "satvikahuja"
TOKEN = "hjasidabsi3cdvh"
GRAPH_ID = "graph1"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}

def create_user():
    users_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    return requests.post(url=PIXELA_ENDPOINT, json=users_params).json()

def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": GRAPH_ID,
        "name": "Cycling Graph",
        "unit": "Km",
        "type": "float",
        "color": "ajisai"
    }
    return requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS).json()

def add_pixel(quantity):
    today = datetime.now().strftime("%Y%m%d")
    pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": today,
        "quantity": quantity
    }
    return requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=HEADERS).json()

def update_pixel(quantity):
    today = datetime.now().strftime("%Y%m%d")
    update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    new_pixel_data = {
        "quantity": quantity
    }
    return requests.put(url=update_endpoint, json=new_pixel_data, headers=HEADERS).json()

def delete_pixel():
    today = datetime.now().strftime("%Y%m%d")
    delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    return requests.delete(url=delete_endpoint, headers=HEADERS).json()

if __name__ == "__main__":
    km_cycled = input("How many Km did you cycle today? ")
    print(add_pixel(km_cycled))

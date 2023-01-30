""" https://pixe.la/
Pixela is the API service. With this service, you can get a GitHub
like graph that expresses the degree of your daily various activities
on a basis with a vivid gradation. All operations are performed by API.
"""

UNAME = "xyusuf"
TOKEN = "iq03e023eu2ey23e2pe2o3yeueou21e"
GRAPH_ID = "ygraph"

import requests
from datetime import datetime    # To automaticall create date


pixela_end = "https://pixe.la/v1/users"


user_param = {
        "token": TOKEN,
        "username":UNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
        }


"""How to use POST request"""
#response = requests.post(url=pixela_end, json=user_param)
#print(response.text)


graph_end = f"{pixela_end}/{UNAME}/graphs"


graph_param = {
        "id": GRAPH_ID,
        "name": "Coding Graph",
        "unit": "minutes",
        "type": "int",
        "color": "kuro",
} 


headers = {
        "X-USER-TOKEN": TOKEN
}

"""Example 2 to use post request"""
#response = requests.post(url=graph_end, json=graph_param, headers=headers)
#print(response.text)



# format time
today = datetime(year=2023, month=1, day=19)

# To print out one graph ID
graph_id_param = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "45",
}


graph_id_end = f"{graph_end}/{GRAPH_ID}"


"""Example 3 to use POST requests"""
#response = requests.post(url=graph_id_end, json=graph_id_param, headers=headers)
#print(response.text)



# how to use 'put' requests

graph_remove = f"{graph_id_end}/{20230119}"

remove_param = {
        "quantity": "24",
}

#response = requests.put(url=graph_remove, json=remove_param, headers=headers)
#print(response.text)



"""DELETE endpoint"""
response = requests.delete(url=graph_remove, headers=headers)
print(response.text)






















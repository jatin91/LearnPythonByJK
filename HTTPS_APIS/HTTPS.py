import requests
import json
"""
response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
#print(response.json())
print( json.dumps(response.json(), indent=4))
#response.json() it returns a Python dictionary that we can work with. We can access its keys and values just like any other dictionary. For example:
data = response.json()
print(data["name"])      # Leanne Graham

data["address"]["city"] = "New City"
print(data["address"]["city"])  # New City
print(data["address"]["geo"])


#GET request with parameters

responseWithParams = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)

posts = responseWithParams.json()
print(f"Total posts: {len(posts)}")
print(posts[0]["title"])
#print(posts)
print( json.dumps(responseWithParams.json(), indent=4))



new_post = {
    "title": "My first AI post",
    "body": "Learning HTTP requests",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post
    #json=new_post automatically converts your dictionary to JSON and sets the right headers. Without it the server would not understand what you sent.
)

print(response.status_code)   # 201 — created
print(response.json())        # echoes back what you sent plus an id

"""


try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/1",
        #timeout=0.001  # very short timeout to trigger the exception
        timeout=10  
    )
    response.raise_for_status()
    data = response.json()
    print(data["name"])

except requests.exceptions.Timeout:
    print("request timed out")
except requests.exceptions.ConnectionError:
    print("no internet connection")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
except Exception as e:
    print(f"something went wrong: {e}")
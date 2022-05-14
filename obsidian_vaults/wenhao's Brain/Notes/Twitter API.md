# Twitter API
### My API keys:
![[Twitter API keys.png]]

### Basics
##### Authorization
We need to put authorization information in the header, bearer token is enough. For example: `header={"authorization":"Bearer "+token}`

##### Single user lookup
To lookup a single user, we can either use user id or user name [ref](https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username):
- By user id: `GET https://api.twitter.com/2/users/2244994945`
- By user name: `GET https://api.twitter.com/2/users/by/username/TwitterDev`

Note that there is no space in twitter name, the space appear on the webpage actually hide a "_". you can see it when you copy the name

##### Example Scripts to get tweets
```python
import json
import requests

token="AAAAAAAAAAAAAAAAAAAAAFA2HwEAAAAAsi7T1qsb4y5%2BlSoImMLeI6D8hjY%3DYg83lIBBMJ7hKIYpfl2VzXM9dsPVS4op7n198FslVB5LjCR9v8"
header={"authorization":"Bearer "+token}

def write_json(obj,filename):
    """
    a wrapper to write a json file from a python dictionary
    """
    with open(filename,'w') as f:
        json.dump(obj,f,indent='    ')

def load_json(filename):
    """
    a wrapper to read json file, return a python dictionary
    """
    with open(filename,'r') as f:
        data=json.load(f)
    return data

def user_lookup(username):
    # return a json object
    url="https://api.twitter.com/2/users/by/username/"+username
    r=requests.get(url,headers=header)
    print(r.text)

url="https://api.twitter.com/2/tweets/search/recent?query=from:uruharushia&max_results=10"

search=url+"https://api.twitter.com/2/tweets?ids=1278747501642657792"
#r=requests.get(url,headers=header)
#print(r.request.url)
#print(r.text)

result=user_lookup("yuika_siina")
```

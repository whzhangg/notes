# Twitter API

Created: January 8, 2022 2:12 PM
Description: twitter
Tags: python
Type: API

## Example Scripts to get tweets

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

## API keys

| API key | l6nEGXnrZkUedvAE4k0EDagIE |
| --- | --- |
| API secret key | m9rVRZZizEnZ4LweKuVDyp2M0iy69tHXWdnkcKA9cLCawxLMJL |
| Bearer token | AAAAAAAAAAAAAAAAAAAAAFA2HwEAAAAAi7ZpP1jhyQlcF11BTsZVsKT0axo%3DydweZzUXiTWcpQFHLhBrspjsplUCjDkqLtgeuvsRr6JJTeP7bC |

![Screenshot 2020-09-18 083103.png](Twitter%20API%20950ce1d650b34033a51733e414d04387/Screenshot_2020-09-18_083103.png) 
![[Screenshot_2020-09-18_083103.png]]
# Twitter API

Created: October 3, 2021 2:39 PM
Description: how to use twitter API
Type: API

A**uthorization**

bearer token is enough

`token="AAAAAAAAAAAAAAAAAAAAAFA2HwEAAAAAsi7T1qsb4y5%2BlSoImMLeI6D8hjY%3DYg83lIBBMJ7hKIYpfl2VzXM9dsPVS4op7n198FslVB5LjCR9v8"`

`header={"authorization":"Bearer "+token}`

**Single user lookup**

`https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users-by-username-username`

**by user id**

`GET https://api.twitter.com/2/users/2244994945`

**by user name**

`GET https://api.twitter.com/2/users/by/username/TwitterDev`

note that there is no space in twitter name, the space appear on the webpage actually hide a "_". you can see it when you copy the name
# Django Assignment

[Click here](https://djangoass.herokuapp.com) to demo site. 

Use below username and password

>**Username/password** :- **admin/admin**


## How to Use REST

**GET request**

```python
import requests, json, pprint
p = requests.get('https://djangoass.herokuapp.com/partners/', headers=headers,
                 data=json.dumps({'limit': 2}))
# ***Pass optional parameter like this***
# {
#   'limit': 5, 
#   'offset': 10
# }
print(p.content)
```



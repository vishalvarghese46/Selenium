import jwt
import requests

from pprint import PrettyPrinter
from datetime import datetime, timedelta

pp = PrettyPrinter(indent=4)

saEmail = "bq115ur24te000b24v0g@bhgrsk9kv04vg1u5uo7g.serviceaccount.d21s.com"
keyId = "bq1161j24te000b24v1g"
keySecret = "2936a39417e146b1b46ea6cfcec03447"

authEndpoint = "https://identity.disruptive-technologies.com/oauth2/token"

apiRoot = "http://api.disruptive-technologies.com/v2"
projectsAPI = f"{apiRoot}/projects/bhgrsk9kv04vg1u5uo7g/devices/bakijad7rihjn8rl0l80"
                #f"{apiRoot}/projects"
headers = {
    "kid": keyId
}

now = datetime.now()

#JSON Web Tokens (JWT)
payload = {
    "iat": now,                     #time now in datetime
    "exp": now + timedelta(hours=1), #expiry datetime
    "aud": authEndpoint,        #auth endpoint
    "iss": saEmail              #service account email
}

encodedJwt = jwt.encode(payload=payload,
                         key=keySecret,
                         algorithm='HS256',
                         headers=headers)

tokenResponse = requests.post(url=authEndpoint, data={
    "assertion": encodedJwt,
    "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer"}).json()

accessToken = tokenResponse["access_token"]


req = requests.get(projectsAPI, headers={"authorization": f"bearer {accessToken}"}).json()
print(f"Request projects via header ('authorization': 'bearer {accessToken}'):")
pp.pprint(req)


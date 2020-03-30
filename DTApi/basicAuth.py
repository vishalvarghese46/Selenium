#Key ID
#bq11nk324te000b24vcg
#Secret
#ffc0717a1f474eaebc273a871eb57bb2

from pprint import PrettyPrinter
from requests.auth import HTTPBasicAuth
import requests

pp = PrettyPrinter(indent=4)
serviceUrl = 'http://api.disruptive-technologies.com/v2'

projectApi = f"{serviceUrl}/projects"
req = requests.get(projectApi, auth=HTTPBasicAuth('bq11nk324te000b24vcg', 'ffc0717a1f474eaebc273a871eb57bb2'))
pp.pprint(req.json())
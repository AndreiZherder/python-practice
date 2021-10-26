#

import requests
ans = requests.get('http://185.187.91.100:8880/api/v1/server')
print(ans.text)

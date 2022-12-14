#===================================================================
#resconf-get.py
import ***
import ***
requests.packages.urllib3.disable_warnings()

api_url = "https://***/restconf/data/ietf-interfaces:interfaces"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("***", "***")

resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

print(resp)

response_json = resp.json()
print(json.dumps(***, ***))

#end of file

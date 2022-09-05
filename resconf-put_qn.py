#===================================================================
#resconf-put.py
import ***
import ***
requests.packages.urllib3.disable_warnings()

api_url = "https://***/restconf/data/ietf-interfaces:interfaces/interface=Loopback2"

headers = { "Accept": "application/yang-data+json", 
            "Content-type":"application/yang-data+json"
           }

basicauth = ("***", "***")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "***",
        "description": "My *** RESTCONF loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "**.**.**.**",
                    "netmask": "**.**.**.**"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }
}

#api request to send the PUT request


#conditional statement to check for returned response code

#end of file
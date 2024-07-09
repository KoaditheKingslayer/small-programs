import http.client
import json
conn = http.client.HTTPSConnection("weatherapi-com.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "a3bdbd7ed5msh1ac8bb4c2ce74eap1c990ejsnd035bd0aa18f",
    'X-RapidAPI-Host': "weatherapi-com.p.rapidapi.com"
}

qu = str(input("Please enter a Location, Zip Code, Lat/Long, etc..."))

conn.request("GET", f'/current.json?q={qu}', headers=headers)

res = conn.getresponse()
data = res.read()
parsed = json.loads(data)
output = json.dumps(parsed, indent=2, sort_keys=True)

def print_json(json_data, indent=0):
    if isinstance(json_data, dict):
        for key, value in json_data.items():
            print('  ' * indent + f'{key}')
            print_json(value, indent + 1)
    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            print('  ' * indent + f'{index} \n')
            print_json(item, indent + 1)
    else:
        print('  ' * indent + f'{json_data}\n')


print_json(parsed)

import json
import requests
import csv
import pandas as pd

with open('/Users/vaneezaahmad/Documents/Flatiron/Phase1/ds-east-042621-lectures/Phase_1/ds-apis-nbz32-main/.secrets/creds.json') as f:
    creds = json.load(f)
    
url_params = {
    'term': "Flowers",
    'location': 'Austin+TX',
    'limit': 50,
    'offset': 0
}

filepath = "./businesses.csv"

def api_call(params, key):
    url = 'https://api.yelp.com/v3/businesses/search'
#     term = 'Hamburgers'
    SEARCH_LIMIT = 50
    headers = {
            'Authorization': 'Bearer {}'.format(key),
        }
    
    response = requests.get(url, headers=headers, params=url_params)
    print(response.status_code)
    return response.json()


def parse_results(results):
    parsed_results={}
    parse=[]
    
#     business=json.loads(results)

    for data in results["businesses"]:
        id=data["id"]
        name=data["name"]
#         review_count = data["review_count"]
# #         price = len(data["price"])
#         city=data["location"]["city"]
#         is_closed = data["is_closed"]
        
        parsed_results={"id":id, "name":name, }
        parse.append(parsed_results)
        
    return parse

def df_safe(filepath, parsed):
    
    # your code to open the csv file, concat the current data, and save the data. 
    with open("/Users/vaneezaahmad/Documents/Flatiron/Phase1/Project_Phase1/Phase1_project/businesses.csv", "a") as business:
        if len(parsed)!=0:
            keys = parsed[0].keys()
            writer = csv.DictWriter(business, keys)
            writer.writerows(parsed)
 
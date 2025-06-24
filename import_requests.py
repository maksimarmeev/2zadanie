import requests
import pandas as pd
import os
import time
API_url = 'https://api.golemio.cz/v2/municipallibraries'
API_token = ''
headers = {
    'X-Access-Token': API_token
}
def collect_data(limit = 10000, offset = 0):
    params = {
        'limit':  limit,
        'offset':  offset
    }
    try: 
        response = requests.get(API_url, headers=headers, params=params)
        print("Тип данных:", type(response.json()))
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request API failed {str(e)}")
        raise Exception(f"API Error: {response.status_code} - {response.text}")
def transform_data(data):
    libraries = []
    for feature in data['features']:
        props = feature['properties']
        adress = props.get('address', {})
        opening_hours = []
        for hours in props.get('opening_hours', []):
            if hours.get('is_default', False):
                opening_hours.append(f"{hours['day_of_week']}: {hours['opens']}-{hours['closes']}")
        library = {
            'id': props.get('id'),
            'nazov': props.get('name'),
            'ulica': adress.get('street_address'),
            'psc': adress.get('postal_code'),
            'mesto': adress.get('address_locality'),
            'kraj': props.get('district'),
            'krajina': adress.get('address_country'),
            'sirka': feature['geometry']['coordinates'][1],
            'dlzka': feature['geometry']['coordinates'][0],
            'cas_otvorenia': "; ".join(opening_hours) if opening_hours else None
        }
        libraries.append(library)
    return libraries
data = collect_data()
transformed_data = transform_data(data)
df = pd.DataFrame(transformed_data)
base_dir = os.path.dirname(os.path.abspath(__file__))  
csv_path = os.path.join(base_dir, 'kniznice.csv')
os.makedirs(base_dir, exist_ok=True)
if not df.empty:
    df.to_csv(csv_path, index=False, encoding='utf-8-sig', sep=';')
    print(f"Updated data: {len(df)}")
else:
    print("No data for update")
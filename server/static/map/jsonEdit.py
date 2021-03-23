import json

ob = {
"type": "FeatureCollection",
"features": []
}

with open('geoCountyData.json', 'r', encoding="ISO-8859-1") as json_file:
    data = json.load(json_file)
    for feature in data['features']:
        if feature['properties']['STATE'] == "08":
            ob['features'].append(feature)

# print(ob)

with open('newJsonFile.json', 'w+') as f:
    json.dump(ob, f, indent=2)

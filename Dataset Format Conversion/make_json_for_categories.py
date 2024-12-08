import json

# Level 1
super_categories = ['Drivable', 'Non Drivable', 'Living Things', 'Vehicles', 'Road Side Objects', 'Far Objects', 'Sky']

# Level 4
categories = [
    ['road', 'parking', 'drivable fallback']
    ['sidewalk', 'non-drivable fallback', 'rail track']
    ['person', 'animal', 'rider']
    ['motorcycle', 'bicycle', 'auto rickshaw', 'car', 'truck', 'bus', 'caravan', 'trailer', 'vehicle fallback']
    ['curb', 'wall', 'fence', 'guard rail', 'billboard', 'tradfic sign', 'traffic light', 'pole', 'pole group', 'obs-str-bar fallback']
    ['buuilding', 'bridge', 'tunnel', 'vegetation']
    ['sky', 'fallback background']
]

# Output Format for JSON..

out = {
    "categories" : [

    ]
}

for idx, super_category in enumerate(super_categories) : 
    for category in categories[idx] :

        out["categories"].append({
            "supercategory" : super_category,
            "id" : id,
            "name" : category
        })
        id += 1

# Writing to JSON file..

with open("categories.json", "w") as outfile:
    json.dump(out, outfile)
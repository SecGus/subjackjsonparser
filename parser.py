import json

# Read input from JSON files
with open('data/finger.json', 'r') as file:
    data1 = json.load(file)

with open('data/fingerprints.json', 'r') as file:
    data2 = json.load(file)

with open('data/subjack.json', 'r') as file:
    data3 = json.load(file)

with open('data/myfingerprints.json', 'r') as file:
    data4 = json.load(file)

# Combine the data from all files
all_data = data1 + data2 + data3 + data4

# Create a dictionary to store the unique services and their corresponding cname and fingerprint lists
unique_services = {}

# Iterate over the data list and update the dictionary
for item in all_data:
    service = item["service"]
    cname = item["cname"]
    fingerprint = item["fingerprint"]

    if service in unique_services:
        unique_services[service]["cname"].extend(cname)  # Add unique cname values
        unique_services[service]["fingerprint"].extend(fingerprint)  # Add unique fingerprint values
    else:
        unique_services[service] = {
            "service": service,
            "cname": cname,
            "fingerprint": fingerprint,
            "nxdomain": item["nxdomain"]
        }

# Convert the dictionary values back to a list
result = list(unique_services.values())

# Remove duplicate values from cname and fingerprint arrays
for item in result:
    item["cname"] = list(set(item["cname"]))
    item["fingerprint"] = list(set(item["fingerprint"]))

print(result)

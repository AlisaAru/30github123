import json

# Load the JSON data
file_path = "sample_data.json"
with open(file_path, "r") as file:
    data = json.load(file)

# Extract relevant information
interface_data = []
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    interface_data.append([attributes["dn"], attributes["descr"], attributes["speed"], attributes["mtu"]])

# Print header
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<5}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Print rows
for row in interface_data:
    print("{:<50} {:<15} {:<10} {:<5}".format(row[0], row[1], row[2], row[3]))

print("=" * 80)

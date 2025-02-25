# zip() for Pairwise Iteration and “Unzipping”

names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# Zip them together
zipped = zip(names, scores)
print("Zipped list:", list(zipped))  
# Output might look like: [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Unzip example
zipped_again = list(zip(names, scores))
unzipped_names, unzipped_scores = zip(*zipped_again)

print("Unzipped names:", unzipped_names)    # ('Alice', 'Bob', 'Charlie')
print("Unzipped scores:", unzipped_scores)  # (85, 92, 78)

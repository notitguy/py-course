band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

# print(type(band))
# print(len(band))

#Access values
# print(band["vocals"])
# print(band.get("guitar"))

# List all keys
# print(band.keys())

# List all values
# print(band.values())

# List of key/value pairs as tuples
# print(band.items())

# Check existance
# print("guitar" in band)

# Change values
band["vocals"] = "Coverdale"
# print(band)

# band.update({"bass": "JPJ"})
band["bass"] = "JPJ"
# print(band)

  # remove and return
  # band.pop
  # band.popitem # returns a tuple

# Delete & Clear

band["drums"] = "Bonham"
# del band["drums"]
band2.clear()
# del band2
# print(band2)

# Copy dictionary
# band2 = band #creates reference, no copy
band2 = band.copy()
band2["drums"] = "Dave"
# print(band)
# print(band2)

  # or use dict() constructor function
band3 = dict(band)
# print(band3)

# Nested dictionaries
member1 = {
  "name": "Plant",
  "instrument": "vocals"
}
member2 = {
  "name": "Page",
  "instrument": "guitar"
}
band4 = {
  "member1": member1,
  "member2": member2
}
  # getting values
# print(band4["member1"]["name"])

# SETS

nums = { 1, 2, 3, 4 }
nums2 = set((5,6,7,8))
# print(nums)
# print(nums2)

  # no duplicates allowed
# nums = {1, 2, 2, 3}
# print(nums)
  # True - dupe of 1, False - dupe of 0
# nums = {1, True, 2, False, 3, 4, 0}
# print(nums)

# Merge two sets
one = {1, 2, 3}
two = {2, 3, 4}

three = one.union(two)
# print(three)

# Keep only the duplicates
# print(one & two)
# or
# one.intersection_update(two)
# print(one)

# Keep uniques
print(one ^ two)
# or
one.symmetric_difference_update(two)
print(one)
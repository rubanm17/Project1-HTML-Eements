ms = {1,2,3,4,4,4}
print("Set", ms)

ms.add(5)
print("Updated Set", ms)

set1 = ms
set2 = {2,4,4,6}

print("\nSet1", set1)
print("\nSet2", set2)
print("Difference")
print(set1.difference(set2))
print("Symmetric_difference")
print(set1.symmetric_difference(set2))
def test(st):
    result = {}
    for item in st:
        result[item[0]] = item[1:]
    return result

students = [
    [1, 'Jean Castro', 'V'],
    [2,'Lula Powell','V'],
    [3, 'Brian Howell','VI'],
    [4,'Lynne Foster','VI'],
    [5,'Zachary Simon','VII']
]
print("\nOriginal list of lists:")
print(students)
print("\nConverted list to a dictionary:")
print(test(students))
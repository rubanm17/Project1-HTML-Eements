st = ['Apple','Guava','Mango','banana','kiwi']

print("length of the list: ", len(st))
print("FIrst element:", st[0])
print("Last element:", st[-1])

st.append('Papaya')
print("Update list", st)

st.remove('Guava')
print("Update list", st)

st.sort()
print("Sorted list", st)

st.pop(1)
print("Updated list", st)

st.reverse()
print("Reversed list", st)

print("Multiplication on List:",  st*2)

st = st[:4]
print("Sliced  list", st)

st.clear()
print("Updated list:", st)
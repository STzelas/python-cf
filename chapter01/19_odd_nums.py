print("Java style")
for i in range(22):
  if(i % 2 != 0):
    print(i, end=" ")
print()

print("Python style")
for i in range(1, 22, 2): # start = 1, stop = 22 (γιατί θέλουμε μέχρι το 21), step = 2 (πηδήματα άνα 2 θέλουμε περιτούς)
    print(i, end=" ")
print() 
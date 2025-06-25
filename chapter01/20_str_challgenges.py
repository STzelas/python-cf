# Challenge No1
# F
# aa
# ccc
# tttt
# ooooo
# rrrrrr
# yyyyyyy

# (Factory)

message1 = "Factory"
for i in range(len(message1)):
  print(message1[i] * (i + 1))

message2 = "Coding"
for i in range(len(message1)):
  print(message1[i] * (i + 1))


# Challenge No2
# F******
# aa*****
# ccc****
# tttt***
# ooooo**
# rrrrrr*
# yyyyyyy

for i in range(len(message1)):
  print(message1[i] * ( i + 1), end="*" * (len(message1) - i - 1))
  print()

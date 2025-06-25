s = "Coding Factory"

s1 = s[7] # F
print(s1)

# Slice γίνεται με  
# Εδώ του λέω πάνε απο την αρχή μέχρι το τέλος - ':'
# Μπορώ και :: (start:stop:end) / ίδια λογική με range
s2 = s[::]   
print(s2)

# Ξεκινάει απο την θέση s[7] μέχρι τέλος - Factory
s3 = s[7:]
print(s3)

# Ξεκινάει απο το τέλος του str
s4 = s[-1]  # y
print(s4)

s5 = s[:-2] # Inclusive το 1ο, exclusive το 2ο
print(s5)

s6 = s[7:-1]
print(s6)

s7 = s[7:7]
print(s7)

# s = "Coding Factory"
# for i in range(len(s)):
#   print(s[-i -1], end="")

# Οταν έχουμε αρνητικά indexes το 
# default start είναι το -1 (που είναι και inclusive)
# To stop είναι το -len() -1
s8 = s[::-1] 
print(s8)



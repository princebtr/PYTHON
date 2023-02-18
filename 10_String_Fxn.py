''' Use of string function to find double space and correct this mistake'''
a = "a  crazy fox jumps  over a lazy  dog"
print(a.count("  "))
b = a.replace("  "," ")
print(b)
print(b.count("  "))

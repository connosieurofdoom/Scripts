import random, string
# + "~"+ "^"+ "+"+ "_"+ "-"+ "{"+ "}"+ "|"+ "."+ "["+ "]"+ "?"+ "/"
x = ''.join(random.choices(string.ascii_letters + string.digits , k=15))
print(x)

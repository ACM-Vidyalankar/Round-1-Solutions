S = input()
E = 0 
for i in S:
  if(i.isalpha() or i.isspace() or i.isnumeric()):
    continue
  E += 1
print(E)
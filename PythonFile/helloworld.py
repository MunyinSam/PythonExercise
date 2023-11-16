if (myInput>=80 && myInput<=100):
    print("A")
elif (myInput>=70 && myInput<=79):
    print("B")
elif (myInput>=60 && myInput<=69):
    print("C")
elif (myInput>=50 && myInput<=59):
    print("D")
elif (myInput<50):
    print("F")

    lines = []

for i in range(2):
  myInput = input()
  lines.append(myInput + '\n')
  
       

A = lines[0]
B = lines[1]
A = int(A)
B = int(B)
a = lines[0]
b = lines[1]
divide = int(A/B)

print(a + "+" + b + "= " + str(A+B))

print(a + "-" + b + "= " + str(A-B))

print(a + "*" + b + "= " + str(A*B))
if (B != 0):
  print(a + "/" + b + "= " + str(divide))
else:
  print("")
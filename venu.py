import array as arr
ary1=arr.array('i',[1,2,3,4,5,6,7,8,9])
ary2=arr.array('d',[1,2,5,6,7,3,5,2,8,9,1])
print("elements of first array are:")
for i in range(len(ary1)):
      print(ary1[i])
print("elements of second array are:")
for i in range(len(ary2)):
      print(ary2[i])
print("insertion")
ary1.insert(0,10)
print("updated array is",ary1)
print("removal")
ary1.remove(10)
print("updated array is",ary1)
ary1.pop(8)
print("updated array is",ary1)
print("slicing oparation")
print[:len(ary1)]
print(ary1[-1:])
print(ary1[2:1])
print(ary1[2:8])
print(ary2[:])
print(ary2[::-1])

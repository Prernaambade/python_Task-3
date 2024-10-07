# List Methods
# 1.Append
fruits = ['apple','banana','cherry']
fruits.append("orange")
print(f'fruits{fruits}')

# 2.Clear
fruits = ['apple','banana','cherry']
fruits.clear()
print(f'fruits{fruits}')

#3.Count
fruits = ['apple','banana','cherry']
count_cherry=fruits.count('cherry')
print(f'number of cherries:{count_cherry}') 

#4.copy
fruits = ['apple','banana','cherry']
x=fruits.copy()
print(f'fruits{fruits}')

#5.Extend
fruits = ['apple','banana','cherry']
cars=['ford','BMW','Volvo']
fruits.extend(cars)
print(f'fruits{fruits}')

#6.index
fruits = ['apple','banana','cherry']
x=fruits.index("cherry")
print(f'fruits{fruits}')

#7.insert
fruits = ['apple','banana','cherry']
fruits.insert(1,"orange")
print(f'fruits{fruits}')

#8.pop
fruits = ['apple','banana','cherry']
fruits.pop(1)
print(f'fruits{fruits}')

#9.Remove
fruits = ['apple','banana','cherry']
fruits.remove("banana")
print(f'fruits{fruits}')

#10.Reverse
fruits = ['apple','banana','cherry']
fruits.reverse()
print(f'fruits{fruits}')

#11.Sort
cars=['Ford','BMW','Volvo']
cars.sort()
print(f'cars{cars}')

#12.Fromkeys
x=('key1','key2','key3')
y=0
thisdict=dict.fromkeys(x,y)
print(f'thisdict{thisdict}')

#13.Get
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.get("model")
print(x)

#14.items
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.items()
print(x)

#15.Keys
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.keys()
print(x)

#16.Popitem
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.popitem()
print(x)

#17.setdefault
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.setdefault("model","Bronco")
print(x)

#18.update
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
car.update({"color":"white"})
print(car)

#19.values
car={
    "brand":"Ford",
    "model":"Mustang",
    "year" : 1986
}
x=car.values()
print(x)

#20.Add
fruits = {'apple','banana','cherry'}
fruits.add("orange")
print(fruits)

#21.difference
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
z= x.difference(y)
print(z)

#21.difference_update
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
x.difference_update(y)
print(x)

#22.discard
fruits= {'apple','banana','cherry'}
fruits.discard("banana")
print(fruits)

#23.Intersection
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
z=x.intersection(y)
print(z)

#24.Intersection_update
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
x.intersection_update(y)
print(z)

#25.Isdisjoint
x= {'apple','banana','cherry'}
y={"google","microsoft","facebook"}
z=x.isdisjoint(y)
print(z)

#26.issubset
x={"a","b","c"}
y={"f","e","d","c","b","a"}
z=x.issubset(y)
print(z)

#27.issuperset
x={"f","e","d","c","b","a"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)

#28.symmetric_difference
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
z=x.symmetric_difference(y)
print(z)

#29.Union
x= {'apple','banana','cherry'}
y={"google","microsoft","apple"}
z= x.union(y)
print(z)

#30.close
f= open("demofile.txt","r")
print(f.read())
f.close()





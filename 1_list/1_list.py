thislist=['apple','banana','grapes']
print(thislist)
thistuple=('apple','banana','grapes')
print(thistuple)
thisdict={
    "brand":"BMW",
    "name":"M8 Grand Coupe",
    "year":2023
}
print(thisdict)
thislist.append('mango')
thislist.insert(1,"dragon fruit")
thislist.extend(["orange","strawberry"])
print(thislist)
thislist.pop()
print(thislist)


thisdict.pop("year")
print(thisdict)
dict2 = thisdict.copy()
dict2.update({"fuel": "petrol"})
print(dict2)

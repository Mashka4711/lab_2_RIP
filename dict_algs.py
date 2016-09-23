ivan ={
    "name" : "ivan",
    "age": 34,
    "children": [{
        "name" :"vasja",
        "age" : 12,
    },{
        "name" : "petja",
        "age" : 10,
    }],
}

darja = {
    "name" : "darja",
    "age" : 41,
    "children": [{
        "name" : "kirill",
        "age" : 21,
    },{
        "name" : "pavel",
        "age" : 15,
    }],
}

emps = [ivan, darja]

def func_18(emps):
    boole=0
    for p in emps:
        for c in p.get('children'):
            if c.get("age")>14:
                boole=1
                break
        if boole==1:
          print(p.get("name"))
          boole=0


func_18(emps)
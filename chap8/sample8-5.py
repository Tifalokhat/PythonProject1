def fun(*para):
    print(type(para))
    for item in para:
        print(item)

fun(10,20,30,40)
fun(10)
fun(20,30)
fun([11,22,33,44])
fun(*[11,22,33,44])

def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,'----',value)

fun2(name='娟子姐',age=18,height=170)

d={'name':'娟子姐','age':18,'height':170}

fun2(**d)
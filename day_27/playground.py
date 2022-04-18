def add(*args):
    sum = 0
    for number in args:
        sum +=number
    print(sum)

add(1,2,1,5,3,6,5,8,9,5,2,3,65,5,5,56)

def calculate(**kwargs):
    sum = 0;
    #Option one loop through
    # for key,value in kwargs.items():
    #     if(key =="add"):
    #         sum +=kwargs["add"]
    #     elif key=="multiply":
    #         sum*=kwargs[key]
    #     elif key=="substract":
    #         sum-=kwargs[key]
    #     elif key=="divide":
    #         sum/=kwargs[key]
    #     else:
    #         continue
    # sum+=kwargs["add"]
    # sum-=kwargs["subtract"]
    # sum*=kwargs["multiply"]
    # sum/=kwargs["divide"]
    #if key is not specify will crash
    #use get instead
    sum += kwargs.get("add") or 0
    sum -= kwargs.get("subtract") or 0
    sum *= kwargs.get("multiply") or 1
    sum /= kwargs.get("divide") or 1
    print(sum)

calculate(add=3,multiply=10)
a={"abc":10,"abc1":11 ,"abc2":12}
print(a)
print(a["abc"])

key_value=10
b=a.items()
print("a.items():",b)
for key, value in a.items():
    if value==key_value:
        print(f"Key corresponding to value {key_value}: {key}")
        break
    else:
        print(f"Value {key_value} not found in the dictionary")

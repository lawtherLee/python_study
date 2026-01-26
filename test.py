a = 10
b = a

print(f"id:{id(a)}")
print(f"id:{id(b)}")

b = 20
print(a)
print(f"id:{id(a)}")
print(f"id:{id(b)}")

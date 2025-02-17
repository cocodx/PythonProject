from ctypes import HRESULT

# basic operators

friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 5
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2   迷的几次方
# friends **= 2

reminder = friends % 2

print(friends)
print(reminder)

x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
result = min(x, y, z)
print(result)

a = ['corona', 1, 1.2]
b = a.copy()
a.append("hello world")
a.remove("corona")
a.pop(1)
# a.insert
b.extend(a)
b.insert(1,"delta")

print(b, 'without reverse')
b.reverse()
print(b,"reverse")

a = [1,2,3,4,2,1,3,4,5,6,4,3]
a.sort()
print(a)

a = [1,2,3,4,2,1,3,4,5,6,4,3]
a.sort(reverse=True)
print(a)
# DemoLoop.py

value=5
while value > 0:
    print(value)
    value -= 1

lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i)

color = {"apple":100, "kiwi":200, "banana":300}
for item in color.keys():
    print(item)

for item in color.values():
    print(item)

print("====구구단 출력====")
for x in [2, 3, 4, 5, 6]:
    print("===={0}단====".format(x))
    for y in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

print("====break===")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    #추가 탈출조건
    if i > 5:
        break
    print(i)

for x in [20, 18, 16, 14, 12, 10, 8, 6, 4, 2, 1]:
        print("♥"*x)

print("====contine===")
lst = [1,2,3,4,5,6,7,8,9,10]
for x in lst:
    #추가 탈출조건
    if x % 2 == 0:
        continue
    print(x)

print("====수열====")
print(list(range(10)))
print(list(range(2000,2023)))
print(list(range(1,101)))

print("===리스트 컴프리헨션===")
lst = list(range(1,11))
print([x**2 for x in lst if x>5])
tp=("apple", "kiwi", "banana")
print([len(x) for x in tp])

print("====필터링하는 경우===")
lst = [10, 25, 30]
interL = filter(None, lst)
for item in interL:
    print(item)





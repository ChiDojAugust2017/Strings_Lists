words = "It's thanksgiving day. It's my birthday,too!"



index_position = words.find("day")
print (index_position)

yeah = words.replace ("day", "month")
print yeah


x = [2,54,-2,7,12,98]

print(min(x))
print(max(x))

x = ["hello",2,54,-2,7,12,98,"world"]
x.sort()
print x[6:]

first = "hello"
last = "world"
new_list = first + " , " + last
print new_list


y = [19,2,54,-2,7,12,98,32,10,-3,6]

y.sort()

#z = []
#q = []
#p = y[:6]
#s = y[6:]
#z.append(p)
#q.append(s)


#print y

#print z
#print q
list_a = y[:len(y)/2]
list_b = y[len(y)/2:]
list_c = [list_a]
for item in list_b:
    list_c.append(item)
print list_c











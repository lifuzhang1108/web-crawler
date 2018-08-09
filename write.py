import time
input="""

"""
input=input.split("---------------------------------")
for i in range(0,len(input)):
    input[i]=input[i].splitlines()

def rem(the_list, val):
    while val in the_list:
        the_list.remove(val)

for i in range(0,len(input)):
    rem(input[i],"")
    rem(input[i], "ERROR")
    rem(input[i], "Timeout")
    input[i].reverse()
rem(input,[])

for i in input:
    print
    for j in i:
        print(j,end="|")
    print("\n")


filename="info"+str(time.ctime())
with open(filename,'w') as f: # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
    for i in input:
        f.write("|")
        for j in i:
            str=j+"|"
            f.write(str)
        f.write("\n")
print(filename)
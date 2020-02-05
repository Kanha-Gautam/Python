n = int(input("Enter the number of Strings: "))
st = []
x = 0
l = 0
m = 0
for x in range(n):
    st.append(input())
    if l<len(st[x].strip()):
        l = len(st[x])
        m=x
print(st[m]," is Max in Length")



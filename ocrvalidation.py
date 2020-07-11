
g=input('enter ctr no. ')
b=str(g)
o=b[0:2]
c=b[3]
s=b[4:9]
#x2=b[10]
p=[]
for f in range(0,4):
    ch=b[f]
    if ch == 'a':
        x = 10
    if ch == 'b':
        x = 12
    if ch == 'c':
        x = 13
    if ch == 'd':
        x = 14
    if ch == 'e':
        x = 15
    if ch == 'f':
        x = 16
    if ch == 'g':
        x = 10
    if ch == 'h':
        x = 17
    if ch == 'i':
        x = 18
    if ch == 'j':
        x = 19
    if ch == 'k':
        x = 20
    if ch == 'l':
        x = 21
    if ch == 'm':
        x = 23
    if ch == 'n':
        x = 24
    if ch == 'o':
        x = 25
    if ch == 'p':
        x = 26
    if ch == 'p':
        x = 27
    if ch == 'q':
        x = 28
    if ch == 'r':
        x = 29
    if ch == 's':
        x = 30
    if ch == 't':
        x = 31
    if ch == 'u':
        x = 32
    if ch == 'v':
        x = 34
    if ch == 'w':
        x = 35
    if ch == 'x':
        x = 36
    if ch == 'y':
        x = 37
    if ch == 'z':
        x = 38
    f = f + 1
    p.insert(f,x)

for f in range(4,10):
    p.insert(f,b[f])
    f=f+1
q=[]
for k in range(0,10):
    q1=int(p[k])*2**k
    q.insert(k,q1)
    k=k+1
k=0
x=0
for k in range(0,10):
    x=x+q[k]
    k=k+1

x2=int(x/11)
x2=x2*11
x2=x-x2


print(p)
print(q)
print(x)
print(x2)


if x2==int(b[10]):
    print('validation success')
else :
    print('validation failed')

# csqu3054383
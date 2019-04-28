import math

vx = 3 # m/s
ax = 0.5 # m/s²

vy = 0.5 # m/s
ay = 0.5 # m/s²

vz1 = 1# m/s
az1 = 1# m/s²  空载伸叉

vz2 = 0.75# m/s
az2 = 0.5# m/s²  满载伸叉

x0 = 0 # m
y0 = 0.65 # m

x1 = 0.85 # m
y1 = 0.55 # m

h = 0.07  #微升
vh = 1/6
ah = 0.6

tt0 =2.5 #响应时间

x9 = 0;
y9 = 0;

d = 0.93 # m





k = 10 #层
m = 34 #列

hk = 0.35 #层间距
hm = 0.67 #列间距


def f2(s,v,a):

    if s <= (v*v/a):
        t = math.sqrt(4*s/a)
    else:
        t=2*v/a+(s-v*v/a)/v
    return t


print('********case1*单循环*******')

t1 = []

for i in range(m):
    for j in range(k):
        t1.append(max(f2((x1+hm*i),vx,ax),f2(abs(y1+hk*j-y0),vy,ay)))

t0 = f2(d,vz1,az1)+f2(d,vz2,az2)+f2(h,vh,ah)+tt0

t1_final = 2*sum(t1)/len(t1)+2*t0
n1 = 3600/t1_final*0.85

print('n1==',n1,'len(t1)=',len(t1))

print('********case1*单循环*******')

print('********case1复合循环*******')


t11=[]

for i1 in range(m):
    for j1 in range(k):
        for i2 in range(m):
            for j2 in range(k):
                if i1==i2 and j1==j2:continue;
                t11.append(max(f2((x1+hm*i1),vx,ax),f2(abs(y1+hk*j1-y0),vy,ay))+
                           max(f2((x1+hm*i2),vx,ax),f2(abs(y1+hk*j2-y0),vy,ay))+
                           max(f2(hm*abs(i2-i1),vx,ax),f2(hk*abs(j2-j1),vy,ay)))
                               
t11_final = sum(t11)/len(t11)+4*t0
n11 = 3600/t11_final*0.85*2                

print('n11=',n11,'len(t11)=',len(t11))

print('********case1复合循环*******')


print('********case2 复合循环 vvvv*********')
x9 = 23.3
y9 = 0.65
t22=[]
for i1 in range(m):
    for j1 in range(k):
        for i2 in range(m):
            for j2 in range(k):
                if i1==i2 and j1==j2:continue;
                t22.append(max(f2((x1+hm*i1),vx,ax),f2(abs(y1+hk*j1-y0),vy,ay))+
                           max(f2(hm*abs(i2-i1),vx,ax),f2(hk*abs(j2-j1),vy,ay))+
                           max(f2(abs(x1+hm*i1-x9),vx,ax),f2(abs(y1+hk*j1-y9),vy,ay))+
                           f2((x9-x0),vx,ax))

t22_final = sum(t22)/len(t22)+4*t0
n22 = 3600/t22_final*0.85*2
print('n22=',n22,'len(t22)=',len(t22))

print('********case2 复合循环 vvvv*********')

















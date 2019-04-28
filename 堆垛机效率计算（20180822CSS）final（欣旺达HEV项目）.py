import math

vx = 3 # m/s
ax = 0.5 # m/s²

vy = 0.5 # m/s
ay = 0.5 # m/s²

L = 50 # m
H = 1.8 # m

#入分容 H：0→2m；L：0→4m
L1 = 4 # m
H1 = 2 # m


#入静置1 ：H：0→2m；L：0→4m；
#          H：0→1.8m；L：0→50m；
#          H：0→1.8m；L：0→50m；
H2 = 1.8
L2 = 50

y0 = 3 # m
x0 = L/2 # m
t0 = 8.7 # s

case = 2

n=0.85


def f2(s,v,a):

    if s <= (v*v/a):
        t = math.sqrt(4*s/a)
    else:
        t=2*v/a+(s-v*v/a)/v
    return t
#入分容
tt11 = max(f2(L1,vx,ax),f2(H1,vy,ay));
tt1 = 2*tt11+2*t0;
print('tt1=',tt1)

#分容入静置
tt21 = max(f2(1/5*L2,vx,ax),f2(2/3*H2,vy,ay))
tt22 = max(f2(2/3*L2,vx,ax),f2(1/5*H2,vy,ay))

tt2 = tt11 + tt21 + tt22 + 2*t0

print('tt2',tt2)

#出静置1；
H3 = 1.8
L3 = 50

tt311 = max(f2(1/5*L3,vx,ax),f2(2/3*H3,vy,ay))+max(f2(4/5*L3,vx,ax),f2(2/3*H3,vy,ay));
tt312 = max(f2(2/3*L,vx,ax),f2(1/5*H,vy,ay)) + max(f2(1/3*L,vx,ax),f2(1/5*H,vy,ay));
#跑全程
tt32 = max(f2(L,vx,ax),f2(0*H,vy,ay))

tt3 = (tt311+tt312)/2+2*t0

print('tt3',tt3)

#出静置1：
tt411 = max(f2(1/5*L3,vx,ax),f2(2/3*H3,vy,ay));
tt412 = max(f2(2/3*L,vx,ax),f2(1/5*H,vy,ay));

tt4 = tt411 + tt412 +2*t0
print('tt4',tt4)

#空盘回流：
tt0 = tt32+2*t0
print('tt0',tt0)


# case 1

if case ==1:
    t1= max(f2(1/5*L,vx,ax),f2(2/3*H,vy,ay))
    t2= max(f2(2/3*L,vx,ax),f2(1/5*H,vy,ay))

    t3= max(f2((2/3-1/5)*L,vx,ax),f2((2/3-1/5)*H,vy,ay))

    t = (t1+t2)+2*t0

    ta2 = t1 + t3 + t2 + 4*t0

    print('case=',case,'\n','%.1f' % t1,'\n','%.1f'% t2,'\n','t=','%.1f'% t,'\n','ta=','%.1f'% ta2)

# case 2

if case ==2:
    t21 = max(f2(1/5*L,vx,ax),f2(2/3*H,vy,ay))
    t22 = max(f2((2/3-1/5)*L,vx,ax),f2((2/3-1/5)*H,vy,ay))
    t23 = max(f2((1-2/3)*L,vx,ax),f2((1/5)*H,vy,ay))

    t24 = max(f2((1-1/5)*L,vx,ax),f2(2/3*H,vy,ay))
    t25 = max(f2((2/3-1/5)*L,vx,ax),f2((2/3-1/5)*H,vy,ay))
    t26 = max(f2((2/3)*L,vx,ax),f2((1/5)*H,vy,ay))

    t27 = max(f2((1)*L,vx,ax),f2((0)*H,vy,ay))

    ta21 = (t21+t22+t23+t24+t25+t26+2*t27)/2+4*t0

    print('case=',case,'\n',t21,'\n',t22,'\n',t23,'\n',t24,'\n',t25,'\n',t26,'\n',t27,'\n',ta21)

# case 3
if case ==3:
    t31 = max(f2(1/5*L,vx,ax),f2((1-1/3)*y0,vy,ay))
    t32 = max(f2(2/3*L,vx,ax),f2(abs(1/3*y0+7*H/15-y0),vy,ay))

    t33 = max(f2((2/3-1/5)*L,vx,ax),f2((7*H/15),vy,ay))

    ta31 = t31+t32+2*t0
    ta32 = t31 + t32 + t33 +4*t0

    print ('case=',case,'\n',t31,'\n',t32,'\n',t33,'\n',ta31,'\n',ta32)
    
#case 4
if case ==4:
    t41 = max(f2(abs(1/5*L+1/3*x0-x0),vx,ax),f2((2/3)*H,vy,ay))
    t42 = max(f2(abs(2/3*L+1/3*x0-x0),vx,ax),f2((1/5)*H,vy,ay))

    t43 = max(f2(abs(2/3*L-1/5*L),vx,ax),f2((2/3-1/5)*H,vy,ay))

    ta1 = t41 +t42 + 2*t0
    ta2 = t41 + t42 + t43 + 4*t0

    print('case=',case,'\n',t41,'\n',t42,'\n',t43,'\n',ta1,'\n',ta2)

#case 5
if case ==5:
    t51 = max(f2(abs(1/5*L),vx,ax),f2(((2/3)*H+1/6*y0),vy,ay))
    t52 = max(f2(abs(2/3*L),vx,ax),f2(((1/5)*H+1/6*y0),vy,ay))

    ta51 = t51+t52+2*t0

    t53 = max(f2(abs(1/5*L),vx,ax),f2(abs((2/3)*H+1/6*y0-y0),vy,ay))
    t54 = max(f2(abs(2/3*L),vx,ax),f2(abs((1/5)*H+1/6*y0-y0),vy,ay))

    ta52 = t53 + t54 + 2*t0

    t55 = max(f2(abs(2/3*L-1/5*L),vx,ax),f2(abs(2/3*H-1/5*H),vy,ay))
    t56 = max(f2(abs(2/3*L),vx,ax),f2(abs(1/5*H+1/6*y0-y0),vy,ay))
    t57 = max(f2(0,vx,ax),f2(abs(y0),vy,ay))

    ta53 = t51+t55 + t56 +t57 + 4*t0

    ta54 = t52 + t55 + t53 +t57 +4*t0

    print('case=',case,'\n',t51,'\n',t52,'\n',t53,'\n',t54,'\n',t55,'\n',t56,'\n',t57,'\n',ta51,'\n',ta52,'\n',ta53,'\n',ta54)


#case 6
if case ==6:
#入
    t61 = max(f2(abs(1/5*L),vx,ax),f2(abs((2/3)*H+1/6*y0-y0),vy,ay))
    t62 = max(f2(abs(2/3*L),vx,ax),f2(abs((1/5)*H+1/6*y0-y0),vy,ay))

    ta61 = t61 + t62 + 2*t0

#出
    t63 = max(f2(abs(1/5*L),vx,ax),f2(((2/3)*H+1/6*y0),vy,ay))
    t64 = max(f2(abs(2/3*L),vx,ax),f2(((1/5)*H+1/6*y0),vy,ay))

    ta62 = t63+t64+2*t0

#中间
    t65 = max(f2(abs(2/3*L-1/5*L),vx,ax),f2(abs(2/3*H-1/5*H),vy,ay))
    t66 = max(f2(0,vx,ax),f2(abs(y0),vy,ay))

#复合
    ta63 = t61 + t65 + t64 +t66 +4*t0

#输出
    print('case=',case,'\n',t61,'\n',t62,'\n',t63,'\n',t64,'\n',t65,'\n',t66,'\n',ta61,'\n',ta62,'\n',ta63)



yy = range(0,265,6)
xx = range(0,L+1,1)

tt = []

for i in yy:
    for j in xx:
        tt.append(max(f2(j,vx,ax),f2(i/10,vy,ay)))

#print(sum(tt)/len(tt)*2+2*t0,len(tt))

#print('tt1=',tt1)
















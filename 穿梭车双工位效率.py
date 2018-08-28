import math

s=1.5;
v1=0.2;
a1=0.5;

L1=0;
L2=[0,5,10,15,20,25,30,35,40,45]
v2=3;
a2=0.5;

n=0.85

L3=[abs(i-L1) for i in L2]

def f1(a):
    b=[]
    for i in a:
        for j in a:
            if i==j:
                continue
            b.append(abs(i-j));
    return b

def f2(s,v,a):

    if s <= (v*v/a):
        t = math.sqrt(4*s/a)
    else:
        t=2*v/a+(s-v*v/a)/v
    return t


t_all_a = [f2(i,v2,a2) for i in L3]
t_ave_a = sum(t_all_a)/len(t_all_a)

t_ave_b = f2(s,v1,a1)


#L_all_c = [f1(L2) for i in L2]



t_all_c = [f2(i,v2,a2) for i in f1(L2)]
t_ave_c = sum(t_all_c)/len(t_all_c)

t_all = 2*t_ave_a + 3*t_ave_b + t_ave_c

t_all2 = 2*t_ave_a + 2*t_ave_b

t_all3 = 2*t_ave_a + 4*t_ave_b + t_ave_c+f2(1.5,v2,a2)

#print(t_ave_a,t_ave_b,t_ave_c,t_all)

pp = 2*3600*0.85/t_all

pp2 = 3600*0.85/t_all2

pp3 = 2*3600*0.85/t_all3

print('双工位效率= %.1f' % pp)

print('单工位效率= %.1f' % pp2)

print('双工位两次叉取效率= %.1f' % pp3)

print('双工位相比于单工位效率提升%.2f' % (pp/pp2))

print('双工位两次叉取相比于单工位效率提升%.2f' % (pp3/pp2))
#print(L3)
#print(t_all_c)
#print(max(f1(L2)))




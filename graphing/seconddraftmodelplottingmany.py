import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

#constants/other functions
p1=1.25
p2=0.285
mu1=0.1
b=0.0011
mu2=0.41
alpha=0.52
p4=0.12
B=0.011
delta=1/B
d=1
def p5(t):
    return 0.003
p3=1.1
r=0.032
b=0
#CHANGE THIS WHEN CORRECT VALUE IS FOUND:
c=1

def system(t, y):
    x1, x2, x3, x4 = y
    dx1 =-p1*x2*x1-p2*x1*x4-mu1*x1+b
    dx2 = -mu2*x2+alpha*x3+p4*x2*x1-p5(t)*x2*x3
    dx3 = p2*x1*x4-p3*x3*x2
    dx4 = -p2*x1*x4+x4*(b-c*np.log(x4/delta))
    return [dx1, dx2, dx3, dx4]

t_span = (0, 80)
t_eval = np.linspace(*t_span, 2000)
y0s=[]
poss=[0,0.5,1]
for i in poss:
    for j in poss:
        for k in poss:
            for l in [0.5,1]:
                y0s.append([i,j,k,l])
print("calculating...")
sol=[]
for i in y0s:
    sol.append(solve_ivp(system, t_span, i, t_eval=t_eval, rtol=1e-8))
print('done')
fig, axes = plt.subplots(ncols=3,nrows=2, figsize=(15, 7))
for i in range(len(sol)):
    axes[0,0].scatter(y0s[i][0],y0s[i][1])
    axes[0,0].scatter(sol[i].y[0][-1],sol[i].y[1][-1],s=100)
    axes[0,0].plot(sol[i].y[0], sol[i].y[1])     
axes[0,0].set_xlabel('B'); axes[0,0].set_ylabel('E'); axes[0,0].set_title('Slice (B, E)')


for i in range(len(sol)):
    axes[0,1].scatter(y0s[i][0],y0s[i][2])
    axes[0,1].scatter(sol[i].y[0][-1],sol[i].y[2][-1],s=100)
    axes[0,1].plot(sol[i].y[0], sol[i].y[2])       
axes[0,1].set_xlabel('B'); axes[0,1].set_ylabel('T_i'); axes[0,1].set_title('Slice (B, T_i)')


for i in range(len(sol)):
    axes[0,2].scatter(y0s[i][0],y0s[i][3])
    axes[0,2].scatter(sol[i].y[0][-1],sol[i].y[3][-1],s=100)
    axes[0,2].plot(sol[i].y[0], sol[i].y[3])         
axes[0,2].set_xlabel('B'); axes[0,2].set_ylabel('T_u'); axes[0,2].set_title('Slice (B, T_u)')

for i in range(len(sol)):
    axes[1,0].scatter(y0s[i][1],y0s[i][2])
    axes[1,0].scatter(sol[i].y[1][-1],sol[i].y[2][-1],s=100)
    axes[1,0].plot(sol[i].y[1], sol[i].y[2])        
axes[1,0].set_xlabel('E'); axes[1,0].set_ylabel('T_i'); axes[1,0].set_title('Slice (E, T_i)')

for i in range(len(sol)):
    axes[1,1].scatter(y0s[i][1],y0s[i][3])
    axes[1,1].scatter(sol[i].y[1][-1],sol[i].y[3][-1],s=100)
    axes[1,1].plot(sol[i].y[1], sol[i].y[3])     
axes[1,1].set_xlabel('E'); axes[1,1].set_ylabel('T_u'); axes[1,1].set_title('Slice (E, T_u)')

for i in range(len(sol)):
    axes[1,2].scatter(y0s[i][2],y0s[i][3])
    axes[1,2].scatter(sol[i].y[2][-1],sol[i].y[3][-1],s=100)
    axes[1,2].plot(sol[i].y[2], sol[i].y[3])     
axes[1,2].set_xlabel('T_i'); axes[1,2].set_ylabel('T_u'); axes[1,2].set_title('Slice (T_i, T_u)')

plt.tight_layout(); 
plt.savefig("seconddraftmanyfig.png")
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
b=0
def p5(t):
    return 0.003
p3=1.1
r=0.032
c=r

def system(t, y):
    x1, x2, x3, x4 = y
    dx1 =-p1*x2*x1-p2*x1*x4-mu1*x1+b
    dx2 = -mu2*x2+alpha*x3+p4*x2*x1-p5(t)*x2*x3
    dx3 = p2*x1*x4-p3*x3*x2
    dx4 = delta*(np.exp(-d*np.exp(-c*t)))-p2*x1*x4
    return [dx1, dx2, dx3, dx4]

t_span = (0, 60)
t_eval = np.linspace(*t_span, 1000)
y0 = [.1, .1, .1, .1]
print("here1")
sol = solve_ivp(system, t_span, y0, t_eval=t_eval, rtol=1e-8)
print('here2')
fig, axes = plt.subplots(ncols=3,nrows=2, figsize=(15, 7))
axes[0,0].scatter(y0[0],y0[1])
axes[0,0].plot(sol.y[0], sol.y[1])     
axes[0,0].set_xlabel('B'); axes[0,0].set_ylabel('E'); axes[0,0].set_title('Slice (B, E)')

axes[0,1].scatter(y0[0],y0[2])
axes[0,1].plot(sol.y[0], sol.y[2])      
axes[0,1].set_xlabel('B'); axes[0,1].set_ylabel('T_i'); axes[0,1].set_title('Slice (B, T_i)')

axes[0,2].scatter(y0[0],y0[3])
axes[0,2].plot(sol.y[0], sol.y[3])     
axes[0,2].set_xlabel('B'); axes[0,2].set_ylabel('T_u'); axes[0,2].set_title('Slice (B, T_u)')

axes[1,0].scatter(y0[1],y0[2])
axes[1,0].plot(sol.y[1], sol.y[2])       
axes[1,0].set_xlabel('E'); axes[1,0].set_ylabel('T_i'); axes[1,0].set_title('Slice (E, T_i)')

axes[1,1].scatter(y0[1],y0[3])
axes[1,1].plot(sol.y[1], sol.y[3])       
axes[1,1].set_xlabel('E'); axes[1,1].set_ylabel('T_u'); axes[1,1].set_title('Slice (E, T_u)')

axes[1,2].scatter(y0[2],y0[3])
axes[1,2].plot(sol.y[2], sol.y[3])       
axes[1,2].set_xlabel('T_i'); axes[1,2].set_ylabel('T_u'); axes[1,2].set_title('Slice (T_i, T_u)')

plt.tight_layout(); 
plt.savefig("firstdraftfig.png")
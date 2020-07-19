##############################################################################################
# plot of Temperature, Heat Capacity, Magnetization and Magnetic susceptibility of Ising model
# Arya Gholampour
##############################################################################################


import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

T = .1
B = 0
N = 10
dT = 5 / 50
cv_list = np.ones([20,50])
chi_list = np.zeros([20,50])
e_list = np.zeros([20,50])
M_list = np.zeros([20,50])

n1 = 1.0 / (10000*N*N)
n2 = 1.0 / (10000*N*N)

for i in tqdm(range(10)):
    T = .1
    for j in range(50):
        m1 = 0
        m2 = 0
        e = 0
        e2 = 0
        s = np.ones((N,N))
        for _ in range(1000):
            x = np.random.randint(N)
            y = np.random.randint(N)
            new_s = s[x,y]
            H = 2*(s[(x-1)%N,y%N] + s[(x+1)%N,y%N] + s[x%N,(y-1)%N] + s[x%N,(y+1)%N] + B)*new_s
            if H < 0 or np.random.rand() < np.exp(-H / T):
                s[x,y] = -new_s
            e += -H/(8)
            e2 += e**2
            m1 += np.sum(s)
        cv_list[i,j] = (n1*e2-n2*e**2)*(T**2)/2000000
        chi_list[i,j] = (1 - np.mean(s)**2)/T
        e_list[i,j] = (e/20000)
        M_list[i,j] = (m1/200000)
        T += dT

fig, axs = plt.subplots(2, 2, constrained_layout=True)
x = np.linspace(0.1,5,50)
axs[0,1].plot(x,np.mean(e_list, axis=0),'.')
axs[0,1].set_title('Mean Energy')
axs[0,1].set_xlabel('Temperature')
axs[0,1].set_ylabel('E')
fig.suptitle('Ising Model {}*{}'.format(N,N), fontsize=16)

axs[1,0].plot(x,np.mean(cv_list, axis=0),'.')
axs[1,0].set_xlabel('Temperature')
axs[1,0].set_title('Cv')
axs[1,0].set_ylabel('Heat Capacity ')

axs[0,0].plot(x,np.mean(np.abs(M_list), axis=0),'.')
axs[0,0].set_xlabel('Temperature')
axs[0,0].set_title('Magnetization')
axs[0,0].set_ylabel('M')

axs[1,1].plot(x,np.mean(chi_list, axis=0),'.')
axs[1,1].set_xlabel('Temperature')
axs[1,1].set_title('Magnetic susceptibility') 
axs[1,1].set_ylabel('Chi')
plt.show()

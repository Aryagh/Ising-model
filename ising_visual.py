import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Slider, Button, RadioButtons

fig = plt.figure()
ax1 = plt.axes([0.65,0.10,0.25,0.35])
ax1.set_title('Mean Energy')
ax2 = plt.axes([0,0.25,0.65,0.65])
ax3 = plt.axes([0.65,0.50,0.25,0.35])
ax3.set_title('Magnetization')

#Parameters
N = 200
B = 0
T = 1
M = 0
M_list = []

s = np.random.choice([-1,1],size=(N,N))
e = []
new_e = 0

for x in range(N):
    for y in range(N):
        new_s = s[x,y]
        M += s[x,y]
        new_e += (-1*(s[(x-1)%N,y%N]*new_s + s[(x+1)%N,y%N]*new_s + s[x%N,(y-1)%N]*new_s + s[x%N,(y+1)%N]*new_s + B*new_s))

e.append(new_e/N**2)
#M_list.append(M/N**2)
line1, = ax1.plot(e,'.')
line2, = ax3.plot(e,'.')
im = ax2.imshow(s)

axcolor = 'lightgoldenrodyellow'
axb = plt.axes([0.1, 0.1, 0.40, 0.03], facecolor=axcolor)
axt = plt.axes([0.1, 0.15, 0.40, 0.03], facecolor=axcolor)

st = Slider(axb, 'T', 0.0, 2.0, valinit=1, valstep=1e-5)
sb = Slider(axt, 'B', -1.0, 1.0, valinit=0, valstep=1e-5)

def animate(i):
    global T, B, M
    T = st.val
    B = sb.val
    new_e = e[-1]
    for _ in range(1000):
        x , y = np.random.randint(0,N,[1,2])[0]
        new_s = s[x,y]
        H1 = -1*(s[(x-1)%N,y%N]*new_s + s[(x+1)%N,y%N]*new_s + s[x%N,(y-1)%N]*new_s + s[x%N,(y+1)%N]*new_s + B*new_s)
        new_s = s[x,y]*-1
        H2 = -1*(s[(x-1)%N,y%N]*new_s + s[(x+1)%N,y%N]*new_s + s[x%N,(y-1)%N]*new_s + s[x%N,(y+1)%N]*new_s + B*new_s)
        H = H2 - H1
        if H < 0 or np.random.rand() < np.exp(-1 / T * H):
            s[x,y] = new_s
            new_e += H/N**2
            M += new_s*2/N**2
    M_list.append(M)
    e.append(new_e)
    im.set_array(s)
    line1.set_data(range(len(e)), e)
    ax1.axis([0, len(e), min(e),max(e)])
    line2.set_data(range(len(M_list)), M_list)
    ax3.axis([0, len(M_list), min(M_list),max(M_list)])
    return line1, line2, im

anim = animation.FuncAnimation(fig, animate, interval=50)

plt.show()

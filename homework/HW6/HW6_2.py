
import numpy as np
import matplotlib.pyplot as plt
import random
from tkinter import _flatten
import math
from matplotlib.animation import FuncAnimation

color = ['red','green','blue']
Center = np.array([(1,5,2),(1,2,5)])
sitesx = []
sitesy = []

sampleNo = 100
sigma = 1.5
for i in range(3):
    Randx = np.random.normal(Center[0,i],sigma,sampleNo)
    Randy = np.random.normal(Center[1,i],sigma,sampleNo)
    sitesx.append(Randx)
    sitesy.append(Randy)
# plt.scatter(sitesx,sitesy)
# plt.scatter(Center[0,:],Center[1,:],c=color)

# print(sitesx)
# plt.show()

# print(len(sitesx))
# print(sitesx)
x = sitesx[0]
y = sitesy[0]
for i in range(len(sitesx)-1):
    x = np.hstack((x,sitesx[i + 1]))
    y = np.hstack((y,sitesy[i + 1]))

startPoint = random.randint(0,len(x) - 1)
SP = []
SP.append(startPoint)
dist = np.zeros([len(x),len(x)])
for i in range(len(x)):
    for j in range(len(y)):
        dist[i,j] = np.linalg.norm((x[i] - x[j])**2)
        dist[j,i] = dist[i,j]
#select initial center
n = 3
while len(SP) < n:
    Max = 0
    Maxindex = -1
    for i in range(len(x)):
        dis = 0
        for j in range(len(SP)):
            dis += dist[i,SP[j]]
        if dis >= Max:
            Max = dis
            Maxindex = i
    SP.append(Maxindex)

print(SP)
SP = [x[SP],y[SP]]
print(len(SP[0]))

# m = 2
#x: sitex   y:sitey     C:center    dist:
def Getdis(x,y):
    return math.sqrt(x**2 + y**2)
def Getmu(x,y,C,m):
    if m == 1:
        return -1
    mu = np.zeros([len(x),len(C[0])])
    for i in range(len(x)):
        for j in range(len(C[0])):
            mu[i,j] = 0
            for h in range(len(C[0])):
                if Getdis(x[i] - C[0][h],y[i] - C[1][h]) == 0:
                    mu[i,j] = 0.0001
                else:
                    mu[i,j] += (Getdis(x[i]-C[0][j],y[i] - C[1][j])/Getdis(x[i] - C[0][h],y[i] - C[1][h]))**(2/(m-1))
                # mu[i,j] += (dist[i,C[j]]/dist[i,h])**(2/(m-1))
            mu[i,j] = mu[i,j] ** (-1)
    return mu

def GetCenter(x,y,mu,m):
    Center = np.zeros([2,len(mu[0])])
    for j in range(len(mu[0])):
        sitexZi = 0
        Fenmu = 0
        siteyZi = 0

        for i in range(len(x)):
            sitexZi += (mu[i,j]**m)*x[i]
            siteyZi += (mu[i,j]**m)*y[i]
            Fenmu += mu[i,j] ** m
        Center[0,j] = sitexZi / Fenmu
        Center[1,j] = siteyZi / Fenmu
    return Center


print(SP)
# print(SP[0][1])
PreCenter = SP
Center = np.zeros([len(SP),len(SP[0])])

mu_ans = []
Center_ans = []

print(Center)
for m in np.linspace(1.1,3,num = 20):
    plt.cla()
    print(m)
    PreCenter = SP
    Center = np.zeros([len(SP),len(SP[0])])
    while np.linalg.norm(Center - PreCenter) > 0.01:
        Center = PreCenter
        mu = Getmu(x,y,PreCenter,m)
        PreCenter = GetCenter(x,y,mu,m)
        # print(PreCenter)
        # print(mu)
    # plt.title("m=".format(m))
    # for i in range(len(mu)):
    #     plt.scatter(x[i],y[i],edgecolors=(mu[i,0]/(mu[i,0] + mu[i,1] + mu[i,2]),mu[i,1]/(mu[i,0] + mu[i,1] + mu[i,2]),mu[i,2]/(mu[i,0] + mu[i,1] + mu[i,2])),marker='o',c='')
    # plt.scatter(PreCenter[0,:],PreCenter[1,:],s=100,c='yellow',marker='D')
    # plt.pause(0.01)
    mu_ans.append(mu)
    Center_ans.append(PreCenter)
    
plt.figure()
plt.ion()
for j in range(len(mu_ans)):
    plt.cla()
    mu = mu_ans[j]
    PreCenter = Center_ans[j]
    for i in range(len(mu)):
        plt.scatter(x[i],y[i],edgecolors=(mu[i,0]/(mu[i,0] + mu[i,1] + mu[i,2]),mu[i,1]/(mu[i,0] + mu[i,1] + mu[i,2]),mu[i,2]/(mu[i,0] + mu[i,1] + mu[i,2])),marker='o',c='')
    plt.scatter(PreCenter[0,:],PreCenter[1,:],s=100,c='yellow',marker='D')
    plt.pause(0.001)
plt.show()
# plt.ioff

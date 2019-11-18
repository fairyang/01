import numpy as np
import matplotlib.pyplot as plt
a = np.arange(0.0,5.0,0.02)
plt.plot(a,np.cos(2*np.pi*a),'r--')

plt.xlabel('横轴:时间',fontproperties='Simhei',fontsize=15,color='green')
plt.ylabel('纵轴:振幅',fontproperties='simhei',fontsize=15,color='blue')
plt.title(r'正弦波实例 $y=cos(2\pi x)$',fontproperties='Simhei',fontsize=25)
plt.text(2,1,r'$\mu=1005$',fontsize=15)

plt.axis([-1,6,-2,2])
plt.grid(True)#添加网格
plt.show()

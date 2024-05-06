import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def frenet_serret(curvature, torsion, start_point, start_TNB, num_points=100):
    # 初始化参数
    s = np.linspace(0, 1, num_points)
    dt = 1.0 / num_points
    
    # 解压初始T, N, B
    T, N, B = start_TNB
    
    # 初始化曲线点
    curve_points = np.zeros((num_points, 3))
    curve_points[0] = start_point
    
    # 迭代计算切线、法线和次法线
    for i in range(1, num_points):
        T = T + curvature * N * dt
        N = N + (torsion * B - curvature * T) * dt
        B = B - torsion * N * dt
        curve_points[i] = curve_points[i-1] + T * dt
    
    return curve_points, (T, N, B)

# 定义曲线上每段的曲率和挠率
curvatures = [1, 1, 1, 5, 1, 1, 1, 1,5] # 曲率列表
torsions = [0.1, 0.1, 0.1, -0.1, 0, 0, 0, 0,0.2]   # 挠率列表

# 初始化曲线的初始点和切线、法线和次法线
start_point = np.array([0, 0, 0])
start_TNB = (np.array([1, 0, 0]), np.array([0, 1, 0]), np.array([0, 0, 1]))

# 收集整条曲线上的点
curve_points_all = [start_point]

# 分段计算曲线的Frenet-Serret框架
for curvature, torsion in zip(curvatures, torsions):
    curve_points, start_TNB = frenet_serret(curvature, torsion, curve_points_all[-1], start_TNB)
    curve_points_all.extend(curve_points[1:])

# 绘制曲线路径
curve_points_all = np.array(curve_points_all)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(curve_points_all[:,0], curve_points_all[:,1], curve_points_all[:,2], color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Curve Path')

plt.savefig('_curve_path.png')

plt.show()

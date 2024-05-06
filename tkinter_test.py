import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
 
# 创建主窗口
root = tk.Tk()
 
# 创建画布1
fig1 = plt.figure(figsize=(5, 4), dpi=100)
canvas1 = FigureCanvasTkAgg(fig1, master=root)
canvas1.draw()
 
# 创建画布2
fig2 = plt.figure(figsize=(5, 4), dpi=100)
canvas2 = FigureCanvasTkAgg(fig2, master=root)
canvas2.draw()
 
# 在画布1上绘制图像
ax1 = fig1.add_subplot(111)
x1 = np.linspace(0, 10, 100)
y1 = np.sin(x1)
ax1.plot(x1, y1)
 
# 在画布2上绘制图像
ax2 = fig2.add_subplot(111)
x2 = np.linspace(0, 10, 100)
y2 = np.cos(x2)
ax2.plot(x2, y2)
 
# 使用grid方法将画布1和画布2上下排列
canvas1.get_tk_widget().grid(row=0, column=0)
canvas2.get_tk_widget().grid(row=1, column=0)
 
# 运行主窗口
root.mainloop()
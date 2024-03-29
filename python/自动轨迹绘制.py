# AutoTrace.py
import turtle as t
t.title("自动轨迹绘制")
t.setup(800,600)
t.pencolor("red")
t.pensize(5)
t.speed(10)
# 数据读取
datals=[]
f=open("data.txt",'rt')
for line in f:
    line=line.replace('\n','')
    datals.append(list(map(eval,line.split(','))))
f.close()
# 自动绘制
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    t.left(datals[i][2]) if datals[i][1]==0 else t.right(datals[i][2])
t.done()

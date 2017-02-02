import tkinter,random,copy
root=tkinter.Tk()
root.title('2048')
root.minsize(700,520)
root.resizable(False,False)
root.iconbitmap("_2048.ico")
bm2 = tkinter.PhotoImage(file = '2.png')        #导入图片
bm4 = tkinter.PhotoImage(file = '4.png')
bm8 = tkinter.PhotoImage(file = '8.png')
bm16 = tkinter.PhotoImage(file = '16.png')
bm32 = tkinter.PhotoImage(file = '32.png')
bm64 = tkinter.PhotoImage(file = '64.png')
bm128 = tkinter.PhotoImage(file = '128.png')
bm256 = tkinter.PhotoImage(file = '256.png')
bm512 = tkinter.PhotoImage(file = '512.png')
bm1024 = tkinter.PhotoImage(file = '1024.png')
bm2048 = tkinter.PhotoImage(file = '2048.png')
bm4096 = tkinter.PhotoImage(file = '4096.png')
bm8192 = tkinter.PhotoImage(file = '8192.png')
bm16384 = tkinter.PhotoImage(file = '16384.png')
bm32768 = tkinter.PhotoImage(file = '32768.png')
bm65536 = tkinter.PhotoImage(file = '65536.png')
bm131072 = tkinter.PhotoImage(file = '131072.png')
white= tkinter.PhotoImage(file = 'white.png')
background=tkinter.Label(root,bg='#d26900',width=520,height=520)             #界面背景颜色
scoreLabel=tkinter.Label(root,text="0",font=("黑体","15"),justify = "right",bg='#d26900',fg='black')    #得分面板
scoreLabel_2=tkinter.Label(root,text="您的得分：",font=("黑体","15"),bg='#d26900',fg='#ffffff')          #得分面板
helpLabel=tkinter.Label(root,bg='#d26900',font=("黑体","15"),fg='#ffffff',text="W:‘向上移动’\nS:‘向下移动’\nA:‘向左移动’\nD:‘向右移动’",justify = "left")  #帮助面板
helpLabel.place(x=550,y=150)              #各个面板布局
scoreLabel_2.place(x=550,y=350)
scoreLabel.place(x=610,y=380)
background.place(x=0,y=0)
a1=tkinter.Label(root,image=white,width=120,height=120)  #初始化16个方块
a2=tkinter.Label(root,image=white,width=120,height=120)
a3=tkinter.Label(root,image=white,width=120,height=120)
a4=tkinter.Label(root,image=white,width=120,height=120)
b1=tkinter.Label(root,image=white,width=120,height=120)
b2=tkinter.Label(root,image=white,width=120,height=120)
b3=tkinter.Label(root,image=white,width=120,height=120)
b4=tkinter.Label(root,image=white,width=120,height=120)
c1=tkinter.Label(root,image=white,width=120,height=120)
c2=tkinter.Label(root,image=white,width=120,height=120)
c3=tkinter.Label(root,image=white,width=120,height=120)
c4=tkinter.Label(root,image=white,width=120,height=120)
d1=tkinter.Label(root,image=white,width=120,height=120)
d2=tkinter.Label(root,image=white,width=120,height=120)
d3=tkinter.Label(root,image=white,width=120,height=120)
d4=tkinter.Label(root,image=white,width=120,height=120)
m =[[a1,a2,a3,a4],                   #将16个方块放入m数组中
    [b1,b2,b3,b4],
    [c1,c2,c3,c4],
    [d1,d2,d3,d4]]
v =[[0,0,0,0],                    #声明数组v，以0代替方块
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]]
m[0][0].place(x=11,y=11)            #将16个方块置入游戏界面
m[0][1].place(x=11,y=136)
m[0][2].place(x=11,y=261)
m[0][3].place(x=11,y=386)
m[1][0].place(x=136,y=11)
m[1][1].place(x=136,y=136)
m[1][2].place(x=136,y=261)
m[1][3].place(x=136,y=386)
m[2][0].place(x=261,y=11)
m[2][1].place(x=261,y=136)
m[2][2].place(x=261,y=261)
m[2][3].place(x=261,y=386)
m[3][0].place(x=386,y=11)
m[3][1].place(x=386,y=136)
m[3][2].place(x=386,y=261)
m[3][3].place(x=386,y=386)
totalScore = 0    #声明全局变量toalScore代表总分
merge=False     #用以控制是否继续合并方块
gameOver=False  #控制游戏是否结束
def display():                  #显示函数，根据数组v，改变数组m内的图片
    for i in range(4):
        for j in range(4):
            if v[i][j]==0:
                m[i][j]["image"]=white
            elif v[i][j]==2:
                m[i][j]["image"]=bm2
            elif v[i][j]==4:
                m[i][j]["image"]=bm4
            elif v[i][j]==8:
                m[i][j]["image"]=bm8
            elif v[i][j]==16:
                m[i][j]["image"]=bm16
            elif v[i][j]==32:
                m[i][j]["image"]=bm32
            elif v[i][j]==64:
                m[i][j]["image"]=bm64
            elif v[i][j]==128:
                m[i][j]["image"]=bm128
            elif v[i][j]==256:
                m[i][j]["image"]=bm256
            elif v[i][j]==512:
                m[i][j]["image"]=bm512
            elif v[i][j]==1024:
                m[i][j]["image"]=bm1024
            elif v[i][j]==2048:
                m[i][j]["image"]=bm2048
            elif v[i][j]==4096:
                m[i][j]["image"]=bm4096
            elif v[i][j]==8192:
                m[i][j]["image"]=bm8192
            elif v[i][j]==16384:
                m[i][j]["image"]=bm16384
            elif v[i][j]==32768:
                m[i][j]["image"]=bm32768
            elif v[i][j]==65536:
                m[i][j]["image"]=bm65536
            elif v[i][j]==131072:
                m[i][j]["image"]=bm131072
def align(vList, direction):             #对齐非零的数字
    for i in range(vList.count(0)):
        vList.remove(0)
    zeros = [0 for x in range(4 - len(vList))]# 被移出了4-len(vList)个0   ,再用0 for x in range(4 - len(vList))补0并计入zeros[]数组中
    if direction == 'left':
        vList.extend(zeros)
    else:
        vList[:0] = zeros     #以zeros数组填充v
def addSame(vList,direction): #合并相同的方块，通过数组v中相邻数字的相加
    global merge
    global totalScore
    if direction =='left':
        for i in [0,1,2]:
            if vList[i]==vList[i+1]!=0:
                vList[i]*=2
                vList[i+1]=0
                totalScore+=vList[i]
                align(vList,direction)
                merge=False
            else:
                merge=False
    else:
        for i in [3,2,1]:
            if vList[i]==vList[i-1]!=0:
                vList[i-1]*=2
                vList[i]=0
                totalScore+=vList[i-1]
                align(vList,direction)
                merge = False
            else:
                merge = False
def handle (vList,direction): #操作的入口
    global merge
    merge=True
    align(vList , direction)   #每次移动前应先清零，再相加，再判断是否合并
    addSame(vList , direction)
    while merge:            #是否合并
        align(vList , direction)
def init(v):#初始化 V，添加两个数字，2或4
    for x in range(2):
        N = 0
        for q in v:
            N += q.count(0)
        k = random.randrange(1, N+1)# 产生随机数k，产生的2或4将被填到第k个空白区域
        n = 0
        for i in range(4):
            for j in range(4):
                if v[i][j] == 0:
                    n += 1
                    if n == k:
                        a=random.random()

                        if a<0.1:
                            v[i][j]=4
                        else:
                            v[i][j]=2
                            break
    display()
def moveor(v1,v2):    #判断是否移动，如果没有移动则不生成新的数字
    for i in range(4):
        for j in range(4):
            if v1[i][j] == v2[i][j]:
                pass
            else:
                return True
    return False
def w(event): #键盘事件
    vmov1=copy.deepcopy(v)   #Vmov1和vmov2对比移动前和移动后的数组是否一致，如果一致则说明没有移动，则不生成新数字
    global gameOver
    if gameOver==True:
        return
    global totalScore
    direction = 'left'
    for row in range(4):
        handle(v[row], direction)
    vmov2=copy.deepcopy(v)
    if moveor(vmov1,vmov2):
        try:
            add()
        except:
            pass
    judge()
    scoreLabel["text"]=totalScore;
    display()
def s(event):
    vmov1=copy.deepcopy(v)
    global gameOver
    if gameOver==True:
        return
    global totalScore
    direction = 'right'
    for row in range(4):
        handle(v[row], direction)
    vmov2=copy.deepcopy(v)
    if moveor(vmov1,vmov2):
        try:
            add()
        except:
            pass
    judge()
    scoreLabel["text"]=totalScore;
    display()
def a(event):
    vmov1=copy.deepcopy(v)
    global gameOver
    if gameOver==True:
        return
    global totalScore
    direction = 'left'
    for col in range(4):
        # 将矩阵中一列复制到一个列表中然后处理
        vList = [v[row][col] for row in range(4)]
        handle(vList, direction)
        # 从处理后的列表中的数字覆盖原来矩阵中的值
        for row in range(4):
            v[row][col] = vList[row]
    vmov2=copy.deepcopy(v)
    if moveor(vmov1,vmov2):
        try:
            add()
        except:
            pass
    judge()
    scoreLabel["text"]=totalScore;
    display()
def d(event):
    vmov1=copy.deepcopy(v)
    global gameOver
    if gameOver==True:
        return
    global totalScore
    direction = 'right'
    for col in range(4):                            # 将矩阵中一列复制到一个列表中然后处理
        vList = [v[row][col] for row in range(4)]
        handle(vList, direction)                    # 从处理后的列表中的数字覆盖原来矩阵中的值
        for row in range(4):
            v[row][col] = vList[row]
    vmov2=copy.deepcopy(v)
    if moveor(vmov1,vmov2):
        try:
            add()
        except:
            pass
    judge()
    scoreLabel["text"]=totalScore;
    display()
def add():
    N1 = 0   # 统计空白区域数目 N
    for q in v:
        N1 += q.count(0)
    if True:#需改
        global gameOver
        if gameOver==False :
            k = random.randrange(1, N1+1)
            n = 0
            for i in range(4):
                for j in range(4):
                    if v[i][j] == 0:
                        n += 1
                        if n == k:
                            a=random.random()
                            if a<0.1:
                                v[i][j]=4
                            else:
                                v[i][j]=2
                                break
def judge():  #判断游戏是否结束
    global v
    global gameOver
    N1 = 0
    for q in v:
        N1 += q.count(0)
    if N1==0:
        for row in range(4):
            for col in range(3):
                if v[row][col]==v[row][col+1]:
                    return
        for row in range(3):
            for col in range(4):
                if v[row][col]==v[row+1][col]:
                    gameOver=False
                    return
                else:
                    gameOver=True
        if gameOver:
            helpLabel["text"]="游戏结束！"
root.bind('<Key-w>',w)
root.bind('<Key-s>',s)
root.bind('<Key-a>',a)
root.bind('<Key-d>',d)
init(v)
root.mainloop() #root主窗口进入消息循环
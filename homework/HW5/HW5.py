from tkinter import *

# 创建并添加 canvas
# 创建窗口
root = Tk()
root.title("五子棋")
gaird_width = 30
gaird_count = 18

widths = gaird_width*gaird_count + 20

root.maxsize(widths, widths)
root.minsize(widths, widths)
# 创建并添加Canvas
cv = Canvas(root, background='white')
cv.pack(fill=BOTH, expand=YES)


# 画一个外边框为白的 , 填充棋盘颜色
# cv.create_rectangle(10,10,gaird_width*gaird_count + 10,gaird_width*gaird_count + 10,outline="white", fill="#CD8500")
cv.create_rectangle(10,10,gaird_width*gaird_count + 10,gaird_width*gaird_count + 10,outline="white", fill="#FFFFFF")

# 在棋盘里面画 画格子
for num in range(1,gaird_count):
    cv.create_line(num*gaird_width + 10 ,
                   gaird_width + 10,
                   num*gaird_width + 10,
                   gaird_width*(gaird_count-1) + 10,
                   width=2,
                   fill="#595959")
for num in range(1,gaird_count):
    cv.create_line(gaird_width + 10 ,
                   num*gaird_width + 10,
                   (gaird_count-1)*gaird_width + 10,
                   num*gaird_width + 10,
                   width=2,
                   fill="#595959"
                   )

def paint(event):
    python_green = "red"
    x: int = int((event.x + 0.5 * gaird_width - 10)/gaird_width)
    y: int = int((event.y + 0.5 * gaird_width - 10)/gaird_width)

    print(x,y)

    x1, y1 = (x*gaird_width ), (y*gaird_width)
    x2, y2 = (x*gaird_width + 20), (y*gaird_width + 20)
    cv.create_oval(x1,y1,x2,y2, fill = python_green)

def paint2(event):
    python_green = "blue"
    x: int = int((event.x + 0.5 * gaird_width - 10)/gaird_width)
    y: int = int((event.y + 0.5 * gaird_width - 10)/gaird_width)

    print(x,y)

    x1, y1 = (x*gaird_width ), (y*gaird_width)
    x2, y2 = (x*gaird_width + 20), (y*gaird_width + 20)
    cv.create_oval(x1,y1,x2,y2, fill = python_green)

def paint3(event):
    python_green = "green"
    x: int = int((event.x + 0.5 * gaird_width - 10)/gaird_width)
    y: int = int((event.y + 0.5 * gaird_width - 10)/gaird_width)
    print(x,y)
    x1, y1 = (x*gaird_width ), (y*gaird_width)
    x2, y2 = (x*gaird_width + 20), (y*gaird_width + 20)
    cv.create_oval(x1,y1,x2,y2, fill = python_green)

def paint4(event):
    python_green = "yellow"
    x: int = int((event.x + 0.5 * gaird_width - 10)/gaird_width)
    y: int = int((event.y + 0.5 * gaird_width - 10)/gaird_width)
    print(x,y)
    x1, y1 = (x*gaird_width ), (y*gaird_width)
    x2, y2 = (x*gaird_width + 20), (y*gaird_width + 20)
    cv.create_oval(x1,y1,x2,y2, fill = python_green)


cv.bind("<Button-1>", paint)
cv.bind("<Button-3>", paint2)
cv.bind("<Double-Button-1>", paint3)
cv.bind("<Button-2>",paint4)
# <Button-1>：鼠标左击事件
# <Button-2>：鼠标中击事件
# <Button-3>：鼠标右击事件
# <Double-Button-1>：双击事件
# <Triple-Button-1>：三击事件

# message = Label(root, text = "press and drag the mouse to tap")
# message.pack(side = BOTTOM)

root.mainloop()
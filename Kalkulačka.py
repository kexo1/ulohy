import tkinter

canvas = tkinter.Canvas(height=99, width=298)
canvas.pack()

povodne = 0
posun = 12
status = 0


def klik(event):
    global posun, povodne, status, cislo, cislo1
    if 70 > event.y > 40:
        if event.x // 30 != 0:
            if status == 3:
                canvas.delete('cislo')
                status = 0

            cislo = povodne * 10 + event.x // 30
            if len(str(cislo)) != 16:
                canvas.create_text(posun, 20, font='Arial 30', text=event.x // 30, tags='cislo')
                posun += 20
                povodne = cislo

    elif event.y > 70 and event.x < 120:

        if event.x // 30 == 0:
            canvas.delete('cislo')
            povodne, posun, status = 0, 12, 0

        elif event.x // 30 in (1, 2):
            if status == 0:
                canvas.delete('cislo')
                povodne, posun, status, cislo1 = 0, 12, event.x // 30, cislo

        elif event.x // 30 == 3:
            if status in (1, 2):
                canvas.delete('cislo')
                if status == 1:
                    canvas.create_text(6, 20, font='Arial 30', text=cislo1 + cislo, tags='cislo', anchor='w')
                else:
                    canvas.create_text(6, 20, font='Arial 30', text=cislo1 - cislo, tags='cislo', anchor='w')
                povodne, posun, status, cislo1 = 0, 12, 3, cislo


for i in range(10):
    canvas.create_rectangle(i * 30, 40, (i + 1) * 30, 70)
    canvas.create_text(i * 30 + 15, 55, text=i)

znaky = ['C', '+', '-', '=']
for i in range(4):
    canvas.create_rectangle(i * 30, 70, (i + 1) * 30, 100)
    canvas.create_text(i * 30 + 15, 85, text=znaky[i])

canvas.bind('<Button-1>', klik)

canvas.mainloop()

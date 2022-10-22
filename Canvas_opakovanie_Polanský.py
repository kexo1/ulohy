import random
import tkinter
from random import choice

canvas = tkinter.Canvas(width=1000, height=800)
canvas.pack()


def zmrzlina():
    canvas.delete('all')
    # VYKRESLENIE GULIČIEK
    canvas.create_oval(95, 45, 145, 95, outline='', fill='red')
    canvas.create_oval(70, 70, 120, 120, outline='', fill='yellow')
    canvas.create_oval(120, 70, 170, 120, outline='', fill='green')

    # VYKRESLENIE KORNÚTKU
    canvas.create_rectangle(70, 100, 170, 120, fill='white', width=2)
    canvas.create_line(170, 120, 120, 260, 70, 120, width=2)


def ceresna():
    canvas.delete('all')
    x, y = splitni()

    # VYKRESLENIE KMEŇA A KORUNY
    canvas.create_rectangle(x + 30, y + 90, x + 70, y + 200, outline='', fill='brown')
    canvas.create_oval(x, y, x + 100, y + 100, outline='', fill='green')

    # VYKRESLENIE ČEREŠNÍ
    canvas.create_line(x + 40, y + 35, x + 60, y + 10, x + 80, y + 35, width=2)
    canvas.create_oval(x + 30, y + 30, x + 50, y + 50, fill='red')
    canvas.create_oval(x + 70, y + 30, x + 90, y + 50, fill='red')


def balon_kosik():
    canvas.delete('all')
    x, y = splitni()

    # VYKRESLENIE LANA
    canvas.create_line(x, y + 50, x + 50, y + 200, width=2)
    canvas.create_line(x + 100, y + 50, x + 50, y + 200, width=2)

    # VYKRESLENIE BALÓNA A OBDĹŽNIKA
    canvas.create_oval(x, y, x + 100, y + 100, fill='blue')
    canvas.create_rectangle(x + 30, y + 200, x + 70, y + 220, fill='red')


def ciarovy_kod():
    canvas.delete('all')

    x = 420
    for _ in range(20):
        # RANDOM HRÚBKA
        hrubka = random.randint(1, 5)
        print(hrubka, end=" ")

        # VYKRESLENIE ČIARY
        canvas.create_line(x, 300, x, 450, width=hrubka)
        x += 7


def obrazok():
    canvas.delete('all')
    a = random.randrange(300, 600)

    # VYKRESLENIE POZADIA
    canvas.create_rectangle(0, 0, 1000, 400, fill='skyblue', outline='')
    canvas.create_rectangle(0, 400, 1000, 1000, fill='lawngreen')
    canvas.create_oval(a, -50, a + 200, 150, fill='yellow')

    x = random.randrange(50, 200)
    y = random.randrange(500, 700)

    # VYKRESLENIE STROMOV
    for i in range(1, 4):
        canvas.create_rectangle(x, y, x + 30, y + 60, fill='brown')
        canvas.create_oval(x - 30, y + 10, x + 60, y - 80, fill='green')
        x = x + 300
        y = random.randint(500, 700)

    b = random.randrange(200, 800)
    colors = ["red", "orange", "yellow", "blue", "indigo", "violet"]

    # VYKRESLENIE DOMU
    canvas.create_rectangle(b, 400, b + 100, 300, fill=random.choice(colors))
    canvas.create_rectangle(b + 10, 320, b + 40, 350, fill='skyblue')
    canvas.create_rectangle(b + 60, 320, b + 90, 350, fill='skyblue')
    canvas.create_rectangle(b + 40, 400, b + 60, 370, fill='brown')
    canvas.create_line(b, 300, b + 50, 250, b + 100, 300)


def balony():
    canvas.delete('all')

    colors = ["red", "orange", "yellow", "blue", "indigo", "violet", "green", "lightgreen"]
    x = 400
    cislo = random.randint(1, 2)
    for _ in range(8):
        # AK 1 TAK VYKRESLI BALÓNY
        if cislo == 1:
            canvas.create_line(565, 400, x + 25, 560)
        else:
            # AK 2 TAK VYKRESLI BALÓNY NAOPAK
            canvas.create_line(565, 720, x + 25, 560)
        # VYKRESLENIE BALÓNA S RANDOM FARBOU
        canvas.create_oval(x, 550, x + 50, 600, fill=random.choice(colors))
        x += 40


def nahodne_ciary():
    canvas.delete('all')

    colours = ["yellow", "red", "green", "blue", "skyblue", "pink", "lightgreen", "orange"]

    # VYKRESLENIE NÁHODNÝCH ČIAR
    if random.randint(1, 2) == 1:
        for i in range(1, 300):
            canvas.create_line(random.randint(100, 900), random.randint(100, 800), random.randint(100, 900),
                               random.randint(100, 800), fill=random.choice(colours), width=random.randint(1, 5))
    # VYKRESLENIE NÁHODNÝCH ČIAR V ŠPIRÁLE
    else:
        for i in range(1, 300):
            canvas.create_line(500, 400, random.randint(0, 900),
                               random.randint(0, 900), fill=random.choice(colours), width=random.randint(1, 5))


def ostrov_s_vlajkou():
    canvas.delete('all')

    # VYKRESLENIE POZADIA
    canvas.create_rectangle(0, 280, 1100, 0, fill='white', outline='')

    # VYKRESLENIE OSTROVA
    canvas.create_oval(20, 250, 220, 450, fill='saddlebrown', outline='')

    # VYKRESLENIE MORA
    canvas.create_rectangle(0, 280, 1100, 900, fill='blue', outline='')

    # VYKRESLENIE VLAJKY
    canvas.create_line(120, 250, 120, 110, width=3)
    canvas.create_rectangle(120, 110, 220, 170, width=3, fill='lime')
    canvas.create_oval(150, 125, 175, 150, fill='yellow', outline='')
    canvas.create_oval(160, 125, 180, 145, fill='lime', outline='')

    # VYKRESLENIE LODI
    canvas.create_line(240, 300, 370, 300, width=3)
    canvas.create_line(240, 300, 220, 260, width=3)
    canvas.create_line(370, 300, 390, 260, width=3)
    canvas.create_line(220, 260, 390, 260, width=3)
    canvas.create_line(305, 260, 305, 160, width=3)
    canvas.create_line(305, 160, 330, 220, 305, 240, width=3)

    # VYKRESLENIE NÁHODNÉHO MESIACA
    y = random.randint(30, 210)
    canvas.create_oval(480, y, 560, y + 80, fill='yellow', outline='')
    canvas.create_oval(510, y, 610, y + 80, fill='white', outline='')
    canvas.create_oval(480, 500 + (-1 * y), 560, 500 + (-1 * y) + 80, fill='yellow', outline='')
    canvas.create_oval(510, 500 + (-1 * y), 610, 500 + (-1 * y) + 80, fill='blue', outline='')


def rebrik():
    canvas.delete('all')

    # VYKRESLENIE 1 REBRÍKA
    canvas.create_line(8, 10, 80, 300)
    canvas.create_line(78, 10, 150, 300)

    x = 0
    y = 0

    for i in range(1, 20):
        canvas.create_line(x, 20 + y, 85 + x, 20 + y)
        x = x + 4
        y = y + 15

    canvas.create_line(280, 10, 208, 300)
    canvas.create_line(350, 10, 278, 300)

    x = 0
    y = 0

    # VYKRESLENIE 2 REBRÍKA
    for i in range(1, 20):
        canvas.create_line(273 + x, 20 + y, 358 + x, 20 + y)
        x = x - 4
        y = y + 15


def obrazce():
    canvas.delete('all')

    ktore = random.randint(1, 3)

    # VYKRESLENIE ČIERNEHO OBRAZCA
    if ktore == 1:
        x = 250
        for i in range(50):
            canvas.create_line(x, 200, 500, 400)
            x += 10

    # VYKRESLENIE ZELENÉHO OBRAZCA
    elif ktore == 2:
        x = 0
        for i in range(100):
            canvas.create_line(0, 0, x, 800, fill='green')
            x += 10

    # VYKRESLENIE MODRÉHO OBRAZCA
    elif ktore == 3:
        x = 0
        for i in range(100):
            canvas.create_line(1000, 800, x, 0, fill='blue')
            x += 10


def kruznice():
    canvas.delete('all')

    colours = ["yellow", "red", "green", "blue", "skyblue", "pink", "lightgreen", "orange"]

    x = 10

    # VYKRESLENIE 20 KRUHOV S NÁHODNÝMI FARBAMI
    for i in range(20):
        velkost = random.randint(25, 50)
        canvas.create_oval(x - velkost, 400 + velkost, x + velkost, 400 - velkost, outline=random.choice(colours),
                           width=3)
        x += 50


def stvorceky():
    canvas.delete('all')

    # VYKRESLENIE X ČIAR
    x = 0
    for i in range(100):
        canvas.create_line(x, 0, x, 800)
        x += 10

    # VYKRESLENIE Y ČIAR
    y = 0
    for i in range(80):
        canvas.create_line(0, y, 1000, y)
        y += 10


def jaskyna():
    canvas.delete('all')

    # VYKRESLENIE POZADIA
    canvas.create_rectangle(0, 0, 1000, 800, fill='green', outline='')
    x = 0

    # VYKRESLENIE KVAPLÍ
    for _ in range(1000):
        y = random.randint(20, 70)
        canvas.create_line(x, y, x, 800 - y, fill='white')
        x += 1

    # POČET MLÁK
    cislo = random.randint(20, 50)

    # PRIEMERNE KOLKO MLÁK ZA DĺŽKU CANVASU
    kolko = 1000 // cislo
    x = 10

    # VYKRESLENIE MLÁK
    for _ in range(cislo):
        velkost = random.randint(20, 100)
        vyska = random.randint(130, 680)
        canvas.create_oval(x - velkost / 2, vyska - velkost / 2, x + velkost / 2, vyska + velkost / 2, fill='blue',
                           outline='')
        x += kolko

    x = 0

    # VYKRESLENIE REBRÍKA
    for _ in range(10):
        canvas.create_rectangle(x, 350, x + 100, 450, outline='brown', width=3)
        x += 100


def zahradka():
    canvas.delete('all')

    # VYKRESLENIE ZEMI
    canvas.create_rectangle(0, 770, 1000, 800, fill='green', outline='')
    x = 0

    # VYKRESLENIE TRÁVY
    for _ in range(100):
        canvas.create_line(x, 750, x, 800, fill='green', width=3)
        x += 10

    # VYKRESLENIE HUBY
    x = 100
    y = 600
    canvas.create_rectangle(x + 42, y + 55, x + 68, y + 135, fill='saddlebrown', outline='')
    canvas.create_oval(x + 42, y + 128, x + 67, y + 143, fill='saddlebrown', outline='')
    canvas.create_arc(x, y, x + 110, y + 110, start=360, extent=180, fill="red", outline='')
    canvas.create_oval(x + 10, y + 50, x + 20, y + 40, fill='white', outline='')
    canvas.create_oval(x + 35, y + 10, x + 45, y + 20, fill='white', outline='')
    canvas.create_oval(x + 55, y + 50, x + 65, y + 40, fill='white', outline='')
    canvas.create_oval(x + 75, y + 10, x + 85, y + 20, fill='white', outline='')

    # VYKRESLENIE SLNKA
    for _ in range(40):
        canvas.create_line(0, 0, random.randint(10, 160), random.randint(10, 160), fill='yellow', width=5)

    # VYKRESLENIE DOMOV
    y = -20
    for i in range(3):
        y += 60
        x = 600
        for j in range(5):
            velkost = random.randint(10, 50)
            canvas.create_rectangle(x, y, x + velkost, y + velkost)
            x += 60

    x = 0
    y = 0

    # VYKRESLENIE MODRÉHO KRUHU
    for _ in range(20):
        canvas.create_oval(600 + x, 600 + y, 600 - x, 600 - y, outline='blue')
        y += 4
        x += 4


def krajinka():
    canvas.delete('all')

    # VYKRESLENIE KVETOV (30-KRÁT)
    for i in range(30):
        x = random.randint(10, 800)
        y = random.randint(10, 500)

        # VYKRESLENIE STOPKY KVETU
        for j in range(20):
            x1 = random.randint(-20, 20)
            y1 = random.randrange(40)
            canvas.create_line(x, y, x - x1, y - y1, fill='green')
            canvas.create_line(x, y, x, y - 50, fill='green', width=2)

        # VYKRESLENIE KVETINY
        for k in range(40):
            x1 = random.randint(-40, 40)
            y1 = random.randint(-40, 40)
            canvas.create_line(x, y - 50, x1 + x, y - 50 - y1, fill='yellow')

    # VYKRESLENIE STROMOV (20-KRÁT)
    for i in range(20):
        x = random.randint(10, 800)
        y = random.randint(10, 450)
        canvas.create_line(x, y, x, y + 150, width=5, fill='saddlebrown')

        # VYKRESLENIE KONÁROV
        for j in range(10):
            x1 = random.randint(-30, 30)
            y1 = random.randint(-10, -1)
            y2 = random.randint(1, 150)
            canvas.create_line(x, y + y2, x + x1, y + y2 + y1, width=2, fill='saddlebrown')


def splitni():
    # SPLITNE ZADANÉHO HODNOTY A OBIDVE ICH VRÁTI
    pozicia = input('Zadajte x a y pozíciu (oddelte medzerou): ')
    pozicia = pozicia.split()
    return int(pozicia[0]), int(pozicia[1])


# OZNAM
canvas.create_text(500, 100,
                   text='Zadajte pozície v shelli ak sa program zasekne (niektoré úlohy vyžadujú zadané koordinácie)\nNa úlohy "obrazce", "náhodné čiary", "balóny" kliknite viackrát lebo majú v sebe dalšie variácie',
                   font='Arial 15 bold', anchor='center')

# VŠETKY BUTTONY NA LAVÝCH POZÍCIACH
button = tkinter.Button(text='Zmrzlina', command=zmrzlina)
button.pack(side='left')

button = tkinter.Button(text='Čerešňa', command=ceresna)
button.pack(side='left')

button = tkinter.Button(text='Balón s košíkom', command=balon_kosik)
button.pack(side='left')

button = tkinter.Button(text='Čiarový kód', command=ciarovy_kod)
button.pack(side='left')

button = tkinter.Button(text='Obrázok', command=obrazok)
button.pack(side='left')

button = tkinter.Button(text='Balóny', command=balony)
button.pack(side='left')

button = tkinter.Button(text='Náhodné čiary', command=nahodne_ciary)
button.pack(side='left')

button = tkinter.Button(text='Ostrov s vlajkou', command=ostrov_s_vlajkou)
button.pack(side='left')

button = tkinter.Button(text='Rebríky', command=rebrik)
button.pack(side='left')

button = tkinter.Button(text='Obrazce', command=obrazce)
button.pack(side='left')

button = tkinter.Button(text='Kružnice', command=kruznice)
button.pack(side='left')

button = tkinter.Button(text='Štvorčeky', command=stvorceky)
button.pack(side='left')

button = tkinter.Button(text='Jaskyňa', command=jaskyna)
button.pack(side='left')

button = tkinter.Button(text='Záhradka', command=zahradka)
button.pack(side='left')

button = tkinter.Button(text='Krajinka', command=krajinka)
button.pack(side='left')

canvas.mainloop()

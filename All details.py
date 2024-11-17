gpu = {
    1: ("RTX 2060", 150),
    2: ("RTX 2070", 200),
    3: ("RTX 2080", 200),
    4: ("RTX 3060", 285),
    5: ("RTX 3070", 260),
    6: ("RTX 3080", 700),
    7: ("RTX 3090", 850),
    8: ("RTX 4070", 600),
    9: ("RTX 4080 super", 1000),
    10: ("RTX 4090", 1600),
}
cpu = {
    1: ("AMD Ryzen 7 7800X3D", 450),
    2: ("AMD Ryzen™ 7 8700G", 280),
    3: ("Intel Core i9-14900k", 440),
    4: ("Intel Core i9-14700k", 350),
    5: ("AMD Ryzen 7 9800X3D", 480),
    6: ("Intel Core i5-10400", 180),
    7: ("AMD Ryzen 5 5500", 160),
    8: ("AMD Athlon 200GE", 150),
    9: ("AMD Ryzen 7 5700X3D", 210),
    10: ("Intel Core i7-13700K", 270)
}
cooler = {
    1: ("Lian Li Galahad II Performance 360", 200),
    2: ("Cooler Master Master Liquid 360 Atmos", 150),
    3: (" ID-Cooling FX360 INF", 100),
    4: ("Silverstone IceMyst 360", 110),
    5: ("Thermalright Peerless Assassin 120 SE", 40)
}
ram = {
    1: ("8GB", 10),
    2: ("16GB", 20),
    3: ("32GB", 40),
    4: ("64GB", 80),
    5: ("128GB", 100)
}
ddr = {
    1: ("DDR3", 7),
    2: ("DDR4", 20),
    3: ("DDR5", 30)
}
mb = {
    1: ("TUF GAMING Z890-PRO WIFI", 320),
    2: ("PRIME Z890-P WIFI", 250),
    3: ("ROG MAXIMUS Z890 EXTREME", 1000),
    4: ("ROG MAXIMUS Z890 APEX", 720),
    5: ("ROG MAXIMUS Z890 HERO", 700),
    6: ("ROG STRIX Z890-F GAMING WIFI", 430),
    7: ("ROG STRIX Z890-I GAMING WIFI", 500),
    8: (" ProArt Z890-CREATOR WIFI", 530),
    9: ("Pro WS WRX90E-SAGE SE", 1300),
    10: ("PRIME Z890-P WIFI-CSM", 250)
}
psu = {
    1: ("Asus Rog Thor 1600W ATX Power Supply Unit", 670),
    2: ("IWONGOU RM 600W PC PSU Power Supply Unit", 40),
    3: ("MSI MEG Ai1300P PCIE5 - Power supply", 300),
    4: ("MSI MAG A650GL 650W 80 Plus Modular Power Supply", 85),
    5: ("VERO ELECTRONICS 116-17509J MONOVOLT PK100 POWER SUPPLY", 1000)
}
case = {
    1: ("Lian Li Lancool 207", 80),
    2: ("Phanteks XT Pro Ultra", 80),
    3: ("Corsair Obsidian Series 4000X RGB", 75),
    4: ("NZXT H9 Elite Dual-Chamber ATX Mid-Tower PC Gaming Case", 165),
    5: ("be quiet! Shadow Base 800 FX", 185)
}
hdd = {
    1: ("1024GB", 50),
    2: ("2048GB", 100),
    3: ("4096GB", 200),
    4: ("8192GB", 400),
    5: ("16384GB", 800)
}
ssd = {
    1: ("1024GB", 70),
    2: ("2048GB", 140),
    3: ("4096GB", 280),
    4: ("8192GB", 560),
    5: ("16384GB", 1120)
}
core = {
    1: ("2", 50),
    2: ("4", 100),
    3: ("8", 200),
    4: ("16", 400),
    5: ("24", 600)
}
price = 0
print('''Привіт! Я - програма-створювач комп'ютерів, і я буду допомагати тобі, зібрати твій комп'ютер!
-------------------------''')
print('''Спочатку розкажу вам правила, кожна деталь буде позначатися цифрою, щоб вибрати цю деталь,
вам потрібно написати цифру яка її позначає. Поїхали!
-------------------------''')
answer1 = input(f'''Давай виберемо тобі процесор:
1 - {cpu[1][0]} ({cpu[1][1]}$)
2 - {cpu[2][0]} ({cpu[2][1]}$)
3 - {cpu[3][0]} ({cpu[3][1]}$)
4 - {cpu[4][0]} ({cpu[4][1]}$)
5 - {cpu[5][0]} ({cpu[5][1]}$)
6 - {cpu[6][0]} ({cpu[6][1]}$)
7 - {cpu[7][0]} ({cpu[7][1]}$)
8 - {cpu[8][0]} ({cpu[8][1]}$)
9 - {cpu[9][0]} ({cpu[9][1]}$)
10 - {cpu[10][0]} ({cpu[10][1]}$)
''')
cpu_an = 0
cpu_an_p = 0
if answer1==("1"):
    cpu_an = cpu[1][0]
    cpu_an_p = cpu[1][1]
    price = price + cpu[1][1]
elif answer1==("2"):
    cpu_an = cpu[2][0]
    cpu_an_p = cpu[2][1]
    price = price + cpu[2][1]
elif answer1==("3"):
    cpu_an = cpu[3][0]
    cpu_an_p = cpu[3][1]
    price = price + cpu[3][1]
elif answer1==("4"):
    cpu_an = cpu[4][0]
    cpu_an_p = cpu[4][1]
    price = price + cpu[4][1]
elif answer1==("5"):
    cpu_an = cpu[5][0]
    cpu_an_p = cpu[5][1]
    price = price + cpu[5][1]
elif answer1==("6"):
    cpu_an = cpu[6][0]
    cpu_an_p = cpu[6][1]
    price = price + cpu[6][1]
elif answer1==("7"):
    cpu_an = cpu[7][0]
    cpu_an_p = cpu[7][1]
    price = price + cpu[7][1]
elif answer1==("8"):
    cpu_an = cpu[8][0]
    cpu_an_p = cpu[8][1]
    price = price + cpu[8][1]
elif answer1==("9"):
    cpu_an = cpu[9][0]
    cpu_an_p = cpu[9][1]
    price = price + cpu[9][1]
elif answer1==("10"):
    cpu_an = cpu[10][0]
    cpu_an_p = cpu[10][1]
    price = price + cpu[10][1]
print(f'''Отже, ти вибрав процесор {cpu_an}, який коштує {cpu_an_p}$. 
Звучить непогано!
-------------------------''')
core_an = 0
core_an_p = 0
answer2 = input(f'''Одразу після процесора, давай виберемо кількість його ядер:
1 - {core[1][0]} ({core[1][1]}$)
2 - {core[2][0]} ({core[2][1]}$)
3 - {core[3][0]} ({core[3][1]}$)
4 - {core[4][0]} ({core[4][1]}$)
5 - {core[5][0]} ({core[5][1]}$)
''')
if answer2==("1"):
    core_an = core[1][0]
    core_an_p = core[1][1]
    price = price + core[1][1]
elif answer2==("2"):
    core_an = core[2][0]
    core_an_p = core[2][1]
    price = price + core[2][1]
elif answer2==("3"):
    core_an = core[3][0]
    core_an_p = core[3][1]
    price = price + core[3][1]
elif answer2==("4"):
    core_an = core[4][0]
    core_an_p = core[4][1]
    price = price + core[4][1]
elif answer2==("5"):
    core_an = core[5][0]
    core_an_p = core[5][1]
    price = price + core[5][1]
print(f'''Чудово! Твій процесор {cpu_an} тепер з {core_an} ядрами! Ідемо далі!
-------------------------''')
ram_an = 0
ram_an_p = 0
answer3 = input(f'''Тепер давай оберемо кількість твоєї оперативної пам'яті:
1 - {ram[1][0]} ({ram[1][1]}$)
2 - {ram[2][0]} ({ram[2][1]}$)
3 - {ram[3][0]} ({ram[3][1]}$)
4 - {ram[4][0]} ({ram[4][1]}$)
5 - {ram[5][0]} ({ram[5][1]}$)
''')
if answer3==("1"):
    ram_an = ram[1][0]
    ram_an_p = ram[1][1]
    price = price + ram[1][1]
elif answer3==("2"):
    ram_an = ram[2][0]
    ram_an_p = ram[2][1]
    price = price + ram[2][1]
elif answer3==("3"):
    ram_an = ram[3][0]
    ram_an_p = ram[3][1]
    price = price + ram[3][1]
elif answer3==("4"):
    ram_an = ram[4][0]
    ram_an_p = ram[4][1]
    price = price + ram[4][1]asd
elif answer3==("5"):
    ram_an = ram[5][0]
    ram_an_p = ram[5][1]
    price = price + ram[5][1]
print(f'''Хороший вибір! {ram_an} оперативної пам'яті за {ram_an_p}$ забезпечать твій
комп'ютер на довго!
-------------------------''')
ddr_an = 0
ddr_an_p = 0
answer4 = input(f'''І одразу після оперативної пам'яті, виберемо її тип:
1 - {ddr[1][0]} ({ddr[1][1]}$)
2 - {ddr[2][0]} ({ddr[2][1]}$)
3 - {ddr[3][0]} ({ddr[3][1]}$)
''')
if answer4==("1"):
    ddr_an = ddr[1][0]
    ddr_an_p = ddr[1][1]
    price = price + ddr[1][1]
elif answer4==("2"):
    ddr_an = ddr[2][0]
    ddr_an_p = ddr[2][1]
    price = price + ddr[2][1]
elif answer4==("3"):
    ddr_an = ddr[3][0]
    ddr_an_p = ddr[3][1]
    price = price + ddr[3][1]
print(f'''{ram_an} {ddr_an} оперативної пам'яті за ще {ddr_an_p}$ є дуже хорошим вибором!
-------------------------''')
print('''Поки що добре ідем! Продовжуємо!
-------------------------''')
mb_an = 0
mb_an_p = 0
answer5 = input(f'''Щоб це все кудись вставити, нам потрібна материнська плата,
тож давай виберемо:
1 - {mb[1][0]} ({mb[1][1]}$)
2 - {mb[2][0]} ({mb[2][1]}$)
3 - {mb[3][0]} ({mb[3][1]}$)
4 - {mb[4][0]} ({mb[4][1]}$)
5 - {mb[5][0]} ({mb[5][1]}$)
6 - {mb[6][0]} ({mb[6][1]}$)
7 - {mb[7][0]} ({mb[7][1]}$)
8 - {mb[8][0]} ({mb[8][1]}$)
9 - {mb[9][0]} ({mb[9][1]}$)
10 - {mb[10][0]} ({mb[10][1]}$)
''')
if answer5==("1"):
    mb_an = mb[1][0]
    mb_an_p = mb[1][1]
    price = price + mb[1][1]
elif answer5==("2"):
    mb_an = mb[2][0]
    mb_an_p = mb[2][1]
    price = price + mb[2][1]
elif answer5==("3"):
    mb_an = mb[3][0]
    mb_an_p = mb[3][1]
    price = price + mb[3][1]
elif answer5==("4"):
    mb_an = mb[4][0]
    mb_an_p = mb[4][1]
    price = price + mb[4][1]
elif answer5==("5"):
    mb_an = mb[5][0]
    mb_an_p = mb[5][1]
    price = price + mb[5][1]
elif answer5==("6"):
    mb_an = mb[6][0]
    mb_an_p = mb[6][1]
    price = price + mb[6][1]
elif answer5==("7"):
    mb_an = mb[7][0]
    mb_an_p = mb[7][1]
    price = price + mb[7][1]
elif answer5==("8"):
    mb_an = mb[8][0]
    mb_an_p = mb[8][1]
    price = price + mb[8][1]
elif answer5==("9"):
    mb_an = mb[9][0]
    mb_an_p = mb[9][1]
    price = price + mb[9][1]
elif answer5==("10"):
    mb_an = mb[10][0]
    mb_an_p = mb[10][1]
    price = price + mb[10][1]
print(f'''{mb_an} утримає всі деталі крепко, красиво і ідеально! Давай робити комп'ютер далі!
-------------------------''')
case_an = 0
case_an_p = 0
answer6 = input(f'''А саму материнську плату буде тримати корпус комп'ютера, тому що ми ждемо, давай виберемо його швидше:
1 - {case[1][0]} ({case[1][1]}$)
2 - {case[2][0]} ({case[2][1]}$)
3 - {case[3][0]} ({case[3][1]}$)
4 - {case[4][0]} ({case[3][1]}$)
5 - {case[5][0]} ({case[3][1]}$)
''')
if answer6==("1"):
    case_an = case[1][0]
    case_an_p = case[1][1]
    price = price + case[1][1]
elif answer6==("2"):
    case_an = case[2][0]
    case_an_p = case[2][1]
    price = price + case[2][1]
elif answer6==("3"):
    case_an = case[3][0]
    case_an_p = case[3][1]
    price = price + case[3][1]
elif answer6==("4"):
    case_an = case[4][0]
    case_an_p = case[4][1]
    price = price + case[4][1]
elif answer6==("5"):
    case_an = case[5][0]
    case_an_p = case[5][1]
    price = price + case[5][1]
print(f'''Корпус {case_an} зробить твій комп'ютер містким, зручним та красивим!
-------------------------''')
ssd_an = 0
ssd_an_p = 0
answer7 = input(f'''Ледь не забули про SSD, давай оберемо її місткість:
1 - {ssd[1][0]} ({ssd[1][1]}$)
2 - {ssd[2][0]} ({ssd[2][1]}$)
3 - {ssd[3][0]} ({ssd[3][1]}$)
4 - {ssd[4][0]} ({ssd[4][1]}$)
5 - {ssd[5][0]} ({ssd[5][1]}$)
''')
if answer7==("1"):
    ssd_an = ssd[1][0]
    ssd_an_p = ssd[1][1]
    price = price + ssd[1][1]
elif answer7==("2"):
    ssd_an = ssd[2][0]
    ssd_an_p = ssd[2][1]
    price = price + ssd[2][1]
elif answer7==("3"):
    ssd_an = ssd[3][0]
    ssd_an_p = ssd[3][1]
    price = price + ssd[3][1]
elif answer7==("4"):
    ssd_an = ssd[4][0]
    ssd_an_p = ssd[4][1]
    price = price + ssd[4][1]
elif answer7==("5"):
    ssd_an = ssd[5][0]
    ssd_an_p = ssd[5][1]
    price = price + ssd[5][1]
print(f'''{ssd_an} SSD пам'яті дозволять вам завантажувати все що ви тільки захочете, хороший вибір!
-------------------------''')
hdd_an = 0
hdd_an_p = 0
answer8 = input(f'''А тепер до SSD підберемо HDD:
1 - {hdd[1][0]} ({hdd[1][1]}$)
2 - {hdd[2][0]} ({hdd[2][1]}$)
3 - {hdd[3][0]} ({hdd[3][1]}$)
4 - {hdd[4][0]} ({hdd[4][1]}$)
5 - {hdd[5][0]} ({hdd[5][1]}$)
''')
if answer8==("1"):
    hdd_an = hdd[1][0]
    hdd_an_p = hdd[1][1]
    price = price + hdd[1][1]
if answer8==("2"):
    hdd_an = hdd[2][0]
    hdd_an_p = hdd[2][1]
    price = price + hdd[2][1]
if answer8==("3"):
    hdd_an = hdd[3][0]
    hdd_an_p = hdd[3][1]
    price = price + hdd[3][1]
if answer8==("4"):
    hdd_an = hdd[4][0]
    hdd_an_p = hdd[4][1]
    price = price + hdd[4][1]
if answer8==("5"):
    hdd_an = hdd[5][0]
    hdd_an_p = hdd[5][1]
    price = price + hdd[5][1]
print(f'''Як і SSD, HDD забезпечать вам багато місткості, тим більше {hdd_an}!
-------------------------''')
cooler_an = 0
cooler_an_p = 0
answer9 = input(f'''Ще одним важливим фактором є охолодження, тому зараз ми з тобою його оберем:
1 - {cooler[1][0]} ({cooler[1][1]}$)
2 - {cooler[2][0]} ({cooler[2][1]}$)
3 - {cooler[3][0]} ({cooler[3][1]}$)
4 - {cooler[4][0]} ({cooler[4][1]}$)
5 - {cooler[5][0]} ({cooler[5][1]}$)
''')
if answer9==("1"):
    cooler_an = cooler[1][0]
    cooler_an_p = cooler[1][1]
    price = price + cooler[1][1]
if answer9==("2"):
    cooler_an = cooler[2][0]
    cooler_an_p = cooler[2][1]
    price = price + cooler[2][1]
if answer9==("3"):
    cooler_an = cooler[3][0]
    cooler_an_p = cooler[3][1]
    price = price + cooler[3][1]
if answer9==("4"):
    cooler_an = cooler[4][0]
    cooler_an_p = cooler[4][1]
    price = price + cooler[4][1]
if answer9==("5"):
    cooler_an = cooler[5][0]
    cooler_an_p = cooler[5][1]
    price = price + cooler[5][1]
print(f'''{cooler_an} є хорошим охолодженням, класно вибрав!
-------------------------''')
gpu_an = 0
gpu_an_p = 0
answer10 = input(f'''Улюблена частина геймерів, відеокарта! Обирай уважно:
1 - {gpu[1][0]} ({gpu[1][1]}$)
2 - {gpu[2][0]} ({gpu[2][1]}$)
3 - {gpu[3][0]} ({gpu[3][1]}$)
4 - {gpu[4][0]} ({gpu[4][1]}$)
5 - {gpu[5][0]} ({gpu[5][1]}$)
6 - {gpu[6][0]} ({gpu[6][1]}$)
7 - {gpu[7][0]} ({gpu[7][1]}$)
8 - {gpu[8][0]} ({gpu[8][1]}$)
9 - {gpu[9][0]} ({gpu[9][1]}$)
10 - {gpu[10][0]} ({gpu[10][1]}$)
''')
if answer10==("1"):
    gpu_an = gpu[1][0]
    gpu_an_p = gpu[1][1]
    price = price + gpu[1][1]
if answer10==("2"):
    gpu_an = gpu[2][0]
    gpu_an_p = gpu[2][1]
    price = price + gpu[2][1]
if answer10==("3"):
    gpu_an = gpu[3][0]
    gpu_an_p = gpu[3][1]
    price = price + gpu[3][1]
if answer10==("4"):
    gpu_an = gpu[4][0]
    gpu_an_p = gpu[4][1]
    price = price + gpu[4][1]
if answer10==("5"):
    gpu_an = gpu[5][0]
    gpu_an_p = gpu[5][1]
    price = price + gpu[5][1]
if answer10==("6"):
    gpu_an = gpu[6][0]
    gpu_an_p = gpu[6][1]
    price = price + gpu[6][1]
if answer10==("7"):
    gpu_an = gpu[7][0]
    gpu_an_p = gpu[7][1]
    price = price + gpu[7][1]
if answer10==("8"):
    gpu_an = gpu[8][0]
    gpu_an_p = gpu[8][1]
    price = price + gpu[8][1]
if answer10==("9"):
    gpu_an = gpu[9][0]
    gpu_an_p = gpu[9][1]
    price = price + gpu[9][1]
if answer10==("10"):
    gpu_an = gpu[10][0]
    gpu_an_p = gpu[10][1]
    price = price + gpu[10][1]
print(f'''{gpu_an} забезпечить велике FPS в багатьох іграх!
-------------------------''')
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Ecological Footprint Calculator')
root.iconbitmap('E:\\PP\\test\\tkinter\\1.ico')

total_gha_dict = {
    'food': 0,
    'foodtransport': 0,
    'housing': 0,
    'house1': 0,
    'house2': 0,
    'electricity': 0,
    'trash': 0,
    'car': 0,
    'bike': 0,
    'public': 0,
    'flight': 0
}

image1 = ImageTk.PhotoImage(Image.open('E:\\PP\\tut\\ss_food\\11.jpg'))
label1 = Label(image=image1)
label1.grid(row=2, column=0, columnspan=9)

#welcome frame
frame = LabelFrame(root, padx=200, pady=200)
frame.grid(row=1, column=0, columnspan=9)
Label(frame, text='''ECOLOGICAL FOOTPRINT CALCULATOR''', font=('Helvetica', 56)).pack()

#food
def food_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='FOOD', font=('Helvetica', 48), padx=550, pady=35)
    frame.grid(row=1, column=0, columnspan=9)
    frame1 = LabelFrame(frame, text='Select:', font=('Helvetica', 20))
    frame1.grid(row=2, columnspan=3, column=0, ipadx=150)
    food_label = Label(frame, text='''How often do you eat animal-based products?
(beef, pork, chicken, fish, eggs, dairy products)
''', font=('YU Gothic UI', 24))
    food_label.grid(row=0, columnspan=3, column=0)
    food_gha = DoubleVar()
    food_list = [
        ('Never', 0.2),
        ('Infrequently', 0.4),
        ('Occasionally', 1),
        ('Often', 1.5),
        ('Very Often', 2.4)
    ]
    food_gha.set(45)

    def set_food_gha(value):
        global food_gha
        food_gha = value
        total_gha_dict['food'] = food_gha
        # Label(frame, text=f'{value}').pack()

    for frequency, value in food_list:
        Radiobutton(frame1, text=frequency, font=('YU Gothic UI', 15), variable=food_gha, value=value,
                    command=lambda: set_food_gha(food_gha.get())).pack()

    def destroy():
        frame.destroy()
        food_transport_frame()

    destroy_button = Button(frame1, text='OK', width=10, command=lambda: destroy()).pack()

# Food Transportation
def food_transport_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='FOOD TRANSPORT', font=('Helvetica', 48), padx=580, pady=150)
    frame.grid(row=1, column=0, columnspan=9)
    foodtransport_label = Label(frame, text='''How much of the food that you eat is processed,
    packaged or not locally grown?''', font=('YU Gothic UI', 25)).pack()
    foodtransport_gha = DoubleVar()
    foodtransport_gha.set(0)

    def hor():
        global foodtransport_gha
        foodtransport_gha = horizontal.get()*0.022
        total_gha_dict['foodtransport'] = foodtransport_gha
        destroy()
        # label1 = Label(frame, text=foodtransport_gha).pack()

    horizontal = Scale(frame, from_=0, to=100, orient=HORIZONTAL, length=600, width=20, sliderlength=70)
    horizontal.pack()
    button2 = Button(frame, text='OK', font='Hack', width=10, command=hor).pack()

    def destroy():
        frame.destroy()
        housing_frame()

# # Housing
def housing_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='HOUSING', font=('Helvetica', 48), padx=500, pady=40)
    frame.grid(row=1, column=0, columnspan=9)
    frame1 = LabelFrame(frame)
    frame1.grid(row=3, columnspan=3, column=0, ipadx=150)

    housing_label = Label(frame, text='''Which housing type best describes your home?
    Freestanding, no running water
    ''', font=('YU Gothic UI', 25))
    housing_label.grid(row=0, columnspan=3, column=0)

    housing_gha = DoubleVar()
    housing_list = [
        ('Freestanding (no water)', 0.3),
        ('Freestanding with water', 0.9),
        ('Multi Storey Apartment', 1.5),
        ('Duplex, row house', 2.1),
        ('Luxury Condomonium', 2.8)
    ]
    housing_gha.set(0)

    def set_housing_gha(value):
        global housing_gha
        housing_gha = value
        total_gha_dict['housing'] = housing_gha


    for type, value in housing_list:
        Radiobutton(frame1, text=type, font=('YU Gothic UI', 15), variable=housing_gha, value=value,
                    command=lambda: set_housing_gha(housing_gha.get())).pack()

    def destroy():
        frame.destroy()
        house_frame()

    destroy_button = Button(frame1, text='OK', font='Hack', width=10, command=lambda: destroy()).pack()

 # House
def house_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='HOUSE DETAILS', font=('Helvetica', 48), padx=600, pady=50)
    frame.grid(row=1, column=0, columnspan=9)
    house1_label = Label(frame, text='''How many people live in your household?''', font=('YU Gothic UI', 25)).pack()
    house1_gha = DoubleVar()

    def set_house1_gha(value):
        global house1_gha
        house1_gha = value * 0.2
        total_gha_dict['house1'] = house1_gha

        # Label(frame,text=house1_gha).pack()

    horizontal1 = Scale(frame, from_=0, to=10, orient=HORIZONTAL, length=600, sliderlength=60, width=20)
    horizontal1.pack()

    button1 = Button(frame, text='OK', font='Hack', width=10, command=lambda: set_house1_gha(horizontal1.get())).pack()

    house2_label = Label(frame, text='''
    What is the size of your home?
    (in sq. ft.)''', font=('YU Gothic UI', 25))
    house2_label.pack()
    house2_gha = DoubleVar()

    def set_house2_gha(value):
        global house2_gha
        house2_gha = value * 0.0015
        total_gha_dict['house2'] = house2_gha
        destroy()
        # Label(frame, text=house2_gha).pack()

    horizontal2 = Scale(frame, from_=5, to=15000, orient=HORIZONTAL, length=600, sliderlength=60, width=20)
    horizontal2.pack()

    button3 = Button(frame, text='OK', font='Hack', width=10, command=lambda: set_house2_gha(horizontal2.get())).pack()

    def destroy():
        frame.destroy()
        electricity_frame()

# # Electricity
def electricity_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='ELECTRICITY', font=('Helvetica', 48), padx=600, pady=120)
    frame.grid(row=1, column=0, columnspan=9)

    light_label = Label(frame, text='''What percentage of your home's electricity 
    comes from non-renewable sources?
    ''', font=('YU Gothic UI', 25)).pack()
    light_gha = DoubleVar()

    def set_light_gha(value):
        global light_gha
        light_gha = value * 0.003
        total_gha_dict['electricity'] = light_gha
        destroy()
        # Label(frame,text=light_gha).pack()

    horizontal = Scale(frame, from_=0, to=100, orient=HORIZONTAL, sliderlength=50, length=600, width=25)
    horizontal.pack()

    button_light = Button(frame, text='OK', font='Hack', width=10,
                          command=lambda: set_light_gha(horizontal.get())).pack()

    def destroy():
        frame.destroy()
        trash_frame()

# #Trash
def trash_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text="TRASH", font=('Helvetica', 48), padx=600, pady=60)
    frame.grid(row=1, column=0, columnspan=9)
    frame1 = LabelFrame(frame)
    frame1.grid(row=3, columnspan=3, column=0, ipadx=150, ipady=30)

    trash_label = Label(frame, text='''Compared to your neighbors,
     how much trash do you generate?
     ''', font=('YU Gothic UI', 25))
    trash_label.grid(row=0, columnspan=3, column=0)
    trash_gha = DoubleVar()

    trash_list = [
        ('Less', 0.2),
        ('Same', 0.5),
        ('More', 1)
    ]

    def set_trash_gha(value):
        global trash_gha
        trash_gha = value
        total_gha_dict['trash'] = trash_gha
        # Label(frame, text= trash_gha).pack()

    trash_gha.set(0)

    for quantity, value in trash_list:
        Radiobutton(frame1, text=quantity, font=('YU Gothic UI', 15), variable=trash_gha, value=value,
                    command=lambda: set_trash_gha(trash_gha.get())).pack()

    def destroy():
        frame.destroy()
        transport1_frame()

    destroy_button = Button(frame1, text='OK', font='Hack', width=10, command=lambda: destroy()).pack()

 #Transportation
def transport1_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text="CAR & BIKE", font=('Helvetica', 48), padx=600, pady=90)
    frame.grid(row=1, column=0, columnspan=9)

    transport_label = Label(frame, text='''How far do you travel by car 
    or motorcycle each week?''', font=('YU Gothic UI', 25)).pack()
    transport_gha = DoubleVar()
    car_gha = DoubleVar()
    bike_gha = DoubleVar()

    def set_car_gha(value):
        global car_gha
        car_gha = value * 0.003875
        total_gha_dict['car'] = car_gha
        # Label(frame, text=car_gha).pack()

    horizontal1 = Scale(frame, from_=0, to=800, orient=HORIZONTAL, length=600, width=20, sliderlength=70)
    horizontal1.pack()

    button_car = Button(frame, text='Car', font=('Hack'), width=10,
                        command=lambda: set_car_gha(horizontal1.get())).pack()

    def set_bike_gha(value):
        global bike_gha
        bike_gha = value * 0.00075
        total_gha_dict['bike'] = bike_gha
        destroy()

    horizontal2 = Scale(frame, from_=0, to=800, orient=HORIZONTAL, length=600, width=20, sliderlength=70)
    horizontal2.pack()

    button_bike = Button(frame, text='Bike', font=('Hack'), width=10,
                         command=lambda: set_bike_gha(horizontal2.get())).pack()

    def destroy():
        frame.destroy()
        transport2_frame()

# #Transport Part II
def transport2_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text="PUBLIC TRANSPORT", font=('Helvetica', 48), padx=600, pady=120)
    frame.grid(row=1, column=0, columnspan=9)

    transport2_label = Label(frame, text='''How far do you travel on 
    public transportation each week?''', font=('YU Gothic UI', 25)).pack()

    public_gha = DoubleVar()

    def get_public_gha(value):
        global public_gha
        public_gha = value * 0.00375
        total_gha_dict['public'] = public_gha
        destroy()

        # Label(frame, text=public_gha).pack()

    horizontal3 = Scale(frame, from_= 0, to = 800, orient=HORIZONTAL, length=600, width=20, sliderlength=70)
    horizontal3.pack()

    button5 = Button(frame, text='OK', font=('Hack'), width=10,
                     command=lambda: get_public_gha(horizontal3.get())).pack()

    def destroy():
        frame.destroy()
        airplane_frame()

# #Airplane
def airplane_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text="AIRPLANE", font=('Helvetica', 48), padx=600, pady=120)
    frame.grid(row=1, column=0, columnspan=9)

    air_label = Label(frame, text='''How many hours do 
    you fly each year?''', font=('YU Gothic UI', 25)).pack()

    air_gha = DoubleVar()

    def get_air_gha(value):
        global air_gha
        air_gha = value * 0.0345
        total_gha_dict['flight'] = value * 0.0345
        destroy()


    horizontal4 = Scale(frame, from_=0, to=200, orient=HORIZONTAL, length=600, width=20, sliderlength=70)
    horizontal4.pack()


        # Label(frame, text=total_gha).pack()

    def destroy():
        frame.destroy()
        result_1_frame()

    button4 = Button(frame, text='OK', font=('Hack'), width=10, command=lambda: get_air_gha(horizontal4.get())).pack()
    # button_total = Button(frame, text='Total',
    #                       command=lambda: get_total_gha()).pack()
#total
def get_total_gha():
    global total_gha
    total_gha = 0
    for keys in total_gha_dict:
        total_gha += total_gha_dict[keys]
#result part I
def result_1_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='Result I', font=('Helvetica',48), padx=600, pady=110)
    frame.grid(row=1,column=0,columnspan=9)
    label1 = Label(frame,text='''If everyone lived like you we would need
''',font=('YU Gothic UI',25)).pack()
    get_total_gha()
    total = total_gha/1.7
    label2 = Label(frame, text=f'{round(total,2)} Earths', font=('YU Gothic UI',36)).pack()

    def destroy():
        frame.destroy()
        result_2_frame()

    next_button = Button(frame,text='OK',font=('Hack',15), command=lambda:destroy()).pack()

#result part II
def result_2_frame():
    global frame
    frame.destroy()
    frame = LabelFrame(root, text='Result II', font=('Helvetica',48),padx=600,pady=60)
    frame.grid(row=1,column=0,columnspan=9)
    result2_label = Label(frame,text='''By consumption category:
    ''', font=('YU Gothic UI',25)).pack()
    total_gha = 0
    for keys in total_gha_dict:
        total_gha += total_gha_dict[keys]
    total_gha /= 100
    mobility = total_gha_dict['car']+total_gha_dict['bike']+total_gha_dict['public']+total_gha_dict['flight']
    label2 = Label(frame,text=f"Mobility: {round(mobility/total_gha,2)}%", font=("YU Gothic UI",20)).pack()
    food = total_gha_dict['food'] + total_gha_dict['foodtransport']
    label3 = Label(frame, text=f'Food: {round(food/total_gha,2)}%', font=("YU Gothic UI",20)).pack()
    services = total_gha_dict['electricity'] + total_gha_dict['trash']
    label4 = Label(frame, text=f'Services: {round(services/total_gha,2)}%', font=('YU Gothic UI',20)).pack()
    house = total_gha_dict['housing'] + total_gha_dict['house1'] + total_gha_dict['house2']
    label5 = Label(frame, text=f'House: {round(house/total_gha,2)}%', font=('YU Gothic UI',20)).pack()

    def destroy():
        frame.destroy()
        result_3_frame()

    next_button = Button(frame, text='OK', font=('Hack', 15), command=lambda: destroy()).pack()

#result part III
def result_3_frame():
    global frame
    frame = LabelFrame(root, text='Result III', font=('Helvetica',48),padx=500,pady=190)
    frame.grid(row=1,column=0,columnspan=9)
    total_gha = 0
    for keys in total_gha_dict:
        total_gha += total_gha_dict[keys]
    if total_gha < 1.2:
        x = total_gha
        total_gha /= 1.2
        total_gha *= 100
        x = 1.2 - x
        x/=1.2
        x*=100
        label = Label(frame, text=f'''Your footprint is {round(x,2)}% lesser compared to an average Indian''', font=('YU Gothic UI',25)).pack()
    else:
        x = total_gha
        total_gha /= 1.2
        total_gha *= 100
        x-= 1.2
        x/=1.2
        x*=100
        label = Label(frame, text=f'''Your footprint is {round(x,2)}% more compared to an average Indian''', font=('YU Gothic UI',25)).pack()




foodfr_buttton = Button(root, text="Food I", command=lambda: food_frame(), font=('YU Gothic UI',16), padx=60)
foodtr_buttton = Button(root, text="Food II", command=lambda: food_transport_frame(), font=('YU Gothic UI',16), padx=60)
housing_buttton = Button(root, text="House I", command=lambda: housing_frame(), font=('YU Gothic UI',16), padx=60)
house_buttton = Button(root, text="House  II", command=lambda: house_frame(), font=('YU Gothic UI',16), padx=60)
electricity_buttton = Button(root, text="Electricity", command=lambda: electricity_frame(), font=('YU Gothic UI',16), padx=60)
trash_buttton = Button(root, text="Trash", command=lambda: trash_frame(), font=('YU Gothic UI',16), padx=60)
transport1_button = Button(root, text="Transport I", command=lambda: transport1_frame(), font=('YU Gothic UI',16), padx=60)
transport2_button = Button(root, text="Transport II", command=lambda: transport2_frame(), font=('YU Gothic UI',16), padx=60)
airplane_button = Button(root, text="Airplane", command=lambda: airplane_frame(), font=('YU Gothic UI',16), padx=60)

foodfr_buttton.grid(row=0, column=0)
foodtr_buttton.grid(row=0, column=1)
housing_buttton.grid(row=0, column=2)
house_buttton.grid(row=0, column=3)
electricity_buttton.grid(row=0, column=4)
trash_buttton.grid(row=0, column=5)
transport1_button.grid(row=0, column=6)
transport2_button.grid(row=0, column=7)
airplane_button.grid(row=0, column=8)

root.mainloop()

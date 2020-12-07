import random 
import json

  
with open("data.json") as file:
    data = json.load(file)


class MyCode:
    def __init__(self, code=[]):
        self.code = code
        your_letters = 'abcdefghifvwqzxp1234567890'
        for i in range(1, 5):
            x = random.choice(your_letters)
            self.code.append(x)
        self.code = "".join(self.code)


class CarType:

    def choose_car(self):
        while True:
            res = data['car_type'][0] + ", " + data['car_type'][1]
            self.JeepSedan = input('\nWhich of the following types is your car:' + res + ' ')
            self.JeepSedan = self.JeepSedan.upper()
            if self.JeepSedan in data['car_type']:
                return self.JeepSedan
            else:
                print('\nIncorrect input')


class District:
    

    def choose_district(self):
        res_data = data['district'][0] + ", " + data['district'][1] + ", " + data['district'][2] + ", " + data['district'][3]

        while True:
            self.district_choice = input('\nWe have four car-washing companies choose the best for you:' + res_data + ' ')
            self.district_choice = self.district_choice.upper()
            if self.district_choice in data['district']:
                return self.district_choice
            else:
                print('\nIncorrect input')


class Stack():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)             

    def remove(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return 'No one in the queue'
        else:
            return 'Busy'
    
    def last(self):
        if not self.is_empty():
            return self.items[-1]
        




class Result:

    def check_choice(self):
        x = Stack()
        print(x.is_empty())
        name = input('Please mention your name ')
        x.add(name)


        MC = MyCode()
        Dist = District.choose_district(self)
        Chose = CarType.choose_car(self)

        car_washer = input('Do you want to take the order ?') == 'y'
        if car_washer:
            print(x.remove())
            print(x.last())
        else:    
            print('Sorry we cant take order, You can visit us next time')


        info = {
            'District':Dist,
            'Car_choice':Chose,
            'Code': MC.code,
            'name': name
        }

        file_name = 'information.json'
        with open(file_name,'a') as f:
            json.dump(info,f,indent=2)


        if Dist == 'ZEYTUN':
            zey_data1 = data['choice_zeytun'][0] 
            print("\n",zey_data1)

            if  Chose == 'JEEP':
                zey_data2 = data['choice_zeytun'][1]
                print("\n",zey_data2,MC.code)


            elif Chose == 'SEDAN':
                zey_data3 = data['choice_zeytun'][2]
                print("\n",zey_data3,MC.code)

        elif Dist == 'KOMITAS':
            kom_data1 = data['choice_komtas'][0]
            print("\n",kom_data1)

            if Chose == 'JEEP':
                kom_data2 = data['choice_komtas'][1]
                print("\n",kom_data2,MC.code)

            elif Chose == 'SEDAN':
                kom_data3 = data['choice_komtas'][2]
                print("\n",kom_data3,MC.code)


        elif Dist == 'NOR-NORK':
            nor_data1 = data['choice_nornork'][0]
            print("\n",nor_data1)

            if Chose == 'JEEP':
               nor_data2 = data['choice_nornork'][1]
               print("\n",nor_data2,MC.code)

            elif Chose == 'SEDAN':
                nor_data3 = data['choice_nornork'][2]
                print("\n",nor_data3,MC.code)

        elif Dist == 'EREBUNI':
            erbuni_data1 = data['choice_erebuni'][0]
            print("\n",erbuni_data1)

            if Chose == 'JEEP':
                erbuni_data2 = data['choice_erebuni'][1]
                print("\n",erbuni_data2,MC.code)
            elif Chose == 'SEDAN':
                erbuni_data3 = data['choice_erebuni'][2]
                print("\n",erbuni_data3,MC.code)


def main():

    print('\n Welcome \n')
    while True:
        people_choice = input('if you want to wash your car input yes(y) if no input no ') == 'y'
        if people_choice:
            a = Result()
            a.check_choice()
            break
        elif people_choice == 'no':
            print('\nAlways ready to help you when you need it \n')
            break
        else:
            print('\nIncorrect input')


main()





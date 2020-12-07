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


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def last(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def first(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None 
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def remove_last(self): 
        if self.head is not None:
            temp = self.head
            while(temp.next is not None):
                prev  = temp
                temp = temp.next
            prev.next = None
        else:
            print('Nothing to remove')

    def print_list(self):
        cur = self.head
        while cur:
            print('\n',cur.data)
            cur = cur.next


class Result:

    def check_choice(self):

        name = input('Please mention your name ')
        premium_user = input("If you want to be the first in the queue you can type (y) Premium Option,Otherwise input (n) ") == 'y'
        res = ''
        dllist = DoublyLinkedList()
        dllist.last('Ani')

        if premium_user:
            res = '|Premium Choice + 1000amd'
            dllist.first(name)
            name += ' -- Premium User'
        else:   
            dllist.last(name)

        MC = MyCode()
        Dist = District.choose_district(self)
        Chose = CarType.choose_car(self)

        car_washer = input('Done washing the car ? ') == 'y'
        if car_washer:
            dllist.remove_last()
            dllist.print_list()
        else:    
            dllist.print_list()


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
                print("\n",zey_data2,MC.code,res)


            elif Chose == 'SEDAN':
                zey_data3 = data['choice_zeytun'][2]
                print("\n",zey_data3,MC.code,res)

        elif Dist == 'KOMITAS':
            kom_data1 = data['choice_komtas'][0]
            print("\n",kom_data1)

            if Chose == 'JEEP':
                kom_data2 = data['choice_komtas'][1]
                print("\n",kom_data2,MC.code,res)

            elif Chose == 'SEDAN':
                kom_data3 = data['choice_komtas'][2]
                print("\n",kom_data3,MC.code,res)


        elif Dist == 'NOR-NORK':
            nor_data1 = data['choice_nornork'][0]
            print("\n",nor_data1)

            if Chose == 'JEEP':
               nor_data2 = data['choice_nornork'][1]
               print("\n",nor_data2,MC.code,res)

            elif Chose == 'SEDAN':
                nor_data3 = data['choice_nornork'][2]
                print("\n",nor_data3,MC.code,res)

        elif Dist == 'EREBUNI':
            erbuni_data1 = data['choice_erebuni'][0]
            print("\n",erbuni_data1)

            if Chose == 'JEEP':
                erbuni_data2 = data['choice_erebuni'][1]
                print("\n",erbuni_data2,MC.code,res)
            elif Chose == 'SEDAN':
                erbuni_data3 = data['choice_erebuni'][2]
                print("\n",erbuni_data3,MC.code,res)


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





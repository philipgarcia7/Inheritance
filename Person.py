class Person:
    def __init__(self, name, address, phonenum):
        self.__name = name
        self.__address = address
        self.__phonenum = phonenum

    def print_person(self):
        print("The person's name is:", self.__name)
        print("The person's address is:", self.__address)
        print("The person's phone number is:", self.__phonenum)


class Customer(Person):
    def __init__(self, name, address, phonenum, cus_num, mail_list):

        Person.__init__(self, name, address, phonenum)

        self.__cus_num = cus_num
        self.__mail_list = mail_list
    
    def print_person(self):
        Person.print_person(self)
        print("The customer number is:", self.__cus_num)
        print("Does the customer want to be on the mailing list?:", self.__mail_list)

from cars import Car
from cars import Cars
from companies import Company
from companies import Companies
import pickle

cars = None
companies = None

try:
    f = open('data.pk1', 'rb')
except IOError:
    print 'Cannot open file!!!'
    companies = Companies()
    cars = Cars()
    data = {}
else:
    data = pickle.load(f)
    companies = Companies(data['companies'], data['plast'])
    cars = Cars(data['cars'], data['last'])
    f.close()
    if not companies.empty():
        print 'Data has been loaded'
    else:
        print 'File has been found, but it has any data'


def show_menu():
    print "\n1. 'companies'\n2. 'cars'\n3. Back"
    while True:
        key = raw_input("Select table: ")
        if key == '1':
            if not companies.empty():
                print companies
            else:
                print '"companies" is empty'
            return
        elif key == '2':
            if not cars.empty():
                print cars
            else:
                print "'cars' is empty"
            return
        elif key == '3':
            return
        print 'Wrong Answer. Please Try Again!'


def delete_menu():
    print "\n1. 'companies'\n2. 'cars'\n3. Back"
    while True:
        key = raw_input('Select table: ')
        if key == '1':
            while True:
                try:
                    cid = int(raw_input('Enter cid: '))
                except ValueError:
                    print 'Wrong Answer. Please Try Again!'
                else:
                    if not companies.exist(cid):
                        print "Company with cid={} doesn't exist!".format(cid)
                    else:
                        companies.delete(cid)
                        companies.last -= 1
                    return
        elif key == '2':
            while True:
                try:
                    carid = int(raw_input('Enter carid: '))
                except ValueError:
                    print 'Wrong Answer. Please Try Again!'
                else:
                    if not cars.exist(carid):
                        print "Cars with carid={} doesn't exist!".format(carid)
                    else:
                        cars.delete(carid)
                        cars.last -= 1
                    return
        elif key == '3':
            return
        print 'Wrong Answer. Please Try Again!'


def add_menu():
    print "\n1. 'companies'\n2. 'cars'\n3. Back"
    while True:
        key = raw_input("Select table: ")
        if key == '1':
            name = raw_input('Enter company name: ')
            carname = raw_input('Enter carname:')
            companies.add(Company(companies.last, name, carname))
            return
        elif key == '2':
            carname = raw_input('Enter carname:')
            while True:
                try:
                    size = int(raw_input('Enter size of a car:'))
                except ValueError:
                    print 'Wrong Answer. Please Try Again!'
                else:
                    cars.add(Car(cars.last, carname, size))
                    return
        elif key == '3':
            return
        print 'Wrong Answer. Please Try Again!'


def update_menu():
    print "\n1. 'companies'\n2. 'cars'\n3. Back"
    while True:
        key = raw_input("Select table: ")
        if key == '1':
            while True:
                try:
                    cid = int(raw_input('Enter cid: '))
                except ValueError:
                    print 'Wrong answer, try again'
                else:
                    if not companies.exist(cid):
                        print "Product with cid={} doesn't exist!".format(cid)
                    else:
                        name = raw_input('Enter new name: ')
                        companies[cid].name = name
                        carname = raw_input('Enter new carname: ')
                        companies[cid].carname = carname
                        return
        if key == '2':
            while True:
                try:
                    carid = int(raw_input('Enter carid'))
                except ValueError:
                    print 'Wrong answer, try again'
                else:
                    if not cars.exist(carid):
                        print "Product with carid={} doesn't exist!".format(carid)
                    else:
                        carname = raw_input('Enter new carname:')
                        cars[carid].carname = carname
                        while True:
                            try:
                                size = int(raw_input('Enter new size:'))
                            except ValueError:
                                print 'Wrong Answer, try again'
                            else:
                                cars[carid].size = size
                                return
        if key == '3':
            return
        print 'Wrong Answer, try again'


def filter_menu():
    while True:
        try:
            n = int(raw_input('Enter size you need:'))
        except ValueError:
            print 'Wrong answer, try again'
        else:
            companies.find(cars.find(n))
            return


actions = {'1': show_menu, '2': delete_menu, '3': add_menu, '4': update_menu, '5': filter_menu}

while True:
    print "\n1. SHOW \n2. DELETE \n3. ADD \n4. UPDATE \n5. Filter\n6. Save&Exit"
    try:
        key = raw_input('Select action: ')
    except KeyboardInterrupt:
        break
    else:
        if key in actions:
            actions[key]()
        elif key == '6':
            data = {
                'companies': companies.companies,
                'cars': cars.cars,
                'plast': companies.last,
                'last': cars.last
            }
            with open('data.pk1', 'wb') as f:
                pickle.dump(data, f)
                f.close()
            print 'Data has been saved'
            break
        else:
            print 'Wrong Answer. Please Try Again!'

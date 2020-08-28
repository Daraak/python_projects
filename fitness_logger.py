import datetime
date_1 = datetime.datetime.now()

n = 'y'
while n == 'y':
    print('What function you want to perform, type the number accordingly;'
          '\n1 = Log_data', '\n2 = Get_data')
    user = input('Tell me:- ')
    if user == '1' or user == '2':
        user = int(user)
        if user == 1:
            def log_data():
                print('Whose data you want to log, type the number accordingly;'
                      '\n1 = Harry', '\n2 = Rohan', '\n3 = Hammad')
                client = input('Tell me:- ')
                if client == '1' or client == '2' or client == '3':
                    client = int(client)
                    if client == 1:
                        print('Which file you want to log, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                log_info = input('Enter the workout:- ')
                                with open('harry_exe.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            elif file == 2:
                                log_info = input('Enter the meal:- ')
                                with open('harry_diet.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                    if client == 2:
                        print('Which file you want to log, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                log_info = input('Enter the workout:- ')
                                with open('rohan_exe.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            elif file == 2:
                                log_info = input('Enter the meal:- ')
                                with open('rohan_diet.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                    if client == 3:
                        print('Which file you want to log, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                log_info = input('Enter the workout:- ')
                                with open('hammad_exe.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            elif file == 2:
                                log_info = input('Enter the meal:- ')
                                with open('hammad_diet.txt', 'a') as f1:
                                    f1.write('[' + str(date_1) + '] ' + log_info + '\n')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                else:
                    print("Wrong Input! Please enter one of the given options")
            log_data()
        else:
            def get_data():
                print('Whose data you want to retrieve, type the number accordingly;'
                      '\n1 = Harry', '\n2 = Rohan', '\n3 = Hammad')
                client = input('Tell me:- ')
                if client == '1' or client == '2' or client == '3':
                    client = int(client)
                    if client == 1:
                        print('Which file you want to see, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                try:
                                    with open('harry_exe.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            elif file == 2:
                                try:
                                    with open('harry_diet.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                    if client == 2:
                        print('Which file you want to see, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                try:
                                    with open('rohan_exe.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            elif file == 2:
                                try:
                                    with open('rohan_diet.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                    if client == 3:
                        print('Which file you want to see, type the number accordingly;'
                              '\n1 = Workout', '\n2 = Diet')
                        try:
                            file = int(input('Tell me:- '))
                        except:
                            print("Wrong Input! Please enter one of the given options")
                        else:
                            if file == 1:
                                try:
                                    with open('hammad_exe.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            elif file == 2:
                                try:
                                    with open('hammad_diet.txt', 'r') as f1:
                                        print(f1.read())
                                except:
                                    print('File not found')
                            else:
                                print("Wrong Input! Please enter one of the given options")
                else:
                    print("Wrong Input! Please enter one of the given options")
            get_data()
    else:
        print("Wrong Input! Please enter one of the given options")
    n = input('Do you want to continue [y / n] Default[n]:- ')
    if n == '' or n == 'n':
        print('Good Bye! Take care of your health')
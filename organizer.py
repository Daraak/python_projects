import os


def soldier(path, format_type, *names):
    os.chdir(path)
    files = os.listdir()
    num = 1
    for file in files:
        if file.endswith(format_type):
            f_string = file.split('.')[0]
            if f_string in names:
                print(f_string)
                continue
            elif f_string not in names:
                os.rename(file, str(num)+format_type)
                num += 1


path1 = input('Enter the path of the folder:- ')
form = input('Enter the file format (with \'.\'):- ')
not_change = input('Enter the file names which you don\'t want\'t to change'
                   '(each name separated with space):- ')
soldier(path1, form, not_change)
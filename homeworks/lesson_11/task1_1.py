
def read_file(file_name):
    with open(file_name, 'r') as my_file:
        print(my_file.read())


if __name__ == '__main__':

    file_name = input('Input file name to read: ')

    read_file(file_name)
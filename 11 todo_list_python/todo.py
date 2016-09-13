import sys, csv

command_line = sys.argv[1:]

def usage():
    f = open('usage.txt')
    usage_contents = f.read()
    f.close()
    return usage_contents

def menu():
    try:
        if len(command_line) < 1:
            return usage()
        elif command_line[0] == "-l":
            return list_function()
        elif command_line[0] == "-a":
            return add_task()
        elif command_line[0] == "-r":
            return(remove_task())
        elif command_line[0] == "-c":
            return(check_task())
        elif command_line[0] == "-u":
            return(uncheck_task())
    except SyntaxError:
        print('Unsupported argument')
        return usage()
    except IOError:
        open('store_todos.csv', 'a')

def list_function():
    with open('store_todos.csv', 'r') as f:
        reader = list(csv.reader(f))
        number_of_row = 0
        for i in reader:
            number_of_row += 1
            for j in i:
                if j == 'True':
                    print(str(number_of_row) + ' [x] ' + i[1])
                elif j == 'False':
                    print(str(number_of_row) + ' [ ] ' + i[1])
    if len(reader) == 0:
        return 'No todos for today! :)'

def add_task():
    if len(command_line) == 1:
        return('Unable to add: No task is provided')
    with open('store_todos.csv', 'r') as f:
        reader = list(csv.reader(f))
        num_lines = 1
        for row in reader:
            num_lines += 1
        with open('store_todos.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['False', command_line[1]])

def remove_task():
    if len(command_line) == 1:
        return('Unable to remove: No index is provided')
    if not command_line[1].isdigit():
        return('Unable to remove: Index is not a number')
    item_to_remove = int(command_line[1])
    with open('store_todos.csv', 'r') as f:
        reader = list(csv.reader(f))
        num_lines = 1
        if item_to_remove > len(reader):
            return('Unable to remove: Index is out of bound')
        del reader[item_to_remove-1]
        with open('store_todos.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(reader)

def check_task():
    if len(command_line) == 1:
        return('Unable to remove: No index is provided')
    if not command_line[1].isdigit():
        return('Unable to check: Index is not a number')
    with open('store_todos.csv') as f:
        reader = list(csv.reader(f))
        task_to_check = int(command_line[1])
        number_of_row = 0
        for i in reader:
            number_of_row += 1
            if int(command_line[1]) > len(reader):
                return('Unable to check: Index is out of bound')
            if number_of_row == task_to_check:
                i[0] = True
    with open('store_todos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(reader)

def uncheck_task():
    if len(command_line) == 1:
        return('Unable to remove: No index is provided')
    if not command_line[1].isdigit():
        return('Unable to check: Index is not a number')
    with open('store_todos.csv') as f:
        reader = list(csv.reader(f))
        task_to_check = int(command_line[1])
        number_of_row = 0
        for i in reader:
            number_of_row += 1
            if int(command_line[1]) > len(reader):
                return('Unable to check: Index is out of bound')
            if number_of_row == task_to_check:
                i[0] = False
    with open('store_todos.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(reader)

print(menu())

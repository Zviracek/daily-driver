import datetime
import icalendar as ic
import calendar as cal
import event, file_handler
import glob
import os

task_path = './tasks/'
def create_task():
    # TODO: Validate inputs
    print('Name:')
    name = input()

    print('Date: yy-mm-dd, empty for next week')
    line = input()
    if line == '':
        date = datetime.date.today() + datetime.timedelta(days=7)
    else:
        line = line.split('-')
        date = datetime.date(int(line[0])+2000, int(line[1]), int(line[2]))
    
    print('Time: hh:mm, empty for midnight')
    line = input()
    if line == '':
        time_h = 0
        time_m = 0
    else:
        line = line.split(':')
        time_h = int(line[0])
        time_m = int(line[1])
    time = datetime.time(time_h, time_m)

    task = event.Task(date, time, name, None, None, 0, False, False)
    save_task(task)

def save_task(task):
    file_handler.save_task(task_path + str(task.name) + '.txt', task)

def load_tasks():
    files = glob.glob('./tasks/*.txt')
    tasks = []
    for file in files:
        task = file_handler.load_task(file)
        tasks.append(task)
    return sorted(tasks, key=lambda x: (x.date, x.time))

def print_tasks(tasks):
    # TODO: Better formating
    print('Number | Name | Date | Completed')
    for i in range(len(tasks)):
        print(str(i+1) + ': ' + tasks[i].name + ' ' + str(tasks[i].date) + ' [' + ('x' if tasks[i].completed else ' ') + ']')
    print()

def get_next_week_tasks():
    tasks = load_tasks()
    tasks_next_week = []
    for task in tasks:
        if task.date - datetime.date.today() < datetime.timedelta(days=8) and not task.completed:
            tasks_next_week.append(task)
    print('Tasks due to next week:')
    print_tasks(tasks_next_week)

def complete_task():
    # TODO: Validate input
    tasks = load_tasks()
    tasks_not_completed = []
    for task in tasks:
        if not task.completed:
            tasks_not_completed.append(task)
    print('All uncompleted tasks:')
    print_tasks(tasks_not_completed)

    print('Input number of task to mark as done, zero for none.')
    num = int(input())
    print()
    os.system('clear')
    if num == 0:
        return
    tasks_not_completed[num-1].completed = True
    save_task(tasks_not_completed[num-1])

def delete_task():
    # TODO: Validate input
    tasks = load_tasks()
    print('All created tasks:')
    print_tasks(tasks)
    
    print('Input number of task to delete, zero for none.')
    num = int(input())
    print()
    os.system('clear')
    if num == 0:
        return
    file_handler.delete_task(task_path + tasks[num-1].name + '.txt')

# TODO: chechk if ./tasks exists
# Start of routine
os.system('clear')
# Simple loop for task input
while(True):
    print('Create Task: <c>, Print Task: <p>, Get tasks for week: <w>, Mark tasks as done: <m>, Remove tasks: <r>')
    line = input()
    print()
    os.system('clear')
    if line == 'c':
        create_task()
    elif line == 'p':
        tasks = load_tasks()
        print('All created tasks:')
        print_tasks(tasks)
    elif line == 'w':
        get_next_week_tasks()
    elif line == 'm':
        complete_task()
    elif line == 'r':
        delete_task()
    else:
        continue

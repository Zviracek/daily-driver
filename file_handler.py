import datetime
import event
import os

mate_reg = r'^\d\d:\d\d$'
date_reg = r'^\d\d\d\d-\d\d-\d\d'

def save_task(path: str, task: event.Task):
    if not path.endswith('.txt'):
        raise ValueError('Given path is not valid file')

    with open(path, 'w') as fw:
        fw.write(task.name + '\n')

        fw.write(str(task.date) + '\n')
        fw.write(str(task.time) + '\n')
        
        fw.write(str(task.recuring) + '\n')
        fw.write(str(task.priority) + '\n')

        fw.write(str(task.group) + '\n')
        fw.write(str(task.description) + '\n')

        fw.write(str(task.completed) + '\n')

def load_task(path: str) -> event.Event:
    if not path.endswith('.txt'):
        raise ValueError('Given path is not valid file')

    with open(path, 'r') as fr:
        name = fr.readline().rstrip('\n')
        start_date = fr.readline().rstrip('\n')
        start_time = fr.readline().rstrip('\n')
        recuring = fr.readline().rstrip('\n')
        priority = fr.readline().rstrip('\n')
        group = fr.readline().rstrip('\n')
        description = fr.readline().rstrip('\n')
        completed = fr.readline().rstrip('\n')
        
        start_date = start_date.split('-')
        start_time = start_time.split(':')

        recuring = recuring == 'True'
        priority = int(priority)

        completed_bool = completed == 'True'
    
    start_date_task = datetime.date(int(start_date[0]), int(start_date[1]), int(start_date[2]))
    start_time_task = datetime.time(int(start_time[0]), int(start_time[1]))

    return event.Task(start_date_task, start_time_task, name, description, group, priority, recuring, completed_bool)

def delete_task(path: str):
    os.remove(path)
#!/usr/bin/env python3
import os
import signal

# get tasks
def get_tasks():
    task_list = []
    tasks = os.popen('ps aux')

    for task in tasks:
        fields = task.strip().split(' ')
        task_list.append(fields)

    return task_list

# get pid
def get_pid(tasks):
    pids = []

    for task in tasks:
        pids.append(task[1])

    return pids

# get chromium tasks out of tasklist
def get_chromium(tasks):
    chromium_tasks = []

    for task in tasks:
        if 'chromium' in task[10].lower():
            chromium_tasks.append(task)

    return chromium_tasks

if  __name__ == '__main__':
    for pid in get_pid(get_chromium(get_tasks()))
        os.kill(int(pid), signal.SIGKILL)

#!/usr/bin/env python3
import os
import signal


# get tasks
def get_tasks():
    # task container
    task_container = []

    # get tasks
    tasks = os.popen('ps aux')

    for task in tasks:
        fields = task.strip().split(' ')
        fields = filter(None, fields)

        task_container.append(fields)

    return task_container


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
        for field in task:
            if 'chromium' in field or 'Chromium' in field:
                chromium_tasks.append(task)
                continue

    return chromium_tasks


if  __name__ == '__main__':
    tasks = get_tasks()
    chromium_tasks = get_chromium(tasks)
    pids = get_pid(chromium_tasks)

    for pid in pids:
        os.kill(int(pid), signal.SIGKILL)

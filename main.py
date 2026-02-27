import sys
import json
import os
import time

file_name = "data.json"
seconds = time.time()

action = sys.argv[1]
ref = sys.argv[2]

try:
    task = sys.argv[3]
except IndexError:
    pass

time_created = time.ctime(seconds)
time_updated = time.ctime(seconds)

ref_ind = int(ref) - 1

if os.path.exists(file_name): # checking and reading previous data
    with open(file_name, "r") as file:
        tasks = json.load(file)
else: 
    tasks = []
    

if action == "add":
    task_object = {
    "status" : action,
    "id" : ref,
    "description" : task,
    "createdAt" : time_created,
    "updatedAt" : time_updated
}
    tasks.append(task_object)

if action == "update":
    tasks[ref_ind]['description'] = task
    tasks[ref_ind]['updatedAt'] = time_updated

if action == "delete":
    del tasks[ref_ind]


with open("data.json", "w") as file:
    json.dump(tasks, file, indent = 4)
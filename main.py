import sys
import json
import os
import time

file_name = "data.json"
seconds = time.time()

action = sys.argv[1]
ref = sys.argv[2]
task = sys.argv[3]
local_time = time.ctime(seconds)

if os.path.exists(file_name):
    with open(file_name, "r") as file:
        tasks = json.load(file)
else: 
    tasks = []


task_object = {
    "status" : action,
    "id" : ref,
    "description" : task,
    "createdAt" : local_time,
    "updatedAt" : local_time

}

tasks.append(task_object)

with open("data.json", "w") as file:
    json.dump(tasks, file, indent = 4)
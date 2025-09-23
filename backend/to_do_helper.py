import json
from datetime import datetime as dt

#initialize git -- Done
#Add first task with id, desc, status, create_date, update_date
def add_tasks(task:str, status:str):
    try:
        with open("task_tacker.json", "r") as file:
            data = json.load(file)
            data["count"] += 1
            data["total_tasks"][data["count"]] = {
                "task": task,
                "status": status.title(),
                "created_date": dt.now().strftime("%d-%m-%Y"),
                "updated_date": dt.now().strftime("%d-%m-%Y")
            }

    except FileNotFoundError as exp:
            print(f"File Not present. Creating a new file")
            data = {
                "count": 1,
                "total_tasks": {
                    1: {
                        "task": task,
                        "status": status.title(),
                        "created_date": dt.now().strftime("%d-%m-%Y"),
                        "updated_date": dt.now().strftime("%d-%m-%Y")
                    }

                }
            }

    with open("task_tacker.json", "w") as file:
        json.dump(data, file, indent=4)

    print (f"Task: {task} added to your task list | Status: {status.title()} | ID: {data["count"]}")

def print_list(index, task):
    print(f"Task.{index + 1}: {task["task"]} | Status: {task["status"]} | Created Date: {task["created_date"]} | Last Updated: {task["updated_date"]}")

def list_tasks(option):
    try:
        with open("task_tacker.json", "r") as file:
            data = json.load(file)

            for index,task in enumerate(data["total_tasks"].values()):
                if task["status"].lower() == "in-progress" and  option.lower() == "in-progress":
                    print_list(index, task)
                elif task["status"].lower() == "done" == option.lower():
                    print_list(index, task)
                elif option.lower() == "not-done":
                    if task["status"].lower() != "done":
                        print_list(index, task)
                elif option.lower == "all":
                    print_list(index, task)
    except FileNotFoundError as fne:
        print("No Tasks found")
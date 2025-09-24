import json
from datetime import datetime as dt
import logging

#initialize git -- Done
#Add first task with id, desc, status, create_date, update_date
#done:Add docstring for functions
#Todo: Change print statements to loggers
logger = logging.getLogger(name='__name__')
logging.basicConfig(format= "%(levelname)s:%(message)s", level= logging.DEBUG)

def add_tasks(task:str, status:str):
    """
    Function that handles addition of task to the cli app
    :param task: Accepts string input of task description
    :param status: OPTIONAL. Argument for status of task defaults to "To-do" status
    :return: None
    """
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
        logger.warning(f"File Not present. Creating a new file")
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

    logger.info(f"Task: {task} added to your task list | Status: {status.title()} | ID: {data["count"]}")

def print_list(index, task):
    """
    Prints the list of tasks from json file iteration
    :param index: Id of task
    :param task: description of task to be printed
    :return: None
    """
    logger.info(f"Task.{index + 1}: {task["task"]} | Status: {task["status"]} | Created Date: {task["created_date"]} | Last Updated: {task["updated_date"]}")

def list_tasks(option):
    """
    Lists the tasks already added by user
    :param option: Accepts string values of all, done, in-progress and not-done options to be listed
    :return: None
    """
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
            elif option.lower() == "all":
                print_list(index, task)
    except FileNotFoundError as fne:
        logger.warning("No Tasks found")

def update_or_delete_task(task_id, desc=None, status = None):
    """
    Function to update task description or status or delete task based on the provided id
    :param task_id: String value of task id should be passed.
    :param desc: To update description of the task this parameter should be passed.
    :param status: To update status of the task this parameter should be passed.
    :return: None
    """
    data = {}
    try:
        with open("task_tacker.json", "r") as file:
            data= json.load(file)
    except FileNotFoundError as fne:
        logger.warning("No task has been added yet. Please add task to proceed")

    if desc:
        if data:
            data["total_tasks"][task_id]["task"] = desc
            data["total_tasks"][task_id]["updated_date"] = dt.now().strftime("%d-%m-%Y")
            with open("task_tacker.json", "w") as file_w:
                json.dump(data, file_w, indent=4)
            logger.info(f"Task: {task_id} updated!")
    elif status:
        if data:
            data["total_tasks"][task_id]["status"] = status
            with open("task_tacker.json", "w") as file_w:
                json.dump(data, file_w, indent=4)
            logger.info(f"Status of Task: {task_id} updated!")
    else:
        if data:
            del data["total_tasks"][task_id]
            with open("task_tacker.json", "w") as file_w:
                json.dump(data, file_w, indent=4)
            logger.info(f"Task: {task_id} deleted!")






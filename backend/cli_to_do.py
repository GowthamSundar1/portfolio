#Started 17/09/2025
import argparse
from to_do_helper import *


parser = argparse.ArgumentParser(prog= "To-do List:",
                                 description= "This simple CLI app lets you organise your tasks better",
                                 epilog="Thanks for trying it out!")

subparser = parser.add_subparsers(dest="option", description="Describes the options of the to-do app")

add_task = subparser.add_parser("add", help="Adds a new task")
add_task.add_argument(dest="task", type= str, metavar= "TASK", help= "Enter task to be added")
add_task.add_argument("-s", "--status", dest="status", type= str, metavar= "STATUS", default="To-do")
add_task.set_defaults(func=add_tasks)

#done:List tasks
list_task = subparser.add_parser("list", help="Lists tasks present in the application.")
list_task.add_argument(dest="list", type= str, metavar="LIST", help= "Lists the tasks",
                       choices=["all", "in-progress", "done", "not-done"])


update_task = subparser.add_parser("update", help="Updates the progress of an already added task")
delete_task = subparser.add_parser("delete", help="Delete completed or unwanted tasks")

args = parser.parse_args()

if args.option == "add":
    add_tasks(args.task, args.status)
if args.option == "list":
    list_tasks(args.list)


#Todo:update task using id and update status and update_date

#Todo:List task that are done / not done/ in-progress

#Todo: Change print statements to loggers
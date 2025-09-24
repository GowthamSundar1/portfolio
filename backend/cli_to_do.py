#Started 17/09/2025
import argparse
from to_do_helper import *


class Main:

    def __init__(self):
        self.parser = argparse.ArgumentParser(prog= "To-do List:",
                                         description= "This simple CLI app lets you organise your tasks better",
                                         epilog="Thanks for trying it out!")

        self.subparser = self.parser.add_subparsers(dest="option", description="Describes the options of the to-do app")

    def start_app(self):
        """
        Method to start the to do application functionalities
        :return:
        """
        add_task = self.subparser.add_parser("add", help="Adds a new task")
        add_task.add_argument(dest="task", type= str, metavar= "TASK", help= "Enter task to be added")
        add_task.add_argument("-s", "--status", dest="status", type= str, metavar= "STATUS", default="To-do")
        add_task.set_defaults(func=add_tasks)

        #done:List tasks
        #done:List task that are done / not done/ in-progress
        list_task = self.subparser.add_parser("list", help="Lists tasks present in the application.")
        list_task.add_argument(dest="list", type= str, metavar="LIST", help= "Lists the tasks",
                               choices=["all", "in-progress", "done", "not-done"])

        #done:update task using id and update status and update_date
        update_task = self.subparser.add_parser("update", help="Updates the progress of an already added task")
        update_task.add_argument(dest="id", type= str, metavar= "ID", help= "ID of task to be updated")
        update_task.add_argument(dest="update", type= str, metavar= "UPDATE", help= "Update the description of task")

        #done:Marking a task as in-progress or done
        mark_task = self.subparser.add_parser("mark", help= "Mark the status of a particular task using id")
        mark_task.add_argument(dest="id", type= str, metavar= "ID", help= "ID of task for which status is to be updated")
        mark_task.add_argument(dest="status", type= str, metavar= "STATUS", help= "Status to be updated for the task",
                               choices=["all", "in-progress", "done"])

        #done:Delete task using id
        delete_task = self.subparser.add_parser("delete", help="Delete completed or unwanted tasks")
        delete_task.add_argument(dest="id", type= str, metavar= "ID", help= "ID of task to be deleted")

        args = self.parser.parse_args()

        if args.option == "add":
            add_tasks(args.task, args.status)
        elif args.option == "list":
            list_tasks(args.list)
        elif args.option == "update":
            update_or_delete_task(task_id= args.id, desc= args.update)
        elif args.option == "mark":
            update_or_delete_task(task_id= args.id, status= args.status)
        elif args.option == "delete":
            update_or_delete_task(task_id= args.id)

if __name__ == "__main__":
    to_do_app = Main()
    to_do_app.start_app()
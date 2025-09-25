Project Title: To-do CLI App

Description: 
This is a simple command line application to manage basic tasks. This maybe simple but it does not distract you with targeted ads or political campaigns.

Project Usage:
1. Use add command to add tasks to the app, optionally you can use -s or --status to set the status of the task when you start.
Example: list "My first task" (or) list "My first task" --status in-progress
2. Use list command to list the added tasks. Permitted options are "all", "done", "not-done", "in-progress". Example: list all (or) list done (or) list not-done (or) list in-progress
3. Use update command to update the description of added tasks. Use id of task to update the task. Example: update 1 "My first task more descriptively"
4. Use mark command to update the status of the task. This also takes id and updated status arguments. Example: mark 2 in-progress (or) mark 1 done
5. Use delete command to delete the tasks as needed. This takes only id of task as argument. Example: delete 1
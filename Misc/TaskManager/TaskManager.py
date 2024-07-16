# Simple Task Manager

# Features:
    # Add tasks with descriptions and due dates.
    # Mark tasks as completed.
    # Filter tasks by completion status or due date.

from datetime import datetime, time

def createDate(month, day, year):
    if 1 <= month <= 12 and 1 <= day <= 31 and year >= 1:
        return datetime(year, month, day).date()
    else: 
        raise ValueError("Invalid Date. Year must be 1 or greater, Month must be 1-12, Day must be 1-31.")

def createTime(hour24, min60):
    if 0 <= hour24 <= 23 and 0 <= min60 <= 59:
        return time(hour24, min60)
    else:
        raise ValueError("Invalid time: hour must be 0-23 and minute must be 0-59")

# Create a Task class to handle storage and functionality of Tasks.
class Task:
    def __init__(self, description, due_date, due_time):
        self.date_entered = datetime.now()
        self.due_date = due_date
        self.due_time = due_time
        self.description = description

    def __str__(self):
        return f"""
    Task Description: {self.description}
    Date Task was entered: {self.date_entered.date()} 
    Task Due Date/Time: {self.due_date} at {self.due_time.strftime("%H:%M")}
    """
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def display_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

def mainLoop():
    task_manager = TaskManager()
    
    while True:
        command = input("Enter a command. Valid commands are: add (add a task), remove (remove a task), display (display a list of tasks), quit (quit the program).").strip().lower()
        
        match command: 
            case "add":
                description = input("Enter the task description: ")
                due_month = int(input("Enter the due month (1-12): "))
                due_day = int(input("Enter the due day (1-31): "))
                due_year = int(input("Enter the due year: "))
                due_hour = int(input("Enter the due hour (0-23): "))
                due_minute = int(input("Enter the due minute (0-59): "))
                
                try:
                    due_date = createDate(due_month, due_day, due_year)
                    due_time = createTime(due_hour, due_minute)
                    task = Task(description, due_date, due_time)
                    task_manager.add_task(task)
                    print("Task added successfully!")
                except ValueError as e:
                    print(f"Error: {e}")
                    
            case "remove":
                task_manager.display_tasks()
                try:
                    index = int(input("Enter the task number to remove: ")) - 1
                    task_manager.remove_task(index)
                    print("Task removed successfully!")
                except (ValueError, IndexError):
                    print("Invalid task number")

            case "display":
                task_manager.display_tasks()

            case "quit":
                print("Exiting the task manager. Goodbye!")
                break

            case _:
                print("Invalid command. Please try again.")
                
if __name__ == "__main__":
    mainLoop()

# # Example usage
# task1 = Task(description="Take out the Trash", due_date=createDate(7, 31, 2024), due_time=createTime(10, 30))
# task2 = Task(description="Prepare presentation", due_date=createDate(5, 8, 2024), due_time=createTime(19, 0))

# print(task1)
# print(task2)
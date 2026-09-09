def add_task(tasks, task):
    tasks.append({
        "title": task,
        "completed": False
    })


def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст")
        return

    for i, task in enumerate(tasks, start=1):
        status = "x" if task["completed"] else " "
        print(f"{i}. [{status}] {task['title']}")


def complete_task(tasks, task_number):
    if task_number < 1 or task_number > len(tasks):
        raise ValueError("Такой задачи нет")

    tasks[task_number - 1]["completed"] = True


def delete_task(tasks, task_number):
    if task_number < 1 or task_number > len(tasks):
        raise ValueError("Такой задачи нет")

    tasks.pop(task_number - 1)

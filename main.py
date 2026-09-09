from task_manager import (
    add_task,
    show_tasks,
    complete_task,
    delete_task,
)


def main():
    tasks = []

    while True:
        print("\n=== TODO LIST ===")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Выполнить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")

        choice = input("Выберите действие: ")

        try:
            if choice == "1":
                show_tasks(tasks)

            elif choice == "2":
                task = input("Введите задачу: ")
                add_task(tasks, task)
                print("Задача добавлена!")

            elif choice == "3":
                task_number = int(input("Номер задачи: "))
                complete_task(tasks, task_number)
                print("Задача выполнена!")

            elif choice == "4":
                task_number = int(input("Номер задачи: "))
                delete_task(tasks, task_number)
                print("Задача удалена!")

            elif choice == "5":
                print("До свидания!")
                break

            else:
                print("Неизвестная команда")

        except ValueError as error:
            print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()

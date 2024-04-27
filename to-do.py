import os
import json

class ToDoApp:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Задача '{task}' успешно добавлена!")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.save_tasks()
            print(f"Задача '{task}' успешно удалена!")
        else:
            print(f"Задача '{task}' не найдена!")

    def list_tasks(self):
        if self.tasks:
            print("Ваши задачи:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Задачи не найдены!")

    def run(self):
        while True:
            print("\n--- Приложение To-Do ---")
            print("1. Добавить задачу")
            print("2. Удалить задачу")
            print("3. Список задач")
            print("4. Выйти")
            choice = input("Введите номер выбранной опции: ")

            if choice == "1":
                task = input("Введите задачу: ")
                self.add_task(task)
            elif choice == "2":
                task = input("Введите задачу для удаления: ")
                self.remove_task(task)
            elif choice == "3":
                self.list_tasks()
            elif choice == "4":
                print("Завершение работы приложения To-Do. Удачного дня!")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    app = ToDoApp()
    app.run()

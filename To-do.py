tasks = []

while True:
    print("\n" + "=" * 40)
    print("         TO-DO LIST APPLICATION")
    print("=" * 40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Clear All Tasks")
    print("6. Task Summary")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added successfully!")

    elif choice == "2":
        if not tasks:
            print("📋 No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, t in enumerate(tasks, start=1):
                status = "✅ Completed" if t["done"] else "⏳ Pending"
                print(f"{i}. {t['task']} - {status}")

    elif choice == "3":
        if not tasks:
            print("No tasks available.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            try:
                num = int(input("Enter task number to mark as completed: "))
                tasks[num - 1]["done"] = True
                print("🎉 Task marked as completed!")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

    elif choice == "4":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num - 1)
                print(f"🗑️ '{removed['task']}' removed successfully!")
            except (ValueError, IndexError):
                print("❌ Invalid task number.")

    elif choice == "5":
        confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
        if confirm == "yes":
            tasks.clear()
            print("🧹 All tasks cleared!")

    elif choice == "6":
        total = len(tasks)
        completed = sum(task["done"] for task in tasks)
        pending = total - completed

        print("\n===== TASK SUMMARY =====")
        print(f"📌 Total Tasks     : {total}")
        print(f"✅ Completed Tasks : {completed}")
        print(f"⏳ Pending Tasks   : {pending}")

    elif choice == "7":
        print("👋 Thank you for using the To-Do List Application!")
        break

    else:
        print("❌ Invalid choice! Please enter a number between 1 and 7.")

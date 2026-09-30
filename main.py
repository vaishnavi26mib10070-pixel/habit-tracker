from habit_tracker.storage import load_data
from habit_tracker.habits import add_habit, view_habits, delete_habits, edit_habit
from habit_tracker.tracker import mark_done
from habit_tracker.streaks import show_streaks
from habit_tracker.charts import category_pie_chart, completions_bar_chart


def main():
    data = load_data()
    while True:
        print("\n=== MY HABIT TRACKER ===")
        print("1. Add New habit")
        print("2. View All habits")
        print("3. Delete a habit")
        print("4. Edit a habit")
        print("5. Mark habit as done today")
        print("6. View streaks")
        print("7. Show charts")
        print("0. Exit")
        # asks user for the choice
        choice = input("Choose: ").strip()
        if choice == "1":
            add_habit(data)
        elif choice == "2":
            view_habits(data)
        elif choice == "3":
            delete_habits(data)
        elif choice == "4":
            edit_habit(data)
        elif choice == "5":
            mark_done(data)
        elif choice == "6":
            show_streaks(data)
        elif choice == "7":
            category_pie_chart(data)
            completions_bar_chart(data)
        elif choice == "0":
            print("Goodbye! Have a nice day!")
            break
        else:
            print("Invalid choice. Fill again.")


if __name__ == "__main__":
    main()
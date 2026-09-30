from datetime import date
from habit_tracker.storage import save_data
from habit_tracker.habits import view_habits


def mark_done(data):
    view_habits(data)
    habit_id = input("Enter ID of the habit that you completed today: ").strip()
    today = str(date.today())

    if today not in data["completions"]:
        data["completions"][today] = []
    for item in data["habits"]:
        if str(item["id"]) == habit_id:
            if int(habit_id) in data["completions"][today]:
                print("Already marked as done for today.")
                return


            data["completions"][today].append(int(habit_id))
            save_data(data)
            print(f"Marked '{item['name']}' as done for {today}!")
            return


    print("No habit found with that ID.")
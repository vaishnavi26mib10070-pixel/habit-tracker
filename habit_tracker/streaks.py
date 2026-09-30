from datetime import date, timedelta


def get_current_streak(data, habit_id):
    streak = 0
    day = date.today()

    while True:
        day_text = str(day)
        completions_today = data["completions"].get(day_text, [])

        if habit_id in completions_today:
            streak += 1
            day = day - timedelta(days=1)
        else:
            break


    return streak


def show_streaks(data):
    print("\nHabit Streaks")
    print("-" * 30)
    for item in data["habits"]:
        if item.get("archived", False):
            continue
        streak = get_current_streak(data, item["id"])
        print(f"{item['name']}: {streak} day streak")
from datetime import date
from habit_tracker.storage import save_data


def add_habit(data):
    habit = input("Enter the habit name: ").strip()
    if not habit:
        print("The habit cannot be empty.")
        return
    category = input("Enter category (e.g. Health, Study): ").strip() or "General"
    new_id = 1
    for item in data["habits"]:
        if item["id"] >= new_id:
            new_id = item["id"] + 1


    data["habits"].append({
        "id": new_id,
        "name": habit,
        "category": category,
        "created": str(date.today()),
        "archived": False,
    })
    save_data(data)
    print(f"Successfully Added '{habit}'!")


def view_habits(data):
    if not data["habits"]:
        print("No habits yet. ")
        return
    print("\nID | Habit Name | Category")
    print("-" * 30)
    for item in data["habits"]:
        if item.get("archived", False):
            continue
        print(f"{item['id']}  | {item['name']} | {item['category']}")


def delete_habits(data):
    view_habits(data)
    habit_id = input("Enter the ID of the habit to delete: ").strip()
    for item in data["habits"]:
        if str(item["id"]) == habit_id:
            item["archived"] = True
            save_data(data)
            print(f" '{item['name']}' has been deleted.")
            return


    print("no habit found with that ID.")


def edit_habit(data):
    view_habits(data)
    habit_id = input("Enter the ID of the habit to edit: ").strip()

    for item in data["habits"]:
        if str(item["id"]) == habit_id:
            new_name = input(f"New name (leave blank to keep '{item['name']}'): ").strip()
            new_category = input(f"New category (leave blank to keep '{item['category']}'): ").strip()

            if new_name:
                item["name"] = new_name
            if new_category:
                item["category"] = new_category


            save_data(data)
            print("Habit updated successfully!")
            return


    print("No habit found with that ID.")
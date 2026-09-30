import matplotlib.pyplot as plt


def category_pie_chart(data):
    counts = {}
    for item in data["habits"]:
        if item.get("archived", False):
            continue
        cat = item["category"]
        counts[cat] = counts.get(cat, 0) + 1


    if not counts:
        print("NO habits to show.")
        return

    plt.figure()
    plt.pie(counts.values(), labels=counts.keys(), autopct="%1.0f%%")
    plt.title("Habits by Category")
    plt.savefig("category_chart.png")
    plt.close()
    print("Saved chart as category_chart.png")


def completions_bar_chart(data):
    dates = sorted(data["completions"].keys())
    if not dates:
        print("No completions to show.")
        return

    counts = [len(data["completions"][d]) for d in dates]

    plt.figure()
    plt.bar(dates, counts)
    plt.title("Completions per Day")
    plt.xlabel("Dates")
    plt.ylabel("Habits completed")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("completions_chart.png")
    plt.close()
    print("Saved chart as completions_chart.png")
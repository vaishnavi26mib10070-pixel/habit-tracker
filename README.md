# Habit Tracker with Data Visualization

A command-line habit tracker built in Python. Users can add habits, mark them done, track streaks, and view progress through charts (pie chart and bar chart) made using matplotlib.


## Features
--> Add, view, edit, and delete(archive) habits with a name and category.
--> Mark habits done every day.
--> Won't let you mark the same habit twice on the same day.
--> Shows how many days in a row (streak) you've completed a habit.
--> Two charts:
   _-->_ Pie chart: here habits are grouped by category (`category_chart.png`)
   _-->_ Bar chart: shows how many habits you have completed each day (`completions_chart.png`)
--> All the data is saved in `habit_json`, so nothing gets lost when you close the program.


## Technologies Used
- Pyhton 3
- matplotlib (for the charts)
- JSON (to save all the data locally)

## This is the Project Structure

habit-tracker
-main.py
-habits.jason
-README.md
-statement.md
-habit_tracker
-init.py
-storage.py #loads/saves data
-habits.py #add,view,edit,delete habits
-tracker.py #mark habits as done
-streaks.py #does streak calculations
-charts.py #pie chart and bar chart generation

## How to Set Up and Run

1. check Python is installed: python --version
2. Clone this repository:git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

3. Install matplotlib: python -m pip install matplotlib
4. Run the Program: python main.py


## How to Test

1. Choose `1` to add a habit
2. Choose `2` to view all habits
3. Choose `5` to mark a habit done for today
4. Choose `6` to see the streak for each habit
5. Choose `7` to mark the charts (two PNG files will be saved in the folder)
6. Choose `3` to delete a habit, or Choose `4` to edit one 
7. Choose `0` to exit 


## Screenshots 

![Add and View Habits](SS%201.png)
![Delete And Edit Habits](SS%202.png)
![Editing and Marking done](SS%203.png)
![Streaks and Charts](SS%204.png)
![Final Output](SS%205.png)
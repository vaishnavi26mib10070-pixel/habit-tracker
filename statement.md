# Problem Statement & Project Scope

## Problem Statement
In today's fast-paced routine, individuals often struggle to build and maintain positive daily habits. Traditional habit tracking methods, such as paper journals or basic to-do lists, lack real-time feedback, streak accountability, and data-driven insights. Users often lose motivation without visual representations of their progress and consistency over time.


## Project Scope
The **Habit Tracker with Data Visualization** is a command-line application built in Python designed to help users track daily activities, maintain consistency, and analyze habits through graphical reporting.


### Key Capabilities Included in Scope:
- Interactive command-line interface for seamless management of habits.
- Ability to add, view, edit, mark, and archive/delete daily habits.
- Automatic logging of completion timestamps to prevent duplicate daily entries.
- Calculation and display of current and longest habit completion streaks.
- Visual progress analytics generated using Matplotlib (Category-wise breakdown pie chart and Daily completion trend bar chart).
- Persistent JSON file storage ensuring no data loss between application sessions.


### Out of Scope:
- Graphical User Interface (GUI) / Web Interface (CLI-only design).
- Cloud user authentication or multi-device real-time sync.


## Target Users
1. **Students & Learners:** Looking to track study routines, practice sessions, or daily reading habits.
2. **Fitness Enthusiasts:** Tracking daily workouts, hydration, or meditation goals.
3. **Professionals & Self-Improvers:** Anyone seeking a lightweight, data-backed personal accountability tool.


## High-Level Features
1. **Habit Lifecycle Management:** Full CRUD (Create, Read, Update, Delete/Archive) capabilities categorized by custom habit types.
2. **Daily Execution & Validation:** Interactive completion module with duplicate prevention for the same day.
3. **Streak Calculation Engine:** Algorithmic determination of current consecutive active days.
4. **Data Visualization Engine:** Generation of PNG charts (`category_chart.png` and `completions_chart.png`) capturing habit distribution and historical performance.
5. **JSON Storage & Recovery System:** Structured file-based persistence layer for offline usability.


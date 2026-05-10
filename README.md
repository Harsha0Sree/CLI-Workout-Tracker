CLI Workout Logger

A modular Python CLI application that generates calisthenics workouts based on difficulty level and tracks completed reps during a workout session.

Features
Difficulty-based workout generation
Interactive CLI workout logger
Input validation and retry handling
Total workout volume calculation
Structured workout summaries
Modular project architecture
Project Structure
forge/
│
├── forge.py          # Main application flow
├── workouts.py       # Workout data
├── validator.py      # Validation logic
├── formatter.py      # Output formatting
├── README.md
├── requirements.txt
└── .gitignore
Technologies Used
Python 3
CLI-based interaction
Modular software design
How It Works
User selects a workout difficulty
Program validates input
Workout routine is displayed
User logs completed reps for each exercise
Program calculates total workout volume
Session summary is displayed
Example Usage
$ python forge.py

Example session:

whats your level (beginner[b]?intermediate[i]?advanced[a]?) b

incline_pushups             10 reps
squats                      30 reps
assisted_pullups            10 reps

lets start the workout shall we ?

how many reps did you finish for incline_pushups 12
how many reps did you finish for squats 30
how many reps did you finish for assisted_pullups 8

Workout Summary

Exercise                      reps
--------------------------------------------------
incline_pushups               12
squats                        30
assisted_pullups              8

Total volume is 50

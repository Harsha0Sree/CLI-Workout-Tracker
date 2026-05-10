# Forge CLI Workout Logger

A modular Python CLI application that generates calisthenics workouts based on difficulty level and logs completed workout sessions interactively through the terminal.

---

# Features

- Difficulty-based workout generation
- Interactive workout logging
- Input validation with retry loops
- Total workout volume calculation
- Formatted workout summaries
- Modular project structure
- Exception handling for invalid inputs

---

# Project Structure

```bash
forge/
│
├── forge.py          # Main application flow
├── workouts.py       # Workout data and routines
├── validator.py      # Input validation logic
├── formatter.py      # Workout summary formatting
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies Used

- Python 3
- CLI (Command Line Interface)

---

# Concepts Practiced

## Python Fundamentals

- Variables
- Dictionaries
- Lists
- Loops
- Functions
- Conditionals
- Imports
- Exception Handling

## Software Engineering Concepts

- Modularization
- Separation of Concerns
- Validation Layer
- Formatting Layer
- Structured Data Design
- Input Retry Architecture

---

# How It Works

1. User selects a workout difficulty level
2. Program validates the input
3. Workout routine is displayed
4. User logs completed reps for each exercise
5. Program calculates total workout volume
6. Workout summary is displayed

---

# Installation

## Clone the repository

```bash
git clone https://github.com/yourusername/forge-cli-workout-logger.git
```

## Move into the project directory

```bash
cd forge-cli-workout-logger
```

## Run the application

```bash
python forge.py
```

---

# Example Usage

```text
$ python forge.py

whats your level (beginner[b]?intermediate[i]?advanced[a]?) b

incline_pushups             10 reps
squats                      30 reps
assisted_pullups            10 reps
rows                        10 reps

lets start the workout shall we ?

how many reps did you finish for incline_pushups 12
how many reps did you finish for squats 30
how many reps did you finish for assisted_pullups 8
how many reps did you finish for rows 10

Workout Summary

Exercise                      reps
--------------------------------------------------
incline_pushups               12
squats                        30
assisted_pullups              8
rows                          10

Total volume is 60
```

---

# Validation Features

The application validates:

- Difficulty selection
- Numeric rep input
- Negative rep values
- Invalid terminal input

The program retries input until valid values are entered.

---

# Architecture Overview

## `forge.py`

Controls application flow:

- user input
- workout logging
- total volume calculation

---

## `workouts.py`

Stores all workout data in structured dictionaries and lists.

---

## `validator.py`

Handles:

- level validation
- rep validation

---

## `formatter.py`

Handles:

- workout formatting
- summary formatting
- output presentation

---

# Future Improvements

- Save workout history to JSON
- Add progressive overload tracking
- Add workout analytics
- Add SQLite database support
- Build FastAPI backend
- Build Streamlit frontend
- Add authentication system
- Add personalized workout generation

---

# Author

Mikey

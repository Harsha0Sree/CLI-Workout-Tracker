from workouts import WORKOUTS


def format_workout(workout):
    print("\nWorkout Summary\n")
    print(f"{'Exercise':<30}reps")
    print("-" * 50)
    for x in workout:
        print(f"{x['name']:<30} {x['reps']} ")


def print_workout(level):
    for x in WORKOUTS[level]:
        print(f"{x['name']:<30}{x['reps']}reps")

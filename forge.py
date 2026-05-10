from formatter import format_workout, print_workout
from validation import validate_level, validate_reps
from workouts import WORKOUTS

completedworkout = []
level = input("whats your level (beginner[b]?intermediate[i]?advaneced[a]?) ")
formaatted_level = level.strip().lower()
totalvol = 0

while not (validate_level(formaatted_level)):
    level = input(
        "INVALID INPUT . whats your level (beginner[b]?intermediate[i]?advaneced[a]?) "
    )
    formaatted_level = level.strip().lower()
print_workout(formaatted_level)


print("\nlets start the workout shall we ?")
for exercise in WORKOUTS[formaatted_level]:
    finished_reps = input(f"how many reps did you finish for {exercise['name']} ")
    while not validate_reps(finished_reps):
        finishedreps = input(
            f"INVALID INPUT . how many reps did you finish for {exercise['name']} "
        )
    total_volume = int(finishedreps) + totalvol

    finished_exercise = {"name": exercise["name"], "reps": finishedreps}
    completedworkout.append(finished_exercise)

format_workout(completedworkout)
print(f"\nTotal volume is {total_volume}")

def validate_level(level):
    valid_inputs = ["b", "i", "a"]
    if level not in valid_inputs:
        return False
    else:
        return True


def validate_reps(reps):
    try:
        converted_reps = int(reps)
        if converted_reps < 0:
            raise ValueError("enter a positive number")
        return True
    except ValueError:
        return False

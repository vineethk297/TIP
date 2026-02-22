def final_value_after_operations(operations):
    if not operations:
        return 0
    tigger = 1

    for operation in operations:
        if operation == "bouncy" or operation == "flouncy":
            tigger += 1
            continue
        if operation == "trouncy" or operation == "pouncy":
            tigger -= 1

    return tigger


operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))

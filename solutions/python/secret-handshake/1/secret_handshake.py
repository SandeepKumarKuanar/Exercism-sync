def commands(binary_str):
    actions = []
    read_steps = list(binary_str[::-1])
    steps = []
    for step in range(0, len(read_steps)):
        # print(step)
        if read_steps[step] == "1" and step == 0:
            actions.append("wink")
        elif read_steps[step] == "1" and step == 1:
            actions.append("double blink")
        elif read_steps[step] == "1" and step == 2:
            actions.append("close your eyes")
        elif read_steps[step] == "1" and step == 3:
            actions.append("jump")
        elif read_steps[step] == "1" and step == 4:
            return actions[::-1]
    return actions
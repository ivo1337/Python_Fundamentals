stops = input()

while True:
    line = input()
    if line == 'Travel':
        break
    command_args = line.split(":")
    command = command_args[0]
    if command == "Add Stop":
        idx = int(command_args[1])
        new_stop = command_args[2]
        if 0 <= idx < len(stops):
            stops = stops[:idx] + new_stop + stops[idx:]
        print(stops)
    elif command == "Remove Stop":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])
        if 0 <= start_idx < len(stops) and 0 <= end_idx < len(stops):
            stops = stops[:start_idx] + stops[end_idx + 1:]
        print(stops)
    elif command == "Switch":
        old_stop = command_args[1]
        new_stop = command_args[2]
        if old_stop in stops:
            stops = stops.replace(old_stop, new_stop)
        print(stops)


print(f'Ready for world tour! Planned stops: {stops}')
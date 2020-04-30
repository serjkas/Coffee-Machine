list_floats = []
while True:
    try:
        list_floats.append(float(input()))
    except ValueError:
        break

print(sum(list_floats) / len(list_floats))

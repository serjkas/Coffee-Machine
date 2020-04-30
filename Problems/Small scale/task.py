list_floats = []
while True:
    try:
        list_floats.append(float(input()))
    except ValueError:
        break
print(min(list_floats))

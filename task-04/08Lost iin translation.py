x = input()
z = []
x_break = 0

for i in range(len(x)):
    if x[i] == "h":
        z.append(x[i])
        x_break = i + 1
        break

for i in range(x_break, len(x)):
    if x[i] == "e":
        z.append(x[i])
        x_break = i + 1
        break

for i in range(x_break, len(x)):
    if x[i] == "l":
        z.append(x[i])
        x_break = i + 1
        break

for i in range(x_break, len(x)):
    if x[i] == "l":
        z.append(x[i])
        x_break = i + 1
        break

for i in range(x_break, len(x)):
    if x[i] == "o":
        z.append(x[i])
        x_break = i + 1
        break

hello = ''.join(str(item) for item in z)

if hello == "hello":
    print("YES")
else:
    print('NO')

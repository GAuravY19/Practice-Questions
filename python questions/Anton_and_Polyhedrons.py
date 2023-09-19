n = int(input())

Tetrahedron = 4
Cube = 6
Octahedron = 8
Dodecahedron = 12
Icosahedron = 20

sum = 0
for i in range(n):
    s = input()
    if s == 'Tetrahedron':
        sum += Tetrahedron
    elif s == 'Cube':
        sum += Cube
    elif s == 'Octahedron':
        sum += Octahedron
    elif s == "Dodecahedron":
        sum += Dodecahedron
    elif s == 'Icosahedron':
        sum += Icosahedron

print(sum)


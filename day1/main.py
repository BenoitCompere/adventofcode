import sys

def main():
    part = sys.argv[1]
    if part == '1':
        from part1 import f1 as f
    elif part == '2':
        from part2 import f2 as f

    totalFuel = 0
    with open('input.txt', 'r') as file:
        for module in file.readlines():
            totalFuel += f(module)
    print(totalFuel)

main()

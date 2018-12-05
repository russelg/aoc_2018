import string


def solve(lines):
    polymer = lines[0].strip()
    alphabet = string.ascii_lowercase

    def react(line):
        while True:
            prev = line
            for l in alphabet:
                line = line.replace(l + l.capitalize(), '').replace(l.capitalize() + l, '')
            if prev == line:
                return len(line)

    print(react(polymer))
    print(min(react(polymer.replace(l, '').replace(l.capitalize(), '')) for l in alphabet))


print('--- test ---')
with open('test.txt') as f:
    lines = f.readlines()
    solve(lines)

print('--- input ---')
with open('input.txt') as f:
    lines = f.readlines()
    solve(lines)

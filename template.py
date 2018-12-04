def solve(lines):
    print(lines)
    pass


print('--- test ---')
with open('test.txt') as f:
    lines = f.readlines()
    solve(lines)

print('--- input ---')
with open('input.txt') as f:
    lines = f.readlines()
    solve(lines)

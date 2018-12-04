from collections import defaultdict, Counter


def most_common(lst):
    lst2 = lst[:]
    data = Counter(lst2)
    return max(lst2, key=data.get)


def solve(lines):
    lines.sort()
    guards = defaultdict(list)
    guard = None
    for line in lines:
        if 'Guard #' in line:
            guard = line.split()[3]
        elif 'asleep' in line:
            guards[guard].append(int(line.split()[1].split(':')[1].replace(']', '')))
        else:
            guards[guard].append(int(line.split()[1].split(':')[1].replace(']', '')))

    max_diff = 0
    maxi = None
    guard_times = defaultdict(int)
    guard_minutes = {}
    guard_commons = {}

    for guard, times in guards.items():
        mins = []
        pairs = zip(times[::2], times[1::2])
        for pair in pairs:
            diff = pair[1] - pair[0]
            guard_times[guard] += diff
            for item in range(pair[0], pair[1]):
                mins.append(item)

        guard_minutes[guard] = mins
        if guard_times[guard] > max_diff:
            max_diff = guard_times[guard]
            maxi = guard

        guard_commons[guard] = Counter(guard_minutes[guard]).most_common()

    maxguard = 0
    maxtimes = 0
    maxmin = 0
    for guard, common in guard_commons.items():
        for minute, occurs in common:
            if occurs > maxtimes:
                maxmin = minute
                maxtimes = occurs
                maxguard = guard

    common = most_common(guard_minutes[maxi])
    print(maxi, common)
    print(maxguard, maxtimes, maxmin)
    print(int(maxi.replace('#', '')) * common)
    print(maxmin * int(maxguard.replace('#', '')))


print('--- test ---')
with open('test.txt') as f:
    lines = f.readlines()
    solve(lines)

print('--- input ---')
with open('input.txt') as f:
    lines = f.readlines()
    solve(lines)

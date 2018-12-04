import collections
import difflib

with open('input.txt', 'r') as f:
    lines = f.readlines()
    two = 0
    three = 0
    for line in lines:
        chars = collections.defaultdict(int)
        for letter in line:
            chars[letter] += 1

        added_two = False
        added_three = False
        for char in chars.keys():
            if chars[char] == 2 and not added_two:
                two += 1
                added_two = True
            if chars[char] == 3 and not added_three:
                three += 1
                added_three = True

    checksum = two * three
    print(f'two: {two}, three: {three}, checksum: {checksum}')

    # part 2
    found = False
    correct = ""
    for a in lines:
        for b in lines:
            if not found:
                a = a.strip()
                b = b.strip()
                position = 0
                diffs = list(difflib.ndiff(a, b))
                if len(diffs) == len(a) + 1:
                    found = True
                    for s in diffs:
                        if s[0] == ' ':
                            correct += s[2]
                    break
    print(correct)

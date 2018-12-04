import collections

freq = 0
seen_freqs = collections.defaultdict(int)

def calc_freq(line):
    freq = 0

    if line[0] == '+':
        freq += int(line[1:])
    else:
        freq -= int(line[1:])

    return freq

with open('input.txt', 'r') as f:
    lines = f.readlines()
    seen = False
    while not seen:
        for line in lines:
            freq += calc_freq(line)
            seen_freqs[freq] += 1
            if seen_freqs[freq] > 1:
                seen = True
                print('seen: ', freq)
                break

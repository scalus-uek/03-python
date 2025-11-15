###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#

PROGRAM_TIMES = {'j': 40, 'u': 70, 's': 20}

total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

p = program.strip().lower()
if p in PROGRAM_TIMES:
    total_washing_time = PROGRAM_TIMES[p]
else:
    print('Unknown program selected, defaulting to shoes (20 minutes)')
    total_washing_time = PROGRAM_TIMES['s']

if extra_rinse.strip().lower() == 'y':
    total_washing_time += 15
if extra_spin.strip().lower() == 'y':
    total_washing_time += 9

print(f'Total washing time: {total_washing_time} minutes')

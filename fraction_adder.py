def parse_fractions(addends):
    numerators, denominators = [], []
    for fraction in addends:
        numerator, denominator = map(int, fraction.split('/'))
        numerators.append(numerator)
        denominators.append(denominator)
    return numerators, denominators

def find_lcm(addends):
    denominators = parse_fractions(addends)[1]
    step = min(denominators)
    print(' (step is {0})'.format(step))
    for i in range(0, 100000000000, step):
        if i == 0:
            continue
        for denominator in denominators:
            if i % denominator != 0:
                break
        else:
            break
    return i

def normalize(addends):
    lcm = find_lcm(addends)
    numerators, denominators = parse_fractions(addends)
    denominator_multipliers = [lcm/denominator for denominator in denominators]
    new_numerators = [i*j for i, j in zip(numerators, denominator_multipliers)]
    return ['{0:.0f}/{1:.0f}'.format(new_numerator, lcm) for new_numerator in new_numerators]

def add_fractions(addends):
    print('Adding {0} to {1}'.format(*addends), end='')
    normalized_addends = normalize(addends)
    numerators, denominators = parse_fractions(normalized_addends)
    numerator_sum = sum(numerator for numerator in numerators)
    fraction_sum = '{0:.0f}/{1:.0f}'.format(numerator_sum, denominators[0])
    return simplify_fraction(fraction_sum)

def simplify_fraction(fraction, start=0, step=1):
    print('Simplifying: {0} (step is currently {1})'.format(fraction, step))
    numerator, denominator = map(int, fraction.split('/'))
    for i in range(start, denominator//2, step):
        if i == start or i == 1:
            continue
        if numerator % i == 0 and denominator % i == 0:
            start, step = i, i
            return simplify_fraction(fraction, start, step)
    lcd = step
    return '{0:.0f}/{1:.0f}'.format(numerator/lcd, denominator/lcd)

if __name__ == '__main__':
    addends = [
        '1/6',
        '3/10',
    ]
    simplify_fraction('50/500')
    fraction_sum = '0/1'
    for fraction in addends:
        fraction_sum = add_fractions([fraction_sum, fraction])
        print('\n')
    print(fraction_sum)

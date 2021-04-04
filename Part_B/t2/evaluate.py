def evaluate(string):
    n = ''
    total = 0

    for i in range(0, len(string)):
        s = string[i]
        op = ['-','+',' ']

        if s.isnumeric() == False and s not in op:
            raise Exception("string cannot be evaluated")
            return 0

        if s.strip() == '':
            continue
        n += s
        if s.isnumeric():
            #following the example of 1+1+1-1 = 3
            #else, remove this if conditional
            if len(n) == 2:
                if n[0] =='-':
                    n = ''
                    continue
            total += int(n)
            n = ''
    return total

def testEvaluate():
    strings = [
        '1+1+1-1',
        '-1+2+3-1',
        '+2+4',
        '5 + 5',
        '1*2'
    ]
    for s in strings:
        print(s.ljust(10),':',evaluate(s))

testEvaluate()

# NOTE: Make distribution more intentional
import random
import json

p = json.load(open('weights.json', 'r'))
length = 500 # words and punctuation
# Length of longest sentence, in words & punctuation
MAX_CHAIN = 60

def returnRand(pgroup):
    if len(pgroup) == 1:
        return list(pgroup.keys())[0]
    q = random.uniform(0, 1)
    cumulativeProb = 0.0
    for key in pgroup:
        cumulativeProb += pgroup[key]
        if q <= cumulativeProb:
            return key

# Start output with post-period lexemes
output = returnRand(p['.']) + ' '
for i in range(0, length - 1):
    ls = output.split('.')[-1].strip()
    if ls in p:
        output += returnRand(p[ls]) + ' '
    else:
        warr = ls.split(' '); warr.pop(0)
        frag = ' '.join(warr)
        i = 0
        while len(frag) > 0 and i < MAX_CHAIN:
            warr = frag.split(' '); warr.pop(0)
            frag = ' '.join(warr)
            i += 1
        if frag in p:
            output += returnRand(p[frag]) + ' '
        else:
            output += '. ' + returnRand(p['.']) + ' '
# Output should be piped to a file
print(output)

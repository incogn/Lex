import re
import json
# Maximum word chain detection length. See: https://github.com/incogn/Lex/Wiki
MAX_LENGTH = 3
# Count proceeding occurences of words
def addLex(lex, nlex):
    global p
    if not lex in p:
        p[lex] = {nlex : 1}
    elif not nlex in p[lex]:
        p[lex][nlex] = 1
    else:
        p[lex][nlex] += 1

p, f, = {}, open('source.txt', 'r', encoding='utf-8')
for line in f:
    # Remove quotation marks, for now
    line = re.sub(r'"', '', line)
    # Remove newlines and spaces
    line = re.sub(re.compile('\s+', re.UNICODE), ' ', line)
    line = line.strip(' \t\n\r')
    if len(line) > 0:
        # Add spaces to punctuation
        line = re.sub(r'([^ ]+)(,|;|!|\?|\.)', r'\1 \2', line)
        arr = line.split(' ')
        # Add lexeme patterns up to MAX_LENGTH
        for i in range(0, len(arr) - 1):
            addLex(arr[i], arr[i + 1])
        for x in range(2, MAX_LENGTH + 1):
            for i in range(0, len(arr) - x):
                words = []
                for j in range(i, i + x):
                    words.append(arr[j])
                addLex(' '.join(words), arr[i + x])
# Crunch the probabilities to decimals for faster processing
for pgroup in p:
    total = 0
    value = p[pgroup]
    for key in value:
        total += value[key]
    for key in value:
        value[key] /= total
# Write weights object to file
with open('weights.json', 'w') as w:
    json.dump(p, w)

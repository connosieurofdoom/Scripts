import re
with open("text.txt", 'r+', encoding="UTF-8") as f:
    t = f.read()
    t = re.sub('\[\d?\]','', t)
    t = re.sub('-\n', '', t)
    t = re.sub('\n' ,' ', t)
    t = re.sub('[.,]', '', t)
    t = re.sub(' +', ' ', t)
    t = re.sub('-', ' ', t)

    with open("output.txt", 'w', encoding="UTF-8") as w:
        w.write(t)

t2 = t.split(' ')
print(len(t2))

file = open('I-1.tsv', 'r', encoding="utf-8")
lines = file.readlines()
base_num = 0


def insert_emdash_or_not(literal):
    if literal == 'n.i.' or literal == ' n.i.' or literal == 's.t.' or literal == ' s.t.':
        literal = '&mdash;'
        return literal
    else:
        return literal

f = open('I-1.md', 'w', encoding='utf-8')

for line in lines:
    line = line.rstrip()
    cols = line.split('\t')

    schwab = cols[0]
    ref_num = cols[1]
    auteur = insert_emdash_or_not(cols[2])
    titre = insert_emdash_or_not(cols[3])
    try:
        pub_date = cols[4]
    except:
        pub_date = '&mdash;'

    if ref_num != base_num:
        f.write('.\n\n')
        f.write(f'{ref_num}.&nbsp;{auteur}, *{titre}*, {pub_date}.&nbsp;{schwab}')
    else:
        f.write(f' {schwab}')
    base_num = ref_num

f.close()
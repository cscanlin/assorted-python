with open('table_text.txt', 'r') as f:
    table_text = f.readlines()
print(table_text)

users = {}
for line in table_text:
    username = line[line.find("(")+1:line.find(")")]
    submits = True if line.split('|')[3] != '\n' else False
    users[username] = submits

with open('ss_users.txt', 'w') as out:
    out.writelines([un + '\n' for un, submits in users.items() if submits])
    out.write('\n')
    out.writelines([un + '\n' for un, submits in users.items() if not submits])

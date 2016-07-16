import hashlib, sys
m = hashlib.md5()
hash = ""
hashs = "db-conversions-raw.csv"
emails = "emails.txt"
outputfile =  output_file = open("db-conversions-output.csv", 'w+')

try:
	hashfile = open(hashs,"r")
except IOError:
	print ("Invalid file.")
	raw_input()
	sys.exit()
else:
	pass

try:
	emailfile = open(emails,"r")
except IOError:
	print ("Invalid file.")
	raw_input()
	sys.exit()
else:
	pass

for hashline in hashfile:
    hashline = hashline.replace('\n', '').replace('\r','')
    hash = hashline.split(",")[0]
    print(hash)
    for email in emailfile:
        email = email.replace('\n', '').replace('\r','')
        m = hashlib.md5()
        m.update(email)
        word_hash = m.hexdigest()
        if word_hash == hash:
            print("found match with: " + email)
            outputfile.write(hashline + "," + email + "\n")
            outputfile.flush()
            break
    emailfile.seek(0)

outputfile.close()
emailfile.close()
hashfile.close()
print("finished!")
sys.exit()

# import csv
#
# #split file into a list called lines,
# #with each element of the list an individual line
# with open('input.txt') as f:
#     lines = f.readlines()
#

# field_1 = lines[2]
# field_2 = lines[3]
# field_3 = lines[0]
# field_4 = lines[1]
# # etc.....
#
# # combine the fields into a list how you want
# row = [field_1,field_2,field_3,field_4]
#
# # write the row to a csv
# with open('output.csv', 'wb') as o:
#     writer = csv.writer(o)
#     writer.writerow(row)
#

import csv

# open the text output file
text_file = open("newfile.txt", "w")

# open the csv
with open('csvfilename.csv', 'rb') as f:
    reader = csv.reader(f)
    # iterate through each row of the file
    for row in reader:

        # fill in fields how you want in a list called row_list, in whatever order you want.
        # index starts at 0 so the first column in each row is row[0]
        # note that the line splits here are for code readability only.
        row_list = [
            row[2],
            row[3],
            '',  # blank line
            row[0],
            '',
            row[1],
            # etc.....
        ]

        # change the list to a string where each element is split by the newline char (\n)
        string_to_write = '\n'.join(row_list)

        # write the text to the file
        text_file.write(string_to_write)

# close text output file. Input file does not need to be closed
# because we used the "with" statement there
text_file.close()

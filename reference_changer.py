#Changes:
#  OFFSET(B2,0,4)
#To:
#  INDIRECT("'New Matrix'!$F$" & ROW($A2))


import string
from itertools import combinations_with_replacement as cwr
alphabet = string.ascii_lowercase
length = 2
alpha1 = ["".join(letter) for letter in string.ascii_lowercase]
alpha2 = ["".join(comb) for comb in cwr(alphabet, length)]

extended_alphabet = alpha1+alpha2

string = r'IF(ISBLANK(OFFSET(B2,0,4)),"",OFFSET(B2,0,4)&"?"&"utm_source=facebook&utm_medium="&IF(OR(OFFSET(B2,0,13)="des",OFFSET(B2,0,13)="mob",OFFSET(B2,0,13)="mob-tab",OFFSET(B2,0,13)="a",OFFSET(B2,0,13)="mob-all"),"pla","banr")&"&utm_term="&SUBSTITUTE(LOWER(AlphaNumericOnly(SUBSTITUTE(SUBSTITUTE(SUBSTITUTE(OFFSET(B2,0,19),"e","e"),"&","and"),"+","and")))," ","_")&"&utm_content="&OFFSET(B2,0,17)&"&utm_campaign="&OFFSET(B2,0,2)&"&db_dest="&OFFSET(B2,0,21)&"&db_unit=d&db_cid=60&db_terms="&OFFSET(B2,0,23)&"-"&OFFSET(B2,0,24)&"&db_class="&IF(OR(OFFSET(B2,0,13)="des",OFFSET(B2,0,13)="banr"),"des",OFFSET(B2,0,13))&"&db_seg="&OFFSET(B2,0,22)&"&db_sku=&c3ch=Facebook&c3nid="&OFFSET(B2,0,2)&"&db_vref1="&IF(ISBLANK(OFFSET(B2,0,25)),"n",OFFSET(B2,0,25))&"&db_vref2="&IF(ISBLANK(OFFSET(B2,0,26)),"n",OFFSET(B2,0,26))&"&lb=force")'
substring = 'OFFSET'

# for substring in string:
#     print substring

start = string.find('OFFSET')
end = string.find(')', start)
num_reference = string[start+6:end].split(',')[2]
letter_reference = extended_alphabet[int(num_reference)+1]
text_to_replace = string[start:end+1]
print text_to_replace

ind_reference = r'INDIRECT("\'New Matrix\'!${0}$" & ROW($A2))'.format(letter_reference.upper())
print ind_reference


while substring in string:
    start = string.find('OFFSET')
    end = string.find(')', start)
    num_reference = string[start+6:end].split(',')[2]
    letter_reference = extended_alphabet[int(num_reference)+1]
    text_to_replace = string[start:end+1]
    ind_reference = r'INDIRECT("\'New Matrix\'!${0}$" & ROW($A2))'.format(letter_reference.upper())
    print text_to_replace
    print ind_reference
    string = string.replace(text_to_replace,ind_reference,100)
print string

# -*- coding: utf-8 -*-

#Program for Hindi Word Count  
#
# @author Shantipriya Parida 
#



import sys
import re

# separator list

separators = [u"।", u",", u".", u"?", u"-", u"(", u")", u"[", u"]", u"$", u"'", u"`", u"&", u"#", u"%", u"^", u"!", u"~", u"_", u"+", u"/", u":", u";"]

if __name__ == '__main__': 

    if len(sys.argv)<2:
        print("Usage: python hindi_wc.py <infile>")
        sys.exit(1)

fname = sys.argv[1]
f1 = open(fname)

wc = 0
for lineoftext in f1.readlines():

    words=lineoftext.split()
    filt_word_cnt = 0
    
    for chr in words:
        if chr not in separators:
            filt_word_cnt = filt_word_cnt + 1
    wc = wc + filt_word_cnt
print("Total Word Count=",wc)
f1.close()

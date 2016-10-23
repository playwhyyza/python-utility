#translation https://www.facebook.com/pages/Pondloso-Fansub
#create by playwhyyza
#24/10/2016

#sample word = https://กกกกกกกกmega.nz/#!6MYQBCDC!wlBwDqnx3yHCTjwekjWwTpdJwBZlum5hymqXU9Lw1f0

import sys

first_word = "https://mega.nz/#"

next_word = [] #keep word behind sign (#)
full_word = [] #keep full word for export to text

#FT = open("text.txt","r+",encoding="utf-8") # open file with unicode

FT = open(sys.argv[1],"r+") # open file with argument

for line in FT:
    word = (line.split("#"))
    next_word.append(word[1]) # select position of word to append into list next_word

for i in next_word:
    full_word.append(first_word + i)

for i in full_word:
    print (i)

FT.writelines("\n" + "==================Export==================" + "\n")

for i in full_word:
    FT.writelines(i)

FT.close()

#translation https://www.facebook.com/pages/Pondloso-Fansub
#create by playwhyyza
#24/10/2016

#sample word = https://กกกกกกกกmega.nz/#!6MYQBCDC!wlBwDqnx3yHCTjwekjWwTpdJwBZlum5hymqXU9Lw1f0

import sys

count = 0

first_word = "https://mega.nz/#!"

next_word = [] #keep word behind sign (#)
full_word = [] #keep full word for export to text

#FT = open("text.txt","r+",encoding="utf-8") # open file with unicode

# open file with argument

def split_word():
    for line in FT:
        word = line.split("!",1)
        #print (word)
        next_word.append(word[1]) # select position of word to append into list next_word

try:
    FT = open(sys.argv[1],"r+")
    split_word()
except:
    FT = open(sys.argv[1],"r+",encoding="utf-8")
    split_word()

for i in next_word:
    full_word.append(first_word + i)
    print (full_word[count])
    count = count + 1

FT.writelines("\n" + "==================Export==================" + "\n")

for i in full_word:
    FT.writelines(i)

FT.close()

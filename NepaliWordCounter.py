import re
import string

def uniqueNepaliWords(test_file):
    temp=test_file.read()
    temp=temp.translate(temp.maketrans('','',string.punctuation))   #remove punctuation
    temp=re.sub(r"[\b“”‘’•–।br]"," ",temp)          #replace unicode char with single space
    sep_temp=re.sub("\s+"," ",temp).split(" ")      #replace more than one spaces with single space
    uq_words=[]
    occurance=[]
    for i in sep_temp:
        if i not in uq_words:
            uq_words.append(i)
            occurance.append(sep_temp.count(i))
    
    #sorting in ascending order by their occurance
    for i in range(0,len(occurance)-1):
        for j in range(0,len(occurance)-1-i):
            if occurance[j]>occurance[j+1]:
                occurance[j],occurance[j+1]=occurance[j+1],occurance[j]
                uq_words[j],uq_words[j+1]=uq_words[j+1],uq_words[j]
    
    #convert into a dict & write in .txt file
    uWord=dict(zip(uq_words,occurance))
    with open("U_Nepali_words.txt","w",encoding="UTF-8") as op: 
        for word,ocr in uWord.items(): 
            op.write('%s --> %s\n'%(word,ocr))
    op.close()
    test_file.close()

uniqueNepaliWords(open("nepalitext.txt","r",encoding="UTF-8"))
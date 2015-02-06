from bs4 import BeautifulSoup, Tag
import os, sys
import fileinput

f1 = open("training_data.txt", "a")
sentence = []
train_sentence = []
i = 0
doc = []
with open ("gp2012.xml", "r") as f:
    for line in f:
        #sentence.append(line)
        soup = BeautifulSoup(line)
        for word in soup.find_all('w'):
                if word['pos'] == "PM":
                    train_sentence.append("<START> " +word.getText().encode('utf-8')+" <END> ")
                else:
                    train_sentence.append(word.getText().encode('utf-8')+" ")

        if "</sentence>" in line:
            doc.append("".join(train_sentence) + "\n")
            train_sentence = []
            i+=1

        print "length of doc"
        print len(doc)
        if len(doc) == 10000:
            f1.write("".join(doc))
            doc = []

f1.write("".join(doc))
f1.close()

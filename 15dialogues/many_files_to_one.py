import os
import csv
from nltk.tokenize import sent_tokenize
import spacy

def diag_to_file(dialogue: list, filename: int):
    global nlp
    dial_path = os.getcwd() + '\\tagged_diags\\' + str(filename) + ".csv"
    person = ''
    utterances = list()
    tmp = dict()
    s = ''
    for repl in range(len(dialogue)):
        person = 'A' if repl % 2 == 0 else 'B'
        if dialogue[repl][0] == ' ':
            dialogue[repl] = dialogue[repl][1:]
        for utt in sent_tokenize(dialogue[repl]):
            tmp = dict()
            s = ''
            tmp["act_tag"] = ''
            tmp["text"] = utt
            tmp["speaker"] = person
            doc = nlp(utt)
            for token in doc:
                s += str(token) + '/' + str(token.pos_) + ' '
            if len(s) == 0:
                s = './.'
            tmp["pos"] = s
            utterances.append(tmp)
    with open(dial_path, 'w', encoding = "utf-8", newline = '') as fw:
        writer = csv.DictWriter(fw, fieldnames = ["act_tag", "speaker", "pos", "text"])
        writer.writeheader()
        for line in utterances:
            writer.writerow({"act_tag": line["act_tag"], "speaker": line["speaker"], "pos": line["pos"], "text": line["text"]})
    print(dial_path)

dir = os.getcwd() + "\\15diags"
k = 0
nlp = spacy.load("en_core_web_sm")
for i in os.listdir(dir):
    with open(dir + '\\' + i, 'r', encoding = "utf-8", newline = '') as f:
        reader = csv.reader(f, delimiter = ',')
        for row in reader:
            k += 1
            diag_to_file(row, k)

import string
from pymystem3 import Mystem
from itertools import groupby
import pymorphy2
from pyaspeller import YandexSpeller
from flashtext import KeywordProcessor
import psycopg2
from correction import correct_message


# Удаление символов пунктуации
def remove_punctuation(text):
       translator = str.maketrans('', '', string.punctuation)
       return text.translate(translator)

# Лемматизация
def diction_form(text):
       text = ''.join(m.lemmatize(text)).rstrip('\n')
       return text

morph = pymorphy2.MorphAnalyzer()
speller = YandexSpeller()
m = Mystem()
synonims = dict()

dbA = []
iterator = 1
for i in range(7):
      dbA.append([])

f = open("final/baseA.txt", 'r', encoding="utf-8")
for line in f:
      if(len(line) == 2):
            iterator = int(line[0])
            continue
      line = line.rstrip('\n')
      dbA[iterator - 1].append(line)
f.close()

db = []
iterator = 1
for i in range(7):
      db.append([])

f = open("final/baseQ.txt", 'r', encoding="utf-8")
for line in f:
      if(len(line) == 2):
            iterator = int(line[0])
            continue
      line = line.rstrip('\n')
      db[iterator - 1].append(line)
f.close()


necessary_part = {"NOUN", "VERB", "INFN"}
keyword_processor = KeywordProcessor()
_question = []
for i in range(0, len(db)):
      for j in range(len(db[i])):
            db[i][j] = correct_message(db[i][j])


            #question = db[i][j].split()
            #question.sort()
            #question = [el for el, _ in groupby(question)]
            #for el in question:
            #      p = morph.parse(el)[0]
            #      if p.tag.POS in necessary_part and p.normal_form not in _question:
            #            _question.append(p.normal_form)
            #question = _question       

#for i in range(len(question)):
      #msg = []
      #msg.append("хуй" + str(i))
     # msg[0] = str(msg[0]).lower().replace("ё", "е")
    #  msg[0] = speller.spelled(msg[0])
   #   msg[0] = remove_punctuation(msg[0].lower())
  #    msg[0] = diction_form(msg[0])
#      synonims[str(question[i])] = i


#for key in synonims:
#   print(key)
f = open("baseNew.txt", 'a', encoding="utf-8")
for i in range(len(db)):
      f.write(str(i + 1) + '\n')
      for j in range(len(db[i])):
            f.write(db[i][j] + '\n')
f.close()

#keyword_processor.add_keywords_from_dict(synonims)
#content = input("Введи хуй")
#new_content_1 = keyword_processor.replace_keywords(content)
#print(new_content_1)
#print(synonims)



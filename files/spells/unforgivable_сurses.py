#В модулі unforgivable_сurses створіть функцію avada_kedavra. Ця функція має видаляти всі дерикторії в кожному з фільмів котрі не містять в собі нагород. Наприклад пуста дерикторія літери Z.

import os
import shutil
os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/Harry Potter/")

def func_del_empty():
    for i in os.listdir():
      os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/Harry Potter/"+str(i))
      for q in os.listdir():
        os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/Harry Potter/"+str(i)+"/"+str(q))
        if len(os.listdir()) == 0: # Check if the folder is empty
            shutil.rmtree("D:/Users/dn300990ssk/PycharmProjects/hillel_git/Harry Potter/"+str(i)+"/"+str(q))
func_del_empty()

#В модулі unforgivable_сurses створіть функцію imperius. Функція відкриває файл json в якому було збережено словник films_awards та зміню type кожної нагороди на "Winner"

import json
from pprint import pprint
os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/")

def imperius():
    with open('films_awards_json.json', 'rt') as f:
        data = json.load(f)
    for i in range(len(data[0]['results'])):
        if data[0]['results'][i]['type'] == "Nominee":
            data[0]['results'][i]['type'] = "Winner"
    pprint(data[0]['results'])
imperius()



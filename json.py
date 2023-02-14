from script_homework_prew import films_awards
import json
from pprint import pprint

films_awards_json = json.dump(films_awards, hsin_file)
os.chdir("D:/Users/dn300990ssk/PycharmProjects/hillel_git/")
json_file = open('films_awards_json.json', 'w')
json_file.write(films_awards_json)
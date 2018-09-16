import json
import os

with open('config.json') as data_file:    
 data = json.load(data_file)
print(data["test"]["name"])
string = data["test"]["description"]
print(string)
print("-"*int(len(string)))
print("Press 'Enter' to continue...")
input()
os.system("cls")
i = 1
accepts = 0
count = data["test"]["question_count"]
while i <= count:
 print(data["question_"+str(i)]["description"])
 print(data["question_"+str(i)]["answers"])
 user_input = input(">")
 if user_input in data["question_"+str(i)]["acceptable"]:
  accepts = accepts + 1
 i = i + 1
print("-"*7) 
print("Правильных ответов: "+str(accepts))
results = data["results"]
if str(accepts) in results:
 print("Результат: "+results[str(accepts)])
os.system("pause")
 
 
 

# improving the code program135.py
import csv

name = input("What's your name?")
age = input("what's you age?")

with open("file/place#1.csv","a") as file:
    writer = csv.DictWriter(file,fieldnames=["name","age"])
    writer.writerow({"name":name,"age":age})
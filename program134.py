import csv

name = input("What's your name?")
age = input("what's you age?")

with open("file/place.csv","a") as file:
    writer = csv.writer(file)
    writer.writerow([name,age])
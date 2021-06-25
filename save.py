import csv

def save_to_file(jobs) :
  file = open(f"{brand}.csv", mode="w")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "regdate"])
  for j in jobs :
    writer.writerow(j)
  return

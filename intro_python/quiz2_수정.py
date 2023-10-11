from random import *
import random
import csv

#로또.csv
def lotto():
    lotto_list = random.sample(range(1,46),7)
    return lotto_list


num_list =[]
lotto_dict = {}
for i in range(1, 101):
    temps = lotto()
    for j in range(7):
        num_list.append(temps[j])
    temps = str(temps).replace('[', '').replace(' ', '').replace(']', '')
    lotto_dict.__setitem__(i,temps )
print(lotto_dict)
file = open('로또결과.csv', 'w')
with open("로또결과.csv", 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['No','Number1','Number2','Number3','Number4','Number5','Number6','Bonus'])
    for i in lotto_dict:
        file.write(f'{i},{lotto_dict[i]}\n')
file.close()


#빈도.csv



num_count_dict = {}

for i in range(1,46):
    num_count_dict[i] = num_list.count(i)


with open('빈도.csv', 'w', newline = '') as file_w:
    writer = csv.writer(file_w)
    writer.writerow(["Num", "Frequency"])
    for i in num_count_dict:
        file_w.write(f'{i},{num_count_dict[i]}\n')

file_w.close()




    



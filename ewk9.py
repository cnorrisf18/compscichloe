from heapq import nlargest
import os
print(os.path.abspath(os.curdir))

sonnets=open(r"C:\Users\chloe\PycharmProjects\CompSci\sonnets", 'r')
total_words=0
word_list=[]
word_dict={}
sonnets=sonnets.read()
sonnets=sonnets.split(' ')
for words in sonnets:
    word_list=word_list + [words]
    word_dict[words]=word_list.count(words)
    total_words=total_words+1


ten_largest=nlargest(11, word_dict, key=word_dict.get)
del ten_largest [0]
print(ten_largest)

percent_list=[]
for num in ten_largest:
    amount=word_dict.get(num)
    decimal=amount/total_words
    percent= decimal * 100
    percent='{0:.2f}'.format(percent)
    percent_list=percent_list+[percent]

print(percent_list)
print_list=['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
pos=0
for num in range(10):
    print("The {} most common word is {}, and it appears {} percent of the time.".format(print_list[pos], ten_largest[pos], percent_list[pos]))
    pos=pos+1





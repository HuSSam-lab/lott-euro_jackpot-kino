import math
import random
import goto
import numpy as np


# selecting random number from the group
def choos(l):
    """This finction is taking list and return random number """
    return random.choice(l)


# number of numbers
num_number = int(input("Enter The total numbers you want then press enter!"))
numbers = []

# numbers
for _ in range(num_number):
    numbers.append(int(input("<-->")))

# number of random groups
num_rand = int(input("Enter how much Random Group You Want To generate:"))
randoms = []

# length of random group
len_random_group = int(input("Enter The length For Each Group:"))

# ('here')
for _ in range(num_rand):
    r = []
    p = list(numbers)
    for i in range(len_random_group):
        temp = choos(p)
        r.append(temp)
        p.remove(temp)
    randoms.append(r)


# print(randoms)
uni_randoms = np.unique(randoms, axis=0)


duplicated_num = len(randoms)-len(uni_randoms)
# print("Agenda:","\nNumber of Total groups are:  ",len(randoms),
#       "\nNumber Of Duplicated group are:  ",duplicated_num,
#       "\nNumber of uniqe group are:  ",len(uni_randoms))


while duplicated_num >= 1:
    r = []
    p = list(numbers)
    for i in range(len_random_group):
        temp = choos(p)
        r.append(temp)
        p.remove(temp)

    t_uni_randoms = np.array(uni_randoms)
    t_uni_randoms = np.append(t_uni_randoms, [r], axis=0)
    t_uni_randoms = np.unique(t_uni_randoms)

#     print(uni_randoms,t_uni_randoms)

    if len(uni_randoms) != len(t_uni_randoms):
        duplicated_num -= 1
        uni_randoms = np.append(uni_randoms, [r], axis=0)

#     uni_randoms=np.unique(randoms,axis=0)
#     duplicated_num=len(randoms)-len(uni_randoms)


t_f_uni_randoms = []
if (num_rand*len_random_group) < num_number:

    #     for _ in range(len(uni_randoms)):
    #         a=uni_randoms[[_]]
    #         b=uni_randoms[[_+1]]
    #         print(np.intersect1d(a,b))
    tt = uni_randoms.flatten()
    Z = (tt.all() == np.unique(tt).all())
    if Z:
        goto("here")


else:
    print(uni_randoms)

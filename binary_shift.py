import sys
sys.setrecursionlimit (11000)

import random as rand #

# lil = list( rand.randint(0,100) for x in range(10))
# print (lil)

# aList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def sequenceShift(seq, n = 0):
    print(len(seq))
    a = n % len(seq)
    print(a)
    return seq[-a:] + seq[:-a]

def recurcieveShift(seq, n = 0):
    if n == 0:
        return seq
    seq.insert(0,seq.pop())
    recurcieveShift(seq, n - 1)
    return seq

# list = list(range(100))
# print(list)

# recurcieveShift(list, 50)
# print(list)


# def shift(aList):
#     n = len(aList)
#     for i in range(len(aList)):
#         print(aList[i])
#         if aList[i] != aList[n-1]:
#             aList[i] = aList[i+1]
#             return aList
#         elif aList[i] == aList[i-1]:
#             aList[i] = aList[0]
#             return aList

# result = shift(aList)
# print(result)

# seqReult = sequenceShift(aList, 2)
# print(seqReult)

# # list_2 = rotate(aList)
# # print(list_2)
# # aList.insert(0, aList.pop())
# # print(aList)

# result = recurcieveShift(aList, 3)
# print (result)
from test import tests
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case
# print(tests)
test = {
    'input': {
        'card': [1, 2, 3, 4, 5, 6, 7, 8, 9],
        'query': 5
    },
    'output': 4
}

def binSearch(card, query):
    lo, hi = 0, len(card)-1
    print('lo :' , lo , ' hi :' , hi)

    while lo <= hi:
        mid = (lo + hi) // 2
        print('mid :' , mid)
        mid_number = card[mid]

        if mid_number == query:
            return mid
        elif mid_number > query:
            lo = mid + 1
        elif mid_number < query:
            hi = mid -1
    return -1
    
print(tests[7]) 
cards1 = tests[7]['input']['cards']
query1 = tests[7]['input']['query']
print(query1)
print(cards1)
result = binSearch(cards1, query1)
print(tests[7]['output'])
print (result)
print(result == tests[7]['output'])

evaluate_test_case(binSearch, test)

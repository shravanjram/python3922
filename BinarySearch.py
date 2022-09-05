from jovian.pythondsa import evaluate_test_cases
# from linearSearch import tests


# time = 1.00 'hour'
tests = []

def locate_card(card, query):

    lo, hi = 0, len(card)-1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = card[mid]
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid 
        elif mid_number < query:
            hi = mid -1
        elif mid_number > query:
            lo = mid + 1

    return -1


test = {
    'input': {
        'cards': (13, 11, 18, 7, 4, 3, 0, 1),
        'query': 7 
    },
    'output': 3
}
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 11, 10, 7, 4, 3, 1, 0],
        'query': 1
    },
    'output': 6
})

tests.append({
    'input': {
        'cards': [4, 2, 1, -1],
        'query': 4
    },
    'output': 0
})

tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})

tests.append({
    'input': {
        'cards': [6],
        'query': 6
    },
    'output': 0 
})

tests.append({
    'input': {
        'cards': [9, 7, 5, 2, -9],
        'query': 4
    },
    'output': -1
})

tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})
tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 3
    },
    'output': 7
})

tests.append({
    'input': {
        'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
        'query': 6
    },
    'output': 2
})

# cards2 = tests[2]['input']['cards']
# query2 = tests[2]['input']['query']
# result = locate_card(cards2, query2)
# print(result)
# output2 =tests[2]['output']
# print(result == output2)

evaluate_test_cases(locate_card, tests)
    
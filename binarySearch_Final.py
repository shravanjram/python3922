from test import tests
from jovian.pythondsa import evaluate_test_cases, evaluate_test_case

def binary_search(lo, hi, condition):

    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid 
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1

def locate_card(cards, query):
    print(cards, query)
    def condition(mid):
        if cards[mid] == query :
            if mid > 0 and cards[mid -1] == query :
                return 'left'
            else :
                return 'found'
        elif cards[mid] < query :
            return 'left'
        else:
            return 'right'
    return binary_search(0 , len(cards) - 1, condition)

evaluate_test_cases(locate_card, tests)
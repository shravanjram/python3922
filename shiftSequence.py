

STests = []
test0 = {
    'input': {
        'nums': [19, 25, 29, 30, 3, 6, 7, 9, 11, 14]
    },
    'output': 4
}

test1 = {
    'input': {
        'nums': [8, 9, 1, 2, 3, 4, 5, 6]
    },
    'output': 2
}

test2 = {
    'input': {
        'nums': [10, 11, 12, 1, 3, 4, 5, 6, 7, 9]
    },
    'output': 3
}

test3 = {
    'input': {
        'nums': [10, 100, 0, 1, 9]
    },
    'output': 2
}

test4 = {
    'input': {
        'nums': [2, 4, 6, 8, 10, 12, 14, 116]
    },
    'output': 0
}

test5 = {
    'input': {
        'nums': [2, 3, 4, 5, 6, 7, 8, 9, 1]
    },
    'output': 8
}

test6 = {
    'input': {
        'nums': [10, 1, 2, 3]
    },
    'output': 1
}

test7 = {
    'input': {
        'nums': list(range(10000, 0, 1))
    },
    'output': 0
}

tests = [test0, test1, test2, test3, test4, test6, test7]
Stests = tests
# print(Stests)
def count_rotation(nums):
    def condition(mid , lo , hi):
        if nums[mid] > nums[hi]:
            mid = hi
    return mid
    
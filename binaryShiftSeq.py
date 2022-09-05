from binary_shift import recurcieveShift
from shiftSequence import Stests as tests
from jovian.pythondsa import evaluate_test_case, evaluate_test_cases


# print(tests)

def count_rotatons(nums):
    position = 0
    while position < len(nums) - 1 :
        if position > 0 and nums[position] < nums[position - 1]:
            return position 
        position += 1
    return 0


def binary_search(lo, hi, condition):

    while lo < hi:
        mid = (lo + hi)// 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else :
            lo = mid + 1
    return 0


def bin_count_rotation(nums):
    lo = 0
    hi = len(nums) - 1
    def condition(mid):
        if nums[mid] != 0:
            if mid > 0 and nums[mid - 1] > nums[mid]:
                return 'found'
        elif nums[mid] > nums[mid - 1]:
            return 'right'
        else:
            return 'left'
    return binary_search(lo, hi, condition)

def count_rotations_binary(nums):
    lo = 0
    hi = len(nums)-1
    def conditon(lo, hi):
        pass
    while lo < hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and mid_number < nums[mid -1]:
            # The middle position is the answer
            return mid
        
        elif mid_number < nums[hi] :
            # Answer lies in the left half
            hi = mid  
        else:
            # Answer lies in the right half
            lo = mid
    
    return 0
    
evaluate_test_cases(count_rotations_binary, tests)

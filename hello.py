from collections import OrderedDict

def pairSum(arr, s):
    n = len(arr)
    print(f"the length of the array is {n}")


    # Map to store frequency of elements.
    map = OrderedDict()
    print(f"the frequency of elements is {map}")
    # This will store the result.
    ans = []
    print(f"the ans of the array is {ans}")
    for ele in arr:
        count = map.get(s - ele, 0)
        print(count)
        pair = [-1 for i in range(2)]
        pair[0] = ele
        print(pair[0])
        pair[1] = s - ele
        print(pair[1])

        while count > 0:
            ans.append(pair)
            count -= 1

        map[ele] = map.get(ele, 0) + 1

    # This will store the final result.
    res = [[-1 for j in range(2)] for i in range(len(ans))]

    # Sorting the 'ans' array element.
    for i in range(len(ans)):
        a = ans[i][0]
        b = ans[i][1]
        res[i][0] = min(a, b)
        res[i][1] = max(a, b)
        
    # Finally sorting each pair in 'res'.
    res = sorted(res, key=lambda x: x[0])

    return res




all= [1, 2, 3, 4, 5, 6, 7, 8, 9]
s=5
p1 = pairSum(all, s)
print(p1)
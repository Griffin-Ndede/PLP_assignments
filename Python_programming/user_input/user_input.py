# # class Solution:
# #     def twoSum(self, nums: List[int], target: int) -> List[int]:
# #         pass
# # from itertools import permutations

# # target = 9
# # num = [1, 2, 3, 4, 5]
# # perm = list(permutations(num, 2))
# # result = [(i, j, num.index(i), num.index(j)) for i, j in perm if i + j == target]

# # print(result)

# my_list = ['apple', 'banana', 'orange', 'grape']

# for index, item in enumerate(my_list):
#     print(index, item)


# loop

list = [-2,1,-3,4,-1,2,1,-5,4]
sublists = []
n = len(list)
sums_sublist = []
s
for start in range(n):
    for end in range(start + 1, n+1):
        sublists.append(list[start:end])
for sublist in sublists:
    sums_sublist = sum(sublist)
    print (sums_sublist)
print (type(sums_sublist))

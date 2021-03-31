# filter
# 表示过滤为真的元素
from functools import reduce

nums = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, nums)))

# map 表示映射
# 将一个苹果映射与另外一种物体
nums = [1, 2, 3, 4, 5]
print(list(map(str, nums)))

# reduce  a ,b -> ab
# 两个参数变成一个
nums = [1, 2, 3, 4, 5]
print(reduce(lambda x, y: x * 10 + y, nums))

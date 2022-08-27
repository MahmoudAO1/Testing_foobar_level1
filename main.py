

def solution(data, n):
    # Your code here
    if len(data) > 100:
        return False
    data_mod = data.copy()
    for number in set(data):
        data_loop = data.copy()
        count = 0
        while number in data_loop:
            count += 1
            data_loop.remove(number)
        if count > n:
            for _ in range(count):
                print(number)
                data_mod.remove(number)
    return data_mod
data = [5, 10, 15, 10, 7, 5, 15, 63, 9,5 ,57,42,5]
dataa = solution([5, 10, 15, 10, 7, 5, 15, 63, 9,5 ,57,42,5], 2)
print(dataa)
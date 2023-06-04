string = input()
n = int(input())

result = lambda word, times: word * times
print(result(string, n))
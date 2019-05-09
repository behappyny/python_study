file = open('test.txt', 'r')
whole_str = file.read()
print(whole_str)
file.close()
#파일을 열었다면 반드시 닫을 것  

file = open('python.txt', 'r')
whole_str = file.read()
print(whole_str)
file.closer()
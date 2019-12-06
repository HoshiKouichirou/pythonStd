def start():
  index = 0
  b = 1
  a = 1
  print(a)
  print(b)
  for i in range(100):
    print(b + a)
    c = a
    a = b
    b = b + c
start()
# aaa
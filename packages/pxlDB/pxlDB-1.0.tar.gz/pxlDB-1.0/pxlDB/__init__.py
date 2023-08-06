def add_value(value):
  file = open('values.txt', 'a')
  file.write(value)
  
def get_values():
  file = open('values.txt', 'r')
  values = []
  for value in file.read().splitlines():
    values.append(value)
  return values
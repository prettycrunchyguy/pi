i = 1
j = 0
k = 0
digit = "3"
digits = ""
plus = True
while True:
  if (plus):
    j += 4/i
    plus = False
  else:
    j -= 4/i
    plus = True
  print("{} {} {:.30f}".format(digits," ",j))
  if (str(j)[k] == digit):
    k += 1
    digits += digit
  digit = str(j)[k]
  i += 2

def reverse_str(message):
    number_of_text = len(message)
    text = ""
    for i in range(number_of_text):
        number = number_of_text - i - 1
        text += message[number]
    return text

def from_base(b):
    ret = 0
    fstbase = int(input("Please input the current base : "))
    num1 = str(b)
    for i in range (len(num1)):
      x = num1[len(num1) - i - 1].isdigit()
      n = i
      if x == True:
        digit = int(num1[len(num1) - i - 1])
      else :
        asc = int(ord(num1[len(num1) - i - 1]))
        digit = int(asc-55)
      ensemble = digit * (fstbase**n)
      ret += ensemble
    return ret

def change_into_number(a):
  base = int(input("Please input base that you want the number to be : "))
  output = ""
  total = a
  while total > 0:
    remainder = total % base
    total = int((total - remainder) / base)
    if remainder > 9:
      number = (remainder - 9) + 64
      remainder = chr(number)
    
    output += str(remainder)
  output = reverse_str(output)
  return output
    
while True:
    text = input("Please put in your number : ")
    if text == "exit":
        break
    else:
        basetennum = from_base(text)
        num = int(basetennum)
        base = change_into_number(num)
        print(base)

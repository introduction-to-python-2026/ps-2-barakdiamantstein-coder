def find_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
      return num1 
    elif num2 > num1 and num2 > num3:
      return num2
    elif num3 > num1 and num3 > num2:
      return num3
    elif num1 == num2 or num1 == num3:
      return num1
    else:
      return num2


def find_mean(num1 , num2 , num3):
  return (num1 + num2 + num3)/3

def find_mean_std(num1 , num2 , num3):
  mean = (num1 + num2 + num3)/3
  return ((((num1 - mean) ** 2) + ((num2 - mean) ** 2) + ((num3 - mean) ** 2))/3) ** 1/2


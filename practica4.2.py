lista = [3, 1, 4, 7, 2, 8, 9, 11, 10, 71, 0] 

def find_prime(n):
       if n <=1:
         return False
       else:
          for i in range(2, n):
              if n % i == 0:
                  return False
       return True
x = filter(find_prime, lista) 
print(list(x))


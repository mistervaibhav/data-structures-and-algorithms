# Multiply two numbers with recursion, without mathematical operators
from utils.main import timer

@timer
def multiply(x, y):
    
    if y == 0:
        return 0
    
    if y > 0:
        return x + multiply(x, y - 1)
    
    if y < 0:
        return -(x + multiply(x, y - 1))



if __name__ == "__main__":
     print(multiply(300,413))
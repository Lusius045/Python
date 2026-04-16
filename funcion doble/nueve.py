def repetir(num):
    if num > 0:
        print(" ")
        repetir(num-1)
    else:
        return 
    
num = int(input())
repetir(num)
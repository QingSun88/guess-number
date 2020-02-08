import random
start=input('please input the start number:')
end=input('please input the end number')
start=int(start)
end=int(end)
r=random.randint(start,end)
n=0
while True:
    num=input('please guess the number:')
    num=int(num)
    n=n+1
    if num==r:
        print('you are right!')
        break
    elif num>r:
        print('it is bigger than the correct one!')
        print('this is the',n,'times!')
    elif num<r:
        print('it is smaller than the correct one!')
        print('this is the',n,'times!')
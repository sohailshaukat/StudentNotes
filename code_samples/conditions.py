a = int(input())

# def is_even(blyat):
#     return not (blyat % 2 )

is_even = lambda blyat :  not (blyat % 2 )

if is_even(a):
    print("A is even")
else:
    print('A is odd')





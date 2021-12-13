# Hannah Hodges
# CS151, Dr. Rajeev
# Lab 11
# 12/9/2021

def main():
    n = int(input("Enter a number:"))
    binary_search_recursive(n)


def binary_search_recursive(n):
#n has to be greater than 0
    if n <= 0:
        print("N need to be greater than 0")
#base case
    elif n == 0:
        return 1
#the general case
    else:
        return (n * (n-1))


main()

# for function 1 (native recursive fibonacci, 38 is the smallest value that takes at least 5 seconds to run. It take 7.28 seconds to run.
# for function 2 (iterative fibonacci), 600100 is the smallest value of n that takes exactly 5 seconds to run
# for function 3 (recursive binary search), 5500000 is the smallest value of n that takes 5 seocnds to run
# for function 4 (iterative binary search), 879910 is the smallest value of n that takes 5 seconds

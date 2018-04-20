#  https://docs.python.org/3.5/tutorial/controlflow.html

print("for i in range(5,10)...")
for i in range(5, 10):
    print("i=",i)

print()

list_a=['a','b','c']
for i in range(0, len(list_a)):
    print("list_a["+str(i)+"]=\"" +list_a[i] + "\"")

for i in range(len(list_a)):
    print("list_a["+str(i)+"]=\"" +list_a[i] + "\"")

print("range() returns an `iterable`...")

print("range(10)="+str(range(10)))

print("list(range(10)))="+str(list(range(10))))

print()

list_b=['Mary','had','a','little','lamb','it\'s', 'fleece', 'was', 'white', 'as', 'snow', '.']
for i in range(len(list_b)):
    print("list_b["+str(i)+"]=\"" +list_b[i] + "\"")

print()

for i in range(0,len(list_b),2):
    print("list_b["+str(i)+"]=\"" +list_b[i] + "\"")

print("`else` as part of `for` loop...for the \"falls through\" situation...")
# else as part of for loop...for the "falls through" situation...
for n in range(2, 10):
    print("n="+str(n)+"...")
    for x in range(2, n):
        print("\t"+"x="+str(x)+"...")
        if n % x == 0:
            print("\t\t", n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print("\t\t", n, 'is a prime number')


def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n.""" # This is a `docstring`...used to create online documentation...
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()

print('calling fib(2000)...')
fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597

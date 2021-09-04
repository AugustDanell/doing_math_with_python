''' Chapter 1
    #2: Enhanced Multiplication Table Generator
    Our multiplication table generator is cool, but it prints only th first 10 multiples. Enhance the generator so that
    the user can specify both th number and up to which multiple. For example, I should be able to input that I want to
    see a table listing the first 15 multiples of 9.
'''

if __name__ == '__main__':
    f1 = int(input("Enter in the factor you want to generate a multiplication table of: "))
    r1 = int(input("Enter in how many repetitions you want: "))

    for i in range(1,r1+1):
        print("%d x %d = %d" %(f1,i,f1*i))

import cmath
import math
def main():
    global a
    global b
    global c
    print("Quadratic Solver")
    print("The quadratic equation: ax^2 + bx + c = 0")
    print("If you see 'j' in solutions, they mean 'i', or 'imaginary nubmer'.")
    print("To find the common factor of the equation, type '1'.")
    print("To find the solution, type '2'.")
    print("To factorize the equation (ONLY whole numbers), type '3'.")
    choice = input("Enter the number: (1, 2, or 3):")
    a = int(input("Input a:"))
    b = int(input("Input b:"))
    c = int(input("Input c:"))
    if choice == '1':
        common()
    elif choice == '2':
        solve()
    elif choice == '3':
        factor()
    else:
        print("Your choice isn't in the options. How sad.")
	
def common():
    global a
    global b
    global c
    gcd = str(math.gcd(math.gcd(a,b),c))
    a = str(a/int(gcd))
    b = str(b/int(gcd))
    c = str(c/int(gcd))
    print("The factor:" + gcd)
    print("The equation after taking out the factor:" + a + "x^2 + " + b + "x + " + c + " = 0")
	
def solve():
    global a
    global b
    global c
    global one
    global two
    one = str((-b + cmath.sqrt(b**2 - 4 * a * c))/ (2 * a))
    two = str((-b - cmath.sqrt(b**2 - 4 * a * c))/ (2 * a))
    if one != two:
        print("Root 1:" + one)
        print("Root 2:" + two)
    else:
        print("Double Root:" + one)

def factor():
    global one
    global two
    one = str((-b + cmath.sqrt(b**2 - 4 * a * c))/ (2 * a))
    two = str((-b - cmath.sqrt(b**2 - 4 * a * c))/ (2 * a))
    one = one.replace('+0j','')
    two = two.replace('+0j','')
    # If there isn't '+0j' in text, they won't replace it.
    if '+0j' not in one and '+0j' not in two:
        one = one.replace('(','')
        one = one.replace(')','')
        two = two.replace('(','')
        two = two.replace(')','')
        # Same thing - A . means that it is a decimal number - which we don't want. 
        if '.' not in one and '.' not in two:
            one = int(one)
            two = int(two)
            aone = str(abs(int(one)))
            atwo = str(abs(int(two)))
            if one != two:
                if one < 0 and two < 0:
                    print("Factorization: (x + " + aone + ")(x + " + atwo + ") = 0")
                elif one < 0 and two >= 0:
                    print("Factorization: (x + " + aone + ")(x - " + atwo + ") = 0")
                elif one >= 0 and two < 0:
                    print("Factorization: (x - " + aone + ")(x + " + atwo + ") = 0")
                else:
                    print("Factorization: (x - " + aone + ")(x - " + atwo + ") = 0")
            else:
                if one < 0:
                    print("Factorization: (x - " + aone + "^2")
                else:
                    print("Factorization: (x + " + aone + "^2")
        else:
            print("Error - One (or both) of the roots is/are not an interger.")
    else:
        print("Error - One (or both) of the roots is/are not an interger.")

# Main Code
main()

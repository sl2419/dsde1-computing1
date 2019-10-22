import math
def period(length,g):
    if isinstance(length,int)==False|isinstance(g,int)==False:
        print('typeError')
       
    periodd=2*math.pi*(length/g)**1/2
    return periodd


def main():
    a=int(input('length'))
    b=int(input('g'))
    print(period(a,b))

if __name__ == "__main__":
    main()

def period(length,mass):
    if isinstance(length,int)=False|isinstance(mass,int)=False:
        print('typeError') 

    if mass=0:
        print('ValueError')

    import math
    periodd=2*math.pi*(length/mass)**1/2
    print length.isdigit()
    return periodd
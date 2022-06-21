'''
This script validates Iranian security number
'''
# main loop
while True:

    code = input("code melii?")

    #input validator
    for d in code:
        if d not in "0123456789":
            code=""

    if len(code) > 10 or len(code) < 8:
        print("bad input format")
        continue
    
    
    #normalizer
    code = (10-len(code))*"0" + code

    #parser
    d1=int(code[-1])
    d2=int(code[-2])
    d3=int(code[-3])
    d4=int(code[-4])
    d5=int(code[-5])
    d6=int(code[-6])
    d7=int(code[-7])
    d8=int(code[-8])
    d9=int(code[-9])
    d10=int(code[-10])

    #code melli validator

    control= (d2*2 + d3*3 + d4*4 + d5*5 + d6*6 + d7*7 + d8*8 + d9*9 + d10*10) % 11
    if control>1 : control = 11 - control
    if d1==control : print("code validated") 
    else : print("invalid")
    
"""
COSC326 Floating Point Numbers
This program takes a number in IBM format and converts it to IEEE
Authors: Ava Reese, Francesca Totty, Katherine Butt, Matt Dixon
"""

import struct
import math

"""
This section of the code calculates whether or not a value is
positive or negative.
"""

"""
This method is for the IBM32 format
It is for 32 bit long IBM values
"""
def ibm32converter(ibmint,frac):
    #This takes the first 32 bits and converts to a decimal value
    #ibmsign1 = (ibmint >> 31)
    ibmsign = int(str(ibmint)[0])
    exp = bin(ibmint >> 23)
    expstring = "0b" + exp[2:9]
    finalexp = int(expstring,2)-64
    return ibmgenerate32(ibmsign, finalexp, frac)

def ibm64converter(ibmint, frac):
     #This takes the first 32 bits and converts to a decimal value
    ibmsign = (ibmint >> 63)
    #ibmsign = int(str(ibmint)[0])
    exp = bin(ibmint >> 56)
    expstring = "0b" + exp[2:11]
    finalexp = int(expstring,2)-64
    return ibmgenerate64(ibmsign, finalexp, frac)

def ibmgenerate32(sign, exponent, fraction):
    #Used to convert all the alpha hex values to integers
    hexcharvals = {'A':'10', 'a':'10', 'B':'11', 'b':'11', 'C':'12', 'c':'12', 'D':'13', 'd':'13', 'E':'14', 'e':'14', 'F':'15', 'f':'15'}
    power = -1
    frac = 0
    #Generates the fraction
    for x in fraction:
        if(x.isalpha()):
            x = hexcharvals[x]
        if(int(x) == 0):
            power -=1
        else:
            frac += int(x) * 16 ** power
            power -= 1
    return(ie32converter(sign, exponent, frac))

"""
This method is used to work out the floating point value
For double precision inputs
"""
def ibmgenerate64(sign, exponent, fraction):
    #Used to convert all the alpha hex values to integers
    hexcharvals = {'A':'10', 'a':'10', 'B':'11', 'b':'11', 'C':'12', 'c':'12', 'D':'13', 'd':'13', 'E':'14', 'e':'14', 'F':'15', 'f':'15'}
    power = -1
    frac = 0
    #Generates the fraction
    for x in fraction:
        if(x.isalpha()):
            x = hexcharvals[x]
        if(int(x) == 0):
            power -=1
        else:
            frac += int(x) * 16 ** power
            power -= 1
    return(ie64converter(sign, exponent, frac))

"""
Takes a IEEE 32 bit number
Returns a floating point number
If statement check for an infinite input
"""
def ie32converter(sign, exponent, fraction):
    if((exponent == 255) & (fraction !=0)):
        return 0
    elif(exponent > 255):
        temp1 = (-1)**sign * math.inf
        return((-1)**sign * math.inf)
    elif(exponent < 255):
        if(sign == 0):
            sign = -1
        return sign * (fraction) * 16 ** exponent
    else:
        return 0

"""
Takes a IEEE 64 bit number
Returns a floating point number
"""
def ie64converter(sign, exponent, fraction):
    if(exponent > 2047):
        return(-1) ** sign * math.inf
    elif(exponent > 0 & exponent < 2047):
        if(sign == 0):
            sign = -1
        return sign * fraction * 16 ** exponent
    else:
        return 0
"""
Takes inputs with are 32 bits
f is the precision parameter
"""
def floatreader(file_in, file_out, f, o):
    length = 0
    try:
        """
        The b when opening a file indicates binary
        Therefore rb = read binary and wb = write binary
        """
        with open(file_in, "rb") as streamIn:
            with open(file_out, "wb") as streamOut:
                while True:
                    x = streamIn.read(4)
                    if(x):
                        length += 1
                        Y = ""
                        for y in x:
                            if y == 0:
                                Y += "00"
                            else:
                                Y += hex(y)[2:]
                        fraction = Y[2:]
                        reverseY = ""
                        i = len(Y) -1
                        while i > 0:
                            reverseY += Y[i-1:i +1]
                            i -= 2
                        if o == 's':
                            f_point = ibm32converter(int(Y, 16), fraction)
                            #This line formats the string correctly
                            result = struct.pack('f', f_point)
                        else:
                            f_point = ibm32converter(int(Y, 16), fraction)
                            result =  struct.pack('d', f_point)
                        streamOut.write(result)
                    else:
                        break
    except FileNotFoundError:
        print("Input file could not be found")
    if length > 0:
        print("Conversion was successfull")

"""
Takes inputs which are 64 bits
f is the precision paramater
"""
def doublereader(file_in, file_out, f, o):
    length = 0
    try:
        """
        The b when opening a file indicates binary
        Therefore rb = read binary and wb = write binary
        """
        with open(file_in, "rb") as streamIn:
            with open(file_out, "wb") as streamOut:
                while True:
                    x = streamIn.read(8)
                    if(x):
                        #Determines the length of the input
                        length += 1
                        Y = ""
                        #Converting y into hexadecimal format
                        for y in x:
                            if y == 0:
                                Y += "00"
                            else:
                                if(len(hex(y)[2:]) < 2):
                                    Y += "0"
                                Y += hex(y)[2:]
                        fraction = Y[2:]
                        #Reverse the order of the value y
                        reverseY = ""
                        i = len(Y) -1
                        while i > 0:
                            reverseY += Y[i-1:i +1]
                            i -= 2
                        if o == 's':
                            f_point = ibm64converter(int(Y, 16), fraction)
                            #This line formats the string correctly
                            result = struct.pack('f', f_point)
                        else:
                            f_point = ibm64converter(int(Y, 16), fraction)
                            result = struct.pack('d', f_point)
                        streamOut.write(result)
                    else:
                        break
    except FileNotFoundError:
        print("Input file could not be found")
    if length > 0:
        print("Conversion was successfull")

"""
This method is used to determine the type of input
Based of input type different methods are used
"""
def inputtype(userinput):
    userinput = userinput.split(" ")
    if(len(userinput) < 4 or len(userinput) > 4):
        return("Invalid input please try again")
    else:
        file_in = userinput[0]
        file_out = userinput[1]
        f = userinput[2]
        o = userinput[3]

        if(f == 's'):
            return(floatreader(file_in, file_out, f, o))
        elif(f == 'd'):
            return(doublereader(file_in, file_out, f, o))
        else:
            return("Format given is not valid please try again")

if __name__=="__main__":
    userinput = input("Please enter an inputfile, output file, the input file precision(s for single, d for double) and the wanted format for the output file: \n")
    inputtype(userinput)

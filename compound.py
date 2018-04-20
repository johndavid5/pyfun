import sys
#import locale
#locale.setlocale(locale.LC_ALL, 'en_US')

b_debug = 0 

def doIt(s):
    print("%s\t=>\t%s"%(s,numWithCommas(s)))

def testNumWithCommas():
    for i in [0,1,12,123,1234,12345,123456,1234567,12345678,123456789]:
        doIt(i)
        doIt(-1*i)

    mant=0.987654321
    for i in [0,1,12,123,1234,12345,123456,1234567,12345678,123456789]:
        doIt(' + '+str(i+mant))
        doIt(' + '+"%.2f"%(i+mant))
        doIt(-1*(i+mant))

def numWithCommas(x):

    sWho = "numWithCommas"

    if b_debug:
        print(sWho + "(): A: x = " + str(x))
        print(sWho + "(): A: type(x) = ", type(x))

    x_str = str(x);

    if b_debug:
        print(sWho + "(): A: x_str = \"" + x_str + "\"")

    prefix = ""

    if x_str[0] == "-":
        prefix = x_str[0];
        x_str = x_str[1:]; 
    elif x_str[0] == "+":
        prefix = x_str[0];
        x_str = x_str[1:]; 

    if b_debug:
        print(sWho + "(): B: prefix = \"" + prefix + "\"")
        print(sWho + "(): B: x_str = \"" + x_str + "\"")

    #if x < 0:
    #    suffix = "-"
    #    x *= -1

    right = ""
    i_where = x_str.find(".")
    if i_where >= 0:
        # slicing: s = s[ beginning : beginning + LENGTH]
        right = x_str[ i_where : ] 
        x_str = x_str [ 0 : i_where ]

    if b_debug:
        print(sWho + "(): C: right = \"" + right + "\"")
        print(sWho + "(): C: x_str = \"" + x_str + "\"")
     
    x = int(x_str)

    if b_debug:
        print(sWho + "(): D: x = \"" + str(x) + "\"")

    result = ''
    while x >= 1000:
        x, r = divmod(x, 1000)
        result = ",%03d%s" % (r, result)

    if b_debug:
        print(sWho + "(): E: x = " + str(x))
        print(sWho + "(): E: result = \"" + result + "\"")

    s_return = "%s%d%s%s" % (prefix, x, result, right)

    if b_debug:
        print(sWho + "(): F: s_return = \"" + s_return + "\"")

    return s_return

# https://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
#def intWithCommas(x):
#    if type(x) not in [type(0), type(0L)]:
#        raise TypeError("Parameter must be an integer.")
#    if x < 0:
#        return '-' + intWithCommas(-x)
#    result = ''
#    while x >= 1000:
#        x, r = divmod(x, 1000)
#        result = ",%03d%s" % (r, result)
#    return "%d%s" % (x, result)

# main #
print('Number of arguments:', len(sys.argv), 'arguments.')

b_test = 0
PV = 0.0
F = 0.0
N = 0
for i in range(1, len(sys.argv)):
    # i is a number, from 1 to len(sys.argv)-1
    print("sys.argv[%d] = \"%s\"" % (i, sys.argv[i]))
    if sys.argv[i] == "-pv":
        i += 1
        PV = float(sys.argv[i])
    elif sys.argv[i] == "-f":
        i += 1
        F = float(sys.argv[i])
    elif sys.argv[i] == "-n":
        i += 1
        N = int(sys.argv[i])
    elif sys.argv[i] == "-test":
        b_test = 1
    elif sys.argv[i] == "-debug":
        b_debug = 1

#PV = float(sys.argv[1])
#F = float(sys.argv[2])
#N = int(sys.argv[3])

print("PV = %f" % (PV))
print("N = %d" % (N))
print("F = %f" % (F))
print("b_test = %d" % (b_test))

if( b_test ):
    testNumWithCommas();
    exit(0);

FV = PV
for i in range( 1, N):
    FV *= F
    print("i = %d: FV = %15s" % (i, numWithCommas("%.2f" % (FV))))
    #print "i = %d: FV = %13.2f" % (i, FV)
    #print "i = %d: FV = %s" % (i, locale.format("%f", FV, grouping=True))

#####################################
# http://code.activestate.com/recipes/498181-add-thousands-separator-commas-to-formatted-number/
# Code from Michael Robellard's comment made 28 Feb 2010
# Modified for leading +, -, space on 1 Mar 2010 by Glenn Linderman
# 
# Tail recursion removed and  leading garbage handled on March 12 2010, Alessandro Forghieri

def splitThousands( s, tSep=',', dSep='.'):
    '''Splits a general float on thousands. GIGO on general input'''
    if s == None:
        return 0
    if not isinstance( s, str ):
        s = str( s )

    cnt=0
    numChars=dSep+'0123456789'
    ls=len(s)
    while cnt < ls and s[cnt] not in numChars: cnt += 1

    lhs = s[ 0:cnt ]
    s = s[ cnt: ]
    if dSep == '':
        cnt = -1
    else:
        cnt = s.rfind( dSep )
    if cnt > 0:
        rhs = dSep + s[ cnt+1: ]
        s = s[ :cnt ]
    else:
        rhs = ''

    splt=''
    while s != '':
        splt= s[ -3: ] + tSep + splt
        s = s[ :-3 ]

    return lhs + splt[ :-1 ] + rhs

#####################################
if __name__ == "__main__" :
    def doIt(s):
        print "%s\t=>\t%s"%(s,splitThousands(s,','))

    for i in [0,1,12,123,1234,12345,123456,1234567,12345678,123456789]:
        doIt(i)

    mant=0.987654321
    for i in [0,1,12,123,1234,12345,123456,1234567,12345678,123456789]:
        doIt(' + '+str(i+mant))
        doIt(-1*(i+mant))

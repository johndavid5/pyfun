import sys
import re
import logging
import logging.config

DEBUG = True

#logging.config.fileConfig('logging.conf')
# create logger
#logger = logging.getLogger('tcalc')

#logging.setLevel(logging.DEBUG)
#logger.setLevel(logging.DEBUG)

#logging.basicConfig(filename='tcalc.log',level=logging.DEBUG)

def main():
    # terminal-based hours:minutes::seconds time add / subtract calculator
    while 1:
        #sys.stdout.write("tcalc>");
        #line = sys.stdin.readline()
        try:
            s_line = input("tcalc>");
            if( s_line == "quit" ): 
                break
            print("+ " + s_line + " = " + do_line(s_line));
        except EOFError as error:
            # Output expected EOFErrors.
            #print("Got an EOFError:", error)
            print("That's all folks!")
            break
        except Exception as exception:
            # Output unexpected Exceptions.
            print("Got Exception", exception) 
            break

    print("+ Let off some steam, Bennett!")

RE_LINE = re.compile("^(\\d+):(\\d+):(\\d+)\\s*(\\+|\\-|to)\\s*(\\d+):(\\d+):(\\d+)$", re.IGNORECASE)

def do_line(s_line):
    sWho = "do_line" 
    debug_print(sWho + "(): s_line = \"" + s_line + "\"...");
    match = RE_LINE.match(s_line) 
    if( match ):
        debug_print(sWho + "(): SHEMP: match.group(0) = \"" + match.group(0) + "\"...")
        num_groups = len(match.groups())
        groups = match.groups()
        debug_print(sWho + "(): SHEMP: num_groups = " + str(num_groups) + "...")
        debug_print(sWho + "(): SHEMP: groups = \"" + list_to_short_string(groups) + "\"...")
        debug_print(sWho + "(): SHEMP: groups = \n" + list_to_string(groups, "groups","  ") )

        for i in range(0,num_groups+1):
            debug_print(sWho + "(): SHEMP: match.group(" + str(i) + ") = " + match.group(i) + "...")

        hours_a = match.group(1)
        minutes_a = match.group(2)
        seconds_a = match.group(3)

        operator = match.groups(4)

        tot_seconds_a = hms_to_s(hours_a, minutes_a, seconds_a)

        hours_b = match.group(5)
        minutes_b = match.group(6)
        seconds_b = match.group(7)

        tot_seconds_b = hms_to_s(hours_b, minutes_b, seconds_b)

        tot_seconds_op = None

        if( operator == "-" ):
            tot_seconds_op = tot_seconds_a - tot_seconds_b

        [hours_op,minutes_op,seconds_op] = s_to_hms(tot_seconds_op)  
        

    else:
        debug_print(sWho + "(): SHEMP: Sorry, Moe, no match...");
    
    return "???"


def list_to_string(list,name="list", prefix=""):
    s_out = ""

    s_out = name + ": " + str(len(list)) + " item" + ("" if len(list)==1 else "s") + ("." if len(list)==0 else ":")

    for i in range(0,len(list)):
        #if i > 0:
        #    s_out += "\n"
        s_out += "\n"
        s_out += prefix + name + "[" + str(i) + "] = " + str(list[i])
    return s_out

def list_to_short_string(list):
    s_out = ""
    for i in range(0,len(list)):
        if i > 0:
            s_out += ","
        s_out += str(list[i])
    return s_out

def debug_print(msg):
    if DEBUG:
        print("*** " + msg )


# Automatically kick-start main()...
# https://stackoverflow.com/questions/1590608/is-it-possible-to-forward-declare-a-function-in-python
if __name__=="__main__":
   main()

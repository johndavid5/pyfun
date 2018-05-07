import sys
import string
import re
import json
import logging
import logging.config

DEBUG = False
VIA_COMMAND_LINE = False

#logging.config.fileConfig('logging.conf')
# create logger
#logger = logging.getLogger('tcalc')

#logging.setLevel(logging.DEBUG)
#logger.setLevel(logging.DEBUG)

#logging.basicConfig(filename='tcalc.log',level=logging.DEBUG)

VERSION="1.1.0"

def main():

    s_line = ""
    global DEBUG
    global VIA_COMMAND_LINE

    for i in range(len(sys.argv)):
        debug_print("sys.argv[%d]=\"%s\""%(i, sys.argv[i]))
        if sys.argv[i].lower() == "-dbg":
            i += 1
            i_debug = int(sys.argv[i])
            if( i_debug ):
                DEBUG = True
            else:
                DEBUG = False
        elif sys.argv[i].lower() == "-c":
            VIA_COMMAND_LINE=True
            i += 1
            s_line = sys.argv[i]
            print("+ " + s_line + " = " + do_line(s_line));

    print("DEBUG="+str(DEBUG))
    print("VIA_COMMAND_LINE="+str(VIA_COMMAND_LINE))
    print("VERSION="+str(VERSION))

    if VIA_COMMAND_LINE:
        exit(0)

    # terminal-based hours:minutes::seconds time add / subtract calculator
    while 1:
        #sys.stdout.write("tcalc>");
        #line = sys.stdin.readline()
        try:
            s_line = input("tcalc>");
            s_line = trim_comments(s_line)
            s_line = s_line.strip() # That's trim() in the rest of the world...

            if( s_line == "quit" ): 
                break

            if len(s_line) <= 0: 
                next

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
    s_out = ""
    debug_print(sWho + "(): s_line = \"" + s_line + "\"...");

    match = RE_LINE.match(s_line) 

    if( match ):
        debug_print(sWho + "(): SHEMP: match.group(0) = \"" + match.group(0) + "\"...")
        arr_groups = match.groups()
        num_groups = len(arr_groups)
        debug_print(sWho + "(): SHEMP: num_groups = " + str(num_groups) + "...")
        #debug_print(sWho + "(): SHEMP: groups = \"" + list_to_short_string(groups) + "\"...")
        debug_print(sWho + "(): SHEMP: arr_groups = \"" + json.dumps(arr_groups) + "\"...")
        debug_print(sWho + "(): SHEMP: \n" + list_to_string(arr_groups, "arr_groups","  ") )

        for i in range(0,num_groups+1):
            debug_print(sWho + "(): SHEMP: match.group(" + str(i) + ") = " + match.group(i) + "...")

        map_a = {}
        map_a['hours'] = int(match.group(1))
        map_a['minutes'] = int(match.group(2))
        map_a['seconds'] = int(match.group(3))

        debug_print(sWho + "(): SHEMP: Moe, map_a = %s..." % json.dumps(map_a) )

        s_operator = match.group(4)
        debug_print(sWho + "(): SHEMP: Moe, s_operator = \"%s\"..." % s_operator )
        #debug_print(sWho + "(): SHEMP: Moe, s_operator = \"" + s_operator + "\"...")

        tot_seconds_a = hms_to_s(map_a['hours'], map_a['minutes'], map_a['seconds'])
        debug_print(sWho + "(): SHEMP: Moe, tot_seconds_a = %d..." % tot_seconds_a )

        map_b = {}
        map_b['hours'] = int(match.group(5))
        map_b['minutes'] = int(match.group(6))
        map_b['seconds'] = int(match.group(7))

        debug_print(sWho + "(): SHEMP: Moe, map_b = %s..." % json.dumps(map_b) )

        tot_seconds_b = hms_to_s(map_b['hours'], map_b['minutes'], map_b['seconds'])
        debug_print(sWho + "(): SHEMP: Moe, tot_seconds_b = %d..." % tot_seconds_b )

        tot_seconds_c = None

        if( s_operator == "-" ):
            tot_seconds_c = tot_seconds_a - tot_seconds_b
        elif( s_operator == "+" ):
            tot_seconds_c = tot_seconds_a + tot_seconds_b
        elif( s_operator == "to" ):
            tot_seconds_c = tot_seconds_b - tot_seconds_a

        debug_print(sWho + "(): SHEMP: Moe, tot_seconds_c = %d..." % tot_seconds_c )

        s_prefix = ""
        i_multiplier = 1
        if tot_seconds_c < 0: 
            s_prefix = "-"
            i_multiplier = -1
            tot_seconds_c *= -1

        out_map = s_to_hms(tot_seconds_c) 
        debug_print(sWho + "(): SHEMP: Moe, out_map = " + json.dumps(out_map) + "...")
        
        #s_out = "%d:%02d:%02d" % str(out_map['hours']) + ":" + str(out_map['minutes']) + ":" + str(out_map['seconds'])
        s_out = "%s%d:%02d:%02d" % (s_prefix, out_map['hours'], out_map['minutes'], out_map['seconds'] )
        s_out += " = %d seconds" % (tot_seconds_c*i_multiplier)

    else:
        debug_print(sWho + "(): SHEMP: Sorry, Moe, no match...");
        s_out = "???"
    
    return s_out


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


SECONDS_PER_HOUR = 3600
SECONDS_PER_MINUTE = 60

def hms_to_s(hours, minutes, seconds):
    return hours*SECONDS_PER_HOUR + minutes*SECONDS_PER_MINUTE + seconds

def debug_print(msg):
    if DEBUG:
        print("*** " + msg )

def s_to_hms(total_seconds): 
    out_map = {}
    out_map['hours'] = int( total_seconds / SECONDS_PER_HOUR )
    total_seconds = total_seconds % SECONDS_PER_HOUR
    out_map['minutes'] = int( total_seconds / SECONDS_PER_MINUTE )
    total_seconds = total_seconds % SECONDS_PER_MINUTE
    out_map['seconds'] = total_seconds
    return out_map

def trim_comments(s_line):
    i_where = s_line.find("#") 
    # NOTA: This Also works for failed find, because 
    # i_where is -1 in that case...
    return s_line[i_where+1:] 

# Automatically kick-start main()...
# https://stackoverflow.com/questions/1590608/is-it-possible-to-forward-declare-a-function-in-python
if __name__=="__main__":
   main()

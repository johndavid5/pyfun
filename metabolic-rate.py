# reference: https://en.wikipedia.org/wiki/Harris–Benedict_equation
#
# The Harris–Benedict equations revised by Mifflin and St Jeor in 1990:[4]
#
# Men	BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) + 5
# Women	BMR = (10 × weight in kg) + (6.25 × height in cm) - (5 × age in years) - 161
# 
# -----------------------------------------------------------------
# While the original paper does not attempt to translate BMR into
# total energy expenditure (TEE), a BMR result may be multiplied
# by a factor that approximates an individual's physical activity level
# (PAL) to estimate their TEE. The following table enables approximation
# of an individual's daily TEE based on some example lifestyles.[5]
# 
# Lifestyle                                                                             Example PAL                                     Calculation
# Sedentary or light activity   Office worker getting little or no exercise	        1.53	BMR x 1.53
# Active or moderately active   Construction worker or person running one hour daily	1.76	BMR x 1.76
# Vigorously active             Agricultural worker (non mechanized) or person swimming two hours daily	2.25	BMR x 2.25
# ---------------------------------------------------------------------
import sys 

DEBUG=False

CENTIMETERS_PER_INCH=float(2.54)
KILOGRAMS_PER_POUND=float(0.454)

PAL_SEDENTARY=float(1.53)
PAL_ACTIVE=float(1.76)
PAL_VIGOROUS=float(2.25)

def main():
    male_female=None

    weight_in_pounds=None
    mass_in_kilograms=None

    height_in_inches=None
    height_in_centimeters=None

    age_in_years=None

    for i in range(1,len(sys.argv)):
        debug_print("sys.argv[%d]=\"%s\""%(i, sys.argv[i]))
        if( sys.argv[i].lower() == "-help" ):
            print_help()
            exit(255)
        elif( sys.argv[i].lower() == "-dbg" ):
            i += 1
            if sys.argv[i].lower() == "true" or sys.argv[i].lower() == "1":
                DEBUG=True
        elif( sys.argv[i].lower() == "-mf" ):
            i += 1
            male_female = sys.argv[i].lower()
        elif( sys.argv[i].lower() == "-wlb" ):
            i += 1
            weight_in_pounds = float(sys.argv[i])
        elif( sys.argv[i].lower() == "-mkg" ):
            i += 1
            mass_in_kilograms = float(sys.argv[i])
        elif( sys.argv[i].lower() == "-hin" ):
            i += 1
            height_in_inches = float(sys.argv[i])
        elif( sys.argv[i].lower() == "-hcm" ):
            i += 1
            height_in_centimeters = float(sys.argv[i])
        elif( sys.argv[i].lower() == "-ayr" ):
            i += 1
            age_in_years = float(sys.argv[i])

    #print("DEBUG = " + str(DEBUG) + "...")

    print("PAL_SEDENTARY = %f..." % (PAL_SEDENTARY) )
    print("PAL_ACTIVE = %f..." % (PAL_ACTIVE) )
    print("PAL_VIGOROUS = %f..." % (PAL_VIGOROUS) )
    print("")
    print("KILOGRAMS_PER_POUND = %f..." % (KILOGRAMS_PER_POUND) )
    print("CENTIMETERS_PER_INCH = %f..." % (CENTIMETERS_PER_INCH) )
    print("")

    print("male_female = %s..." % (is_null(male_female)) )
    print("weight_in_pounds = %s..." % (is_null(weight_in_pounds,"","")) )
    print("mass_in_kilograms = %s..." % (is_null(mass_in_kilograms,"","")) )
    print("height_in_inches = %s..." % (is_null(height_in_inches,"","")) )
    print("height_in_centimeters = %s..." % (is_null(height_in_centimeters,"","")) )
    print("age_in_years = %s..." % (is_null(age_in_years,"","")) )

    if mass_in_kilograms == None and weight_in_pounds != None:
        mass_in_kilograms = pounds_to_kilograms(weight_in_pounds)
        print("Calculated mass_in_kilograms = %s..." % (is_null(mass_in_kilograms,"","")) )
    elif weight_in_pounds == None and mass_in_kilograms != None:
        weight_in_pounds = kgs_to_lbs(mass_in_kilograms)
        print("Calculated weight_in_pounds = %s..." % (is_null(weight_in_pounds,"","")) )

    if height_in_centimeters == None and height_in_inches != None:
        height_in_centimeters = inches_to_centimeters(height_in_inches)
        print("Calculated height_in_centimeters = %s..." % (is_null(height_in_centimeters,"","")) )
    elif height_in_inches == None and height_in_centimeters != None:
        height_in_inches = centimeters_to_inches(height_in_centimeters)
        print("Calculated height_in_inches = %s..." % (is_null(height_in_inches,"","")) )

    bmr = basal_metabolic_rate( mass_in_kilograms, height_in_centimeters, age_in_years, male_female )  

    print("")

    print("basal_metabolic_rate( mass_in_kilograms = %.2f, height_in_centimeters = %.2f, age_in_years = %.2f, male_female = \"%s\" ) = %.2f calories per day..." % (mass_in_kilograms, height_in_centimeters, age_in_years, male_female, bmr ) )

    print("")

    print("Total Energy Expenditure(TEE) from Physical Activity Level (PAL):")
    print("=================================================================")
    print("* For \"Sedentary\" lifestyle, Total Energy Expenditure = Basal Metabolic Rate * PPAL_SEDENTARY = %.2f x %.2f = %.2f calories per day" % (bmr, PAL_SEDENTARY, (bmr*PAL_SEDENTARY)) )
    print("* For \"Active\" lifestyle, Total Energy Expenditure = Basal Metabolic Rate * PAL_ACTIVE = %.2f x %.2f = %.2f calories per day" % (bmr, PAL_ACTIVE, (bmr*PAL_ACTIVE)) )
    print("* For \"Vigorous\" lifestyle, Total Energy Expenditure = Basal Metabolic Rate * PPAL_VIGOROUS = %.2f x %.2f = %.2f calories per day" % (bmr, PAL_VIGOROUS, (bmr*PAL_VIGOROUS)) )

    print("")
    print("Let off some steam, Bennett!")

# ######## #
# end main #
# ######## #

def print_help():
    print("""Format:
    py metabolic_rate.py -mf <'m'|'f'> [ -wlb <weight_in_pounds> || -mkg <mass_in_kilograms> ] [ -hin <height_in_inches> || -hcm <height_in_centimeters> ] -ayr <age_in_years>
      -- or --
    py metabolic_rate.py -help (to print this help message and exit)
      
    EXAMPLE: If you are a 34 year old 5'4" tall (or 64" tall)
     female who weighs 100 lbs...

    py metabolic_rate.py -mf f -wlb 100 -hin 64 -ayr 34
    """)

def is_null(input,prefix="\"",suffix="\""):
    if input != None:
        return prefix + str(input) + suffix
    else:
        return str("None")

def debug_print(input):
    if(DEBUG != False):
        print(input)

def basal_metabolic_rate( mass_in_kilograms, height_in_centimeters, age_in_years, male_female ):  
    bmr = (10 * mass_in_kilograms) + (6.25 * height_in_centimeters ) - (5 * age_in_years)
    if male_female == "m":
        bmr += 5
    elif male_female == "f":
        bmr -= 161
    return bmr

def inches_to_centimeters(inches):
    sWho = "inches_to_centimeters"
    debug_print(sWho + "(): inches = " + str(inches) )
    return inches*CENTIMETERS_PER_INCH

def centimeters_to_inches(centimeters):
    sWho = "centimeters_to_inches"
    debug_print(sWho + "(): centimeters = " + str(centimeters) )
    return centimeters/CENTIMETERS_PER_INCH

def pounds_to_kilograms(pounds):
    sWho = "pounds_to_kilograms"
    debug_print(sWho + "(): pounds = " + str(pounds) )
    return pounds*KILOGRAMS_PER_POUND

def kilograms_to_pounds(kilograms):
    sWho = "kilograms_to_pounds"
    debug_print(sWho + "(): kilograms = " + str(kilograms) )
    return kilograms/KILOGRAMS_PER_POUND


# Automatically kick-start main()...
# https://stackoverflow.com/questions/1590608/is-it-possible-to-forward-declare-a-function-in-python
if __name__=="__main__":
   main()

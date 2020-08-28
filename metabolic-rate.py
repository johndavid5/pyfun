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
from argparse import ArgumentParser

CENTIMETERS_PER_INCH=float(2.54)
KILOGRAMS_PER_POUND=float(0.454)

PAL_SEDENTARY=float(1.53)
PAL_ACTIVE=float(1.76)
PAL_VIGOROUS=float(2.25)

def main(options):

    print(options.__dict__)
    DEBUG=options.debug

    print(f'DEBUG = {DEBUG}...')
    print(f'PAL_SEDENTARY = {PAL_SEDENTARY}...')
    print(f'PAL_ACTIVE = {PAL_ACTIVE}...')
    print(f'PAL_VIGOROUS = {PAL_VIGOROUS}...')
    print('')
    print(f'KILOGRAMS_PER_POUND = {KILOGRAMS_PER_POUND}...')
    print(f'CENTIMETERS_PER_INCH = {CENTIMETERS_PER_INCH}...' )
    print('')

    if not options.weight_kg:
        options.weight_kg = pounds_to_kilograms(options.weight_lb)
    if not options.height_cm:
        options.height_cm = inches_to_centimeters(options.height_in)

    print(f'sex = {options.sex}...')
    print(f'Weight (lb) = {options.weight_lb}...')
    print(f'Weight (kg) = {options.weight_kg}...')
    print(f'Height (in) = {options.height_in}...')
    print(f'Height (cm) = {options.height_cm}...')
    print(f'age = {options.age}...')

    bmr = int(basal_metabolic_rate(options.weight_kg, options.height_cm, options.age, options.sex))

    print('')
    print(''.join([
      f'basal_metabolic_rate(',
      ', '.join([
        f'weight_kg = {options.weight_kg}',
        f'height_cm = {options.height_cm}',
        f'age = {options.age}',
        f'sex = {options.sex}',]),
      f') = {bmr} calories per day...'
    ]))
    print('')

    print('Total Energy Expenditure (TEE) from Physical Activity Level (PAL):')
    print('=================================================================')
    print(
      '* For \'Sedentary\' lifestyle, Total Energy Expenditure = ' +
      f'Basal Metabolic Rate * PAL_SEDENTARY = {bmr} x {PAL_SEDENTARY} = {int(bmr * PAL_SEDENTARY)} calories per day')
    print(
      '* For \'Active\' lifestyle, Total Energy Expenditure = ' +
      f'Basal Metabolic Rate * PAL_ACTIVE = {bmr} x {PAL_ACTIVE} = {int(bmr * PAL_ACTIVE)} calories per day')
    print(
      '* For \'Vigorous\' lifestyle, Total Energy Expenditure = ' +
      f'Basal Metabolic Rate * PPAL_VIGOROUS = {bmr} x {PAL_VIGOROUS} = {int(bmr * PAL_VIGOROUS)} calories per day')

    print('')
    print('Let off some steam, Bennett!')

def basal_metabolic_rate(weight_kilograms, height_centimeters, age_in_years, sex):
    calories = (10 * weight_kilograms) + (6.25 * height_centimeters) - (5 * age_in_years)
    if sex in ('m', 'male'):
        calories += 5
    elif sex in ('f', 'female'):
        calories -= 161
    return calories

def inches_to_centimeters(inches):
    return inches * CENTIMETERS_PER_INCH

def centimeters_to_inches(centimeters):
    return centimeters / CENTIMETERS_PER_INCH

def pounds_to_kilograms(pounds):
    return pounds * KILOGRAMS_PER_POUND

def kilograms_to_pounds(kilograms):
    return kilograms / KILOGRAMS_PER_POUND


# Automatically kick-start main()...
# https://stackoverflow.com/questions/1590608/is-it-possible-to-forward-declare-a-function-in-python
if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument('-dbg', '--debug', default=False, action='store_true')
    parser.add_argument('-a', '--age', type=int, required=True)
    parser.add_argument('-s', '--sex', type=str, required=True)
    weight = parser.add_mutually_exclusive_group(required=True)
    weight.add_argument('-lb', '--weight-lb', type=float)
    weight.add_argument('-kg', '--weight-kg', type=float)
    height = parser.add_mutually_exclusive_group(required=True)
    height.add_argument('-in', '--height-in', type=float)
    height.add_argument('-cm', '--height-cm', type=float)

    args = parser.parse_args()
    main(args)


import argparse

from core.rotor import rotorb_instance
from core.reflector import reflectorb_instance

parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-r', '--rotor',
                    help="For example -r ROTOR_II -r ROTOR_I -r ROTOR_III.\nSupport: ROTOR_I, ROTOR_II, ROTOR_III, ROTOR_IV, ROTOR_V.\nDefault ROTOR_I, ROTOR_II, ROTOR_III",
                    action='append', choices=rotorb_instance.values, metavar='')
parser.add_argument('-k', '--key', help="For example --key a --key b --key c. Default a, a, a", action='append')
parser.add_argument('--reflector', help="For example UKW_B.\nSupport: UKW_A, UKW_B, UKW_C.\nDefault: UKW_B", choices=reflectorb_instance.values, metavar='', default="UKW_B")
parser.add_argument('--plugboard', help="For example --plugboard AB --plugboard CD", metavar='', default=[], action='append')

args = parser.parse_args()

#
# Python project set up
# --------------------------------------------------------
# Description:
# Unicorn power.
# Convert horsepower => unicorn power
# --------------------------------------------------------
# Author: Tariku T.
#
from colorama import Fore, Style
import powers as unicorns

power = 1500
unicorns = unicorns.Powers.MagicalFormula(power)

print(Fore.MAGENTA  + "You will need " + str(unicorns) + " unicorns")
print(Style.RESET_ALL)
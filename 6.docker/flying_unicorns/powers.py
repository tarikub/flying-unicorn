#
# Python project set up 
# --------------------------------------------------------
# Description:
# Authoritative and definitive class to calculate how many unicorn powers 
# it takes to match a given horsepower.  
# --------------------------------------------------------
# Author: Tariku T.
#

import random
import const

class Powers:
    
    def MagicalFormula(power: int) -> int:
         """A magical formula to give a unicorn powers.

        Args:
             power (int): Power in horsepower
        """
         
         rnd = random.randint(const.LOW, const.HIGH)

         return rnd * power
#
# Author: Darian Marvel
#
#

from enum import Enum

class InstructionType(Enum):
    skip_to_tag = 1
    skip_to_class = 2
    save_value_as_property = 3
    save_href_as_property = 4

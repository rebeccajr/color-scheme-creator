#_______________________________________________________________________
#       _   __   _   _ _   _   _   _         _
#  |   |_| | _  | | | V | | | | / |_/ |_| | /
#  |__ | | |__| |_| |   | |_| | \ |   | | | \_
#   _  _         _ ___  _       _ ___   _                        / /
#  /  | | |\ |  \   |  | / | | /   |   \                        (^^)
#  \_ |_| | \| _/   |  | \ |_| \_  |  _/                        (____)o
#_______________________________________________________________________
#
#-----------------------------------------------------------------------
#  Copyright 2024, Rebecca Rashkin
#  -------------------------------
#  This code may be copied, redistributed, transformed, or built upon in
#  any format for educational, non-commercial purposes.
# 
#  Please give me appropriate credit should you choose to modify this
#  code. Thank you :)
#-----------------------------------------------------------------------
#
#_______________________________________________________________________
#  //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\   //\^.^/\\
#_______________________________________________________________________

#_______________________________________________________________________
# Contains operations related to RGB colors
#_______________________________________________________________________

from utilities.color_scheme_utils import GeneralUtils as Utils

#_______________________________________________________________________
class RgbConst:

  RED_STR: str = 'RED'
  GRN_STR: str = 'GRN'
  BLU_STR: str = 'BLU'

  RED_MASK: str = 0xFF0000
  GRN_MASK: str = 0x00FF00
  BLU_MASK: str = 0x0000FF

  RED_RIGHT_SHIFT: int = 16
  GRN_RIGHT_SHIFT: int = 8
  BLU_RIGHT_SHIFT: int = 0

  DEFAULT_BACKGROUND: int = 0x1c1c1c
  DEFAULT_FOREGROUND: int = 0xeeeeee

  DEFAULT_RGB_STR_LIST: list[str] = '0x202020'\
      ' 0x800000'\
      ' 0x008000'\
      ' 0x808000'\
      ' 0x000080'\
      ' 0x800080'\
      ' 0x008080'\
      ' 0x808080'\
      ' 0x000000'\
      ' 0xd70000'\
      ' 0x00d700'\
      ' 0xd7d700'\
      ' 0x0000d7'\
      ' 0xd700d7'\
      ' 0x00d7d7'\
      ' 0xd7d7d7'

  DEFAULT_RGB_INT_LIST: list[int] =\
    Utils.str_list_to_hex_list(DEFAULT_RGB_STR_LIST.split())


#_______________________________________________________________________
class RgbColor:

  #_____________________________________________________________________
  def get_rgb_from_hex(rgb_color: int) -> dict:
    """
    Creates map of red, green, and blue values from a single number.

    E.g.
    input:  0xFFFF00
    output: {'red': 255, 'grn': 255, blu: 0}
    """

    rgb_map: dict = {}

    red: int = (rgb_color & RgbConst.RED_MASK) >> RgbConst.RED_RIGHT_SHIFT
    grn: int = (rgb_color & RgbConst.GRN_MASK) >> RgbConst.GRN_RIGHT_SHIFT
    blu: int = (rgb_color & RgbConst.BLU_MASK) >> RgbConst.BLU_RIGHT_SHIFT

    rgb_map[RgbConst.RED_STR] = red
    rgb_map[RgbConst.GRN_STR] = grn
    rgb_map[RgbConst.BLU_STR] = blu

    return rgb_map

  #_____________________________________________________________________
  def int_list_hex_str(l: list[int]) -> str:
    """
    Prints list of integers as 6 digit hex string.
    """

    out_str: str = ''


    for i in range (len(l)):
      out_str = f'{out_str}\nColor {i:02}: 0x{l[i]:06x}'

    return out_str

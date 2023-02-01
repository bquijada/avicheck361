# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 2/1/23 
# Description: Region Class to define a backcountry area

class Region:
    """a region class to define a backcountry area to explore. Consists of a name and coordinates"""
    def __init__(self, name, coord):
        self._name = name
        self._coord = coord

    def get_name(self):
        return self._name

    def get_coord(self):
        return self._coord


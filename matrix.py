# Author: Brenda Levy
# GitHub username: bqujiada
# Date: 2/7/23 
# Description: recommendation class

class Recommendation:
    """a recommendation class to define a backcountry warning on the area to explore. Consists of a name and
    coordinates """

    def __init__(self, name, reason):
        self._name = name
        self._reason = reason

    def get_name(self):
        return self._name

    def get_reason(self):
        return self._reason


nr = Recommendation("Not Recommended", "The current conditions for this terrain are very dangerous and it is "
                                       "recommended to either change terrain or postpone the trip to when conditions "
                                       "are better.")
ec = Recommendation("Extra Caution", "The current conditions for this terrain are dangerous. If you choose to "
                                     "proceed, take extra caution and make conservative choices.")
c = Recommendation("Caution", "The current conditions for this terrain are reasonable, but always take caution while "
                              "recreating in the back-country")


# Data Type - Character, Integer, Long, Float and Double

class Solution:
    def dataTypeSize(self, datatype):
        sizes = {
            "Integer": 4,
            "Float": 4,
            "Double": 8,
            "Character": 1,
            "Long": 8,
            "Boolean": 1
        }
        return sizes.get(datatype, 0)

import math
#                 0   1   2   3   4   5   6   7
combinations = [["", "", "J", "V", "D", "", "", ""],# 0
                ["", "", "W", "X", "", "", "", ""],# 1
                ["", "", "", "", "", "", "", ""],# 2
                ["", "", "Z", "", "", "", "", ""],# 3
                ["", "E", "F", "G", "", "", "", ""],# 4
                ["K", "L", "M", "N", "A", "", "", ""],# 5
                ["P", "Q", "R", "S", "B", "H", "", "O"],# 6
                ["T", "U", "Y", "", "C", "I", "", ""]]# 7

def AnalysePose(leftShoulder, leftWrist, rightShoulder, rightWrist):
    # angles in radians
    #      0
    #-90       90
    #     180
    # currently shoulder to wrist seems most accurate
    leftarm = math.atan2(leftShoulder[1] - leftWrist[1], leftShoulder[0] - leftWrist[0])
    leftarm = math.degrees(leftarm)
    rightarm = math.atan2(rightShoulder[1] - rightWrist[1], rightShoulder[0] - rightWrist[0])
    rightarm = math.degrees(rightarm)

    leftDirection = getDirection(leftarm)
    rightDirection = getDirection(rightarm)

    return combinations[leftDirection][rightDirection]

# 22.5, 67.5, 112.5, 157.5
#     0
#   7   1
# 6       2
#   5   3
#     4
def getDirection(value):
    if(abs(value) > 157.5):
        return 4
    if(value > 112.5):
        return 3
    if(value > 67.5):
        return 2
    if(value > 22.5):
        return 1
    if(value < -112.5):
        return 5
    if(value < -67.5):
        return 6
    if(value < -22.5):
        return 7
    return 0
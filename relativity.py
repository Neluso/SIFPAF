import math


def lorentz_factor(beta):
    return 1/math.sqrt(1-beta**2)


def p2v(momentum):
    return math.sqrt(1-1/(momentum**2))

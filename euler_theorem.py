#!/usr/bin/python3

import sys
import numpy as np


def euler_phi(n):
    phi_array = []

    for i in range(0, n):
        if (np.gcd(i, n) == 1):
            phi_array.append(i)

    print("List of coprime integers to {0}:\t{1}".format(n, phi_array))
    return len(phi_array)


def init():
    print('Please enter a positive integer which we will check the Euler totient of:')
    n = int(input())
    print('Please enter an integer coprime to {0}'.format(n))
    a = int(input())
    
    phi = euler_phi(n)
    print("phi = {0}".format(phi))
    prefix = a**phi
    print("{0}**{1} = {2}".format(a, phi, prefix))
    suffix = prefix % n
    print("{0} modulo {1} = {2}".format(prefix, n, suffix))

    if (suffix == 1):
        print("({0} to the power of {1}) modulo {2} = 1".format(a, phi, n));
        print("We've just demonstrated Euler's theorem!");
    else:
        print("Error! We weren't able to prove Euler's theorem - check your algorithm");

if __name__ == "__main__":
    init()

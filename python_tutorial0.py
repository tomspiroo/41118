#!/usr/bin/env python3

import math
import random
import time


# Create a Class called "Location".
# Each location object will have an x and y variable denoting a location in 2D space.
class Location:
    def __init__(self, x, y):

        # Save the input arguments as object variables
        self.x = x
        self.y = y


# Create a Class called "WeightedAverage"
# This Class provides a method for processing a list of Locations
class WeightedAverager:
    def __init__(self, origin, landmarks):

        # Save the input arguments as object variables
        self.origin = origin
        self.landmarks = landmarks

        # Define parameters
        threshold = 10.0 # outliers beyond this distance should be ignored

        # Call the averaging function
        answer = self.weighted_average(threshold)

        # Print the answer to console
        print("answer: " + str(answer))

    def weighted_average(self, threshold):

        # TODO: most of your code will go here


        return 0.0 # Change this return value later

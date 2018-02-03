# ENGR2050_04_jasayles.py
# Ethan Sayles
# Feb 23, 2017
import numpy as np

def forwards(theta_4, theta_2, Dtheta2):                                                              #theta_4 is the list of theta4 values in degrees, theta_2 is the list of theta2 values in degrees, and Dtheta2 is the time derivative of theta2 in radians/s
    Dtheta4 = []                                                                                                          #The time derivative of theta4
    for i in range (len(theta_4) - 1):                                                                           #Loop through theta4, excluding the last term. (forwards difference can't use the last term)
        Dtheta4.append((theta_4[i+1] - theta_4[i])/(theta_2[i+1] - theta_2[i]))        #Calculate the derivative of theta4 with respect to theta2
        Dtheta4[i] = Dtheta4[i] * Dtheta2                                                                   #Multiply by the time derivative of theta2 to get the time derivative of theta4
        Dtheta4[i] = round(Dtheta4[i], 4)
    Dtheta4.append("null")                                                                                       #Fill the last slot with a random non-value
    return (Dtheta4)
    
def backwards(theta_4, theta_2, Dtheta2):                                                            #theta_4 is the list of theta4 values in degrees, theta_2 is the list of theta2 values in degrees, and Dtheta2 is the time derivative of theta2 in radians/s
    Dtheta4 = []                                                                                                          #The time derivative of theta4
    Dtheta4.append("null")                                                                                       #Fill the first slot with a random non-value
    for i in range (1, len(theta_4)):                                                                            #Loop through theta4, excluding the first term. (backwards difference can't use the first term)
        Dtheta4.append((theta_4[i] - theta_4[i-1])/(theta_2[i] - theta_2[i-1]))           #Calculate the derivative of theta4 with respect to theta2
        Dtheta4[i] = Dtheta4[i] * Dtheta2                                                                   #Multiply by the time derivative of theta2 to get the time derivative of theta4
        Dtheta4[i] = round(Dtheta4[i], 4)
    return (Dtheta4)
    
def central(theta_4, theta_2, Dtheta2):                                                                  #theta_4 is the list of theta4 values in degrees, theta_2 is the list of theta2 values in degrees, and Dtheta2 is the time derivative of theta2 in radians/s
    Dtheta4 = []                                                                                                          #The time derivative of theta4
    Dtheta4.append("null")                                                                                       #Fill the first slot with a random non-value
    for i in range (1, len(theta_4) - 1):                                                                       #Loop through theta4, excluding the first and last terms. (central difference can't use the first or last terms)
        Dtheta4.append((theta_4[i+1] - theta_4[i-1])/(2*(theta_2[i+1] - theta_2[i])))   #Calculate the derivative of theta4 with respect to theta2
        Dtheta4[i] = Dtheta4[i] * Dtheta2                                                                   #Multiply by the time derivative of theta2 to get the time derivative of theta4
        Dtheta4[i] = round(Dtheta4[i], 4)
    Dtheta4.append("null")                                                                                       #Fill the last slot with a random non-value
    return (Dtheta4)
    
#Conditional to check for test cases
if __name__ == '__main__':
    theta_4 = [90.88, 87.16, 83.85, 81.04, 78.77, 77.07, 75.89, 75.22, 75.01, 75.19]
    theta_2 = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    print ("Forwards: ", forwards(theta_4, theta_2, 36.7))
    print ("Backwards: ", backwards(theta_4, theta_2, 36.7))
    print ("Cental: ", central(theta_4, theta_2, 36.7))

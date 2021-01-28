import numpy as np
import matplotlib.pyplot as plt
import random
import quantumrandom

def int2bin(number: int) -> list:
    '''
    Converts an integer into a list of bits
    '''
    return list(bin(number)[2:]) # [2:] because the first two characters are 0b

def gen_random_numbers(size):
    # the length of the array obtained from the api should be an int that has enough bits for size
    # they are all 2 bytes (16 bits) so you need 1/16th of the size you are looking for
    length = np.ceil(size/16)

    x = np.array(quantumrandom.get_data(data_type='uint16', array_length=length))

    final_array = []
    for number in x:
        final_array.extend(map(int, int2bin(number)))
        
    # size will always be smaller than len(final_array) because the length was rounded up
    # make the list the length of size
    final_array = final_array[len(final_array)-size:]

    avg = np.mean(final_array)

    return avg

def main():
    x = []
    y = []
    yavg = []

    for i in range(1, 1024):
        x.append(i)
        y.append(gen_random_numbers(i))
        yavg.append(sum(y)/len(y))

    plt.figure()
    plt.plot(x, y, '-r')
    plt.plot(x, yavg, '-b')

    plt.xlabel('Length of list of random numbers')
    plt.ylabel('Average of random numbers in the list')

    plt.show()
    return

if __name__=='__main__':
    main()
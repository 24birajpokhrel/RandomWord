import random


def preprocess(srcFilename, n):
    char = 1
    parts = char * n
    grams = parts
    key = []
    with open(srcFilename, 'r') as file:
        for line in file:    #Check each line of the file
             values= dict.fromkeys(line, 0)  
            for parts in range(len(line.split())):       #Section the line into chunks of n
                pos = parts
                for x in grams:
                    key.append(line.split()[pos])
            d = dict.fromkeys(line, 0)  
            for val in line:
                values[val] += 1 





    pass


def generate(destFilename, model, numChars, initial):
    """Write numChars characters to indicated destination based upon model dictionary.

    destFilename is the desired name of the output file
    model is the dictionary produced by preprocessing
    numChars is the number of desired output characters
    initial is the first ngram of the original source

    The function should write its output to the file and return
    the number of generated characters. Typically that will be
    exactly numChars, but it could be less if the model reaches
    a state with no possible continuation.
    """
    pass





##################################################################
# Main program driver below. Do not edit
##################################################################
if __name__ == '__main__':
    import sys
    import os
    from string import ascii_uppercase
    
    n = 0
    while n <= 0:
        try:
            n = int(input("What value of n for n-grams? "))
            if n <= 0:
                print("Must choose positive n")
        except ValueError:
            print("Invalid integer")
    
    src = None
    while not src:
        filename = input("Input filename? ")
        try:
            fp = open(filename)
            initial = fp.read(n)
            fp.close()
            src = filename
        except IOError:
            print("Unable to read file", filename)
    
    
    default = filename.split('/')[-1].split('.')[0] + '_' + str(n) + '.txt'
    output = None
    while not output:
        filename = input("Output filename? [default: %s] " % default)
        if not filename:
            filename = default
        try:
            fp = open(filename,'w')
            fp.close()
            output = filename
        except IOError:
            print("Unable to write to file", filename)
    
    total = 0
    while not 0 < total:
        try:
            total = int(input("How many characters of output are desired? "))
            if total <= 0:
                print("Must choose positive value")
        except ValueError:
            print("Invalid integer")
    
    
    seed = None
    seed = input("Random Seed [press enter if you don't care]: ").strip()
    if not seed:
        seed = ''.join(random.choice(ascii_uppercase) for _ in range(6))
        print('Using seed:', seed)
    random.seed(seed)
    
    
    
    
    
    model = preprocess(src, n)
    c = generate(output, model, total, initial)
    print(f'Generated {c} characters of output')
    

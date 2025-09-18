import random
from collections import defaultdict

def preprocess(srcFilename, n):
    """
    Read the source file and create an n-gram model.
    Returns a dictionary where keys are n-grams and values are lists of possible next characters.
    """
    model = defaultdict(list)
    
    with open(srcFilename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # Create n-grams and their following characters
    for i in range(len(text) - n):
        ngram = text[i:i+n]  # Get n characters
        next_char = text[i+n]  # Get the character that follows
        model[ngram].append(next_char)
    
    return dict(model)

def generate(destFilename, model, numChars, initial):
    """
    Write numChars characters to indicated destination based upon model dictionary.
    destFilename is the desired name of the output file
    model is the dictionary produced by preprocessing
    numChars is the number of desired output characters
    initial is the first ngram of the original source
    The function should write its output to the file and return
    the number of generated characters. Typically that will be
    exactly numChars, but it could be less if the model reaches
    a state with no possible continuation.
    """
    if not model:
        print("Error: Empty model")
        return 0
    
    # Start with the initial n-gram
    generated_text = initial
    current_ngram = initial
    
    # Generate characters one by one
    for _ in range(numChars - len(initial)):
        if current_ngram in model and model[current_ngram]:
            # Choose a random next character from the possible options
            next_char = random.choice(model[current_ngram])
            generated_text += next_char
            
            # Update the current n-gram by sliding the window
            current_ngram = current_ngram[1:] + next_char
        else:
            # No continuation possible
            print(f"No continuation found for n-gram: '{current_ngram}'")
            break
    
    # Write the generated text to the output file
    try:
        with open(destFilename, 'w', encoding='utf-8') as file:
            file.write(generated_text)
        return len(generated_text)
    except IOError as e:
        print(f"Error writing to file: {e}")
        return 0

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
            fp = open(filename, encoding='utf-8')
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
            fp = open(filename,'w', encoding='utf-8')
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
    
    
    print("Building n-gram model...")
    model = preprocess(src, n)
    print(f"Model created with {len(model)} unique n-grams")
    
    print("Generating text...")
    c = generate(output, model, total, initial)
    print(f'Generated {c} characters of output')
    print(f'Output written to: {output}')

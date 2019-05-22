# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # Base case: if sequence is a single character, there's only one way to order it,
    # then return a singleton list containing sequence
    if len(sequence) == 1:
        return [sequence]
    
    else:
        # Hold the first letter of the sequence
        held_letter = sequence[0]
        
        # Copy the sequence after the first character so that we can get the permutations of it
        copy_sequence = sequence[1:]
        
        # Call the get_permutations method with spliced sequence made above
        list_permutations = get_permutations(copy_sequence)
        
        permutations = []
        
        # For each permutation of copy_sequence, and for each character within each element of
        # copy_sequence, insert the held_letter into each possible index of said element
        # and add it to the permutations list
        for i in list_permutations:
            for j in range(len(i)+1):
                
                # Add the held letter at the index j, moving all characters ahead of this 
                # index forward, maybe there's a method for this. I ended up doing it 
                # manually because I had no internet when doing this..
                
                string_before_index = i[0:j]
                string_after_index = i[j:]
                
                new_permutation_string = string_before_index + held_letter + string_after_index
                
                # Append the string to the permutations list
                permutations.append(new_permutation_string)
                
        # Return the permutations list
        return permutations
    
    
if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    # Test 1
    sequence = 'ab'
    print('Input:', sequence)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(sequence))
    
    print('\n==============\n')
    
    # Test 2
    sequence = 'abc'
    print('Input:', sequence)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(sequence))
    
    print('\n==============\n')
    
    # Test 3
    sequence = 'defg'
    print('Input:', sequence)
    print('Expected Output:', ['defg', 'degf', 'dfeg', 'dfge', 'dgef', 'dgfe', \
                               'edfg', 'edgf', 'fdeg', 'fdge', 'gdef', 'gdfe', \
                               'efdg', 'egdf', 'fedg', 'fgde', 'gedf', 'gfde', \
                               'efgd', 'egfd', 'fegd', 'fged', 'gefd', 'gfed'])
    print('Actual Output:', get_permutations(sequence))
    
    print('\n==============\n')
    
    # Test 4
    sequence = 'defghijk'
    print('Input:', sequence)
#    print('Expected Output:', ['defg', 'degf', 'dfeg', 'dfge', 'dgef', 'dgfe', \
#                               'edfg', 'edgf', 'fdeg', 'fdge', 'gdef', 'gdfe', \
#                               'efdg', 'egdf', 'fedg', 'fgde', 'gedf', 'gfde', \
#                               'efgd', 'egfd', 'fegd', 'fged', 'gefd', 'gfed'])
#    print('Actual Output:', get_permutations(sequence))
    list1 = get_permutations(sequence)
    print("Number of permutations (should equal n!) is: ",len(list1))
    
    
    
    
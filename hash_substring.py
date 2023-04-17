# python3
# Mareks Siņica-Siņavskis 221RDB430

B = 13
Q = 256

def read_input():
    input_type = input()
    if input_type[:1] == 'F':
        #file_name = input()
        try:
            with open("tests/06") as text_file:
                pat_data = text_file.readline()
                text_data = text_file.readline()
        except IOError:
            print('Invalid file name')
            return
    elif input_type[:1] == 'I':
        pat_data = text_file.readline()
        text_data = text_file.readline()
    else:
        print('Invalid input!')
        return
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (pat_data.rstrip(), text_data.rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pat_data, text_data):
    global B, Q
    # this function should find the occurances using Rabin Karp alghoritm 
    result = []
    pattern_length = len(pat_data)
    text_length = len(text_data)
    pattern_hash =0 
    text_hash = 0
    B_powers = [1]

    for i in range(1, pattern_length):
        B_powers.append((B * B_powers[i-1]) % Q)

    for i in range(pattern_length):
        pattern_hash = (B * pattern_hash + ord(pat_data[i])) % Q
        text_hash = (B * text_hash + ord(text_data[i])) % Q

    for i in range((text_length - pattern_length)+1):
        if text_hash == pattern_hash:
            if text_data[i:i+pattern_length] == pat_data:
                result.append(i)
        if i < text_length - pattern_length:
            text_hash = (B * (text_hash - ord(text_data[i]) * B_powers[pattern_length-1]) + ord(text_data[i+pattern_length])) % Q

    # and return an iterable variable
    return result

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

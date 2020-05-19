import sys
#pass text file using command line argument
input_file = open(sys.argv[1])
message = input_file.read()
encoded = []

def encoder():
    dict_size = int(256) # can also be called the start code
    inc = int(0) # for indexing from the start code onward
    asciiDict = {chr(i) : i for i in range(dict_size + inc)}

    new_entry = ""

    for character in message:
        entry_with_character = character + new_entry
        if entry_with_character in asciiDict:
            new_entry = entry_with_character
        else:
            encoded.append(asciiDict[new_entry])
            asciiDict[entry_with_character] = dict_size + inc
            new_entry = character
            inc += 1
    if new_entry in asciiDict:
        encoded.append(asciiDict[new_entry])

    next_code = 256
    string = ""
    dictionary = dict([(x, chr(x)) for x in range(dict_size)])

    print("this is the original message : " + message)
    print("this is the encoded message ", encoded) 
    print(len(encoded)/len(message))

encoder()

#If the start code is received, clear the dictionary and set new-entry empty. For
#the next received code, output the character represented by the code and also place it in new-entry. Then
#for subsequent codes received, append the first character of the string represented by the code to new-entry,
#insert the result in the dictionary, then output the string for the received code and also place it in new-entry
#to start the next dictionary entry. When the stop code is received, nothing needs to be done; new-entry can
#be abandoned.
def decoder(encoded_message):
    incr = int(0)
    dict_size = 256
    new_input_code = 256 
    asciiDict = {i : chr(i) for i in range(dict_size + incr)}  #notice that i and chr(i) switch places comapared to the encoder
    new_entry = ""
    decoded = next_code = chr(encoded_message.pop(0))
    #decoded.append(next_code)

    for code in encoded_message:
        if code in asciiDict:
            new_entry = asciiDict[code]
        if code == dict_size+incr:
            new_entry = next_code + next_code[0]

        decoded += new_entry

        asciiDict[dict_size + incr] = next_code + new_entry[0]
        incr += 1
        next_code = new_entry

    print("this is the original message : ", encoded_message)
    print("this is the decoded message ", decoded)


decoder(encoded)
"""
COSC326 Etude 9 Substrings
Authors:
    Katherine Butt
    Ava Reese
    Francesa Totty
    Matt Dixon
"""
def substringgenerator(value):
    value = value.strip("\n")
    """
    This section of code determine how many new
    characters appear in the input value
    """
    diff_characters = ''
    longeststring = ''
    for c in value:
        if c not in diff_characters:
            diff_characters += c
            longeststring += c + c
    """
    This section of code determines the longest substring
    """
    baselongest = len(diff_characters) * 2
    baselongeststring = longeststring
    position = 0

    temp = ''
    """
    Generates all of the possible pairs and adds them to the string
    """
    for x in diff_characters:
        position = 0
        while(position < (len(diff_characters))):
            temp1 = x + diff_characters[position]
            if not(temp1 in temp):
                temp += temp1
            position += 1

    """
    Adding in a check for when a character occurs more than twice in a row
    """
    char1 = ''
    char2 = ''
    char3 = ''
    pos = 0
    while pos < len(temp)-3:
        char1 = temp[pos]
        char2 = temp[pos+1]
        char3 = temp[pos+2]
        if(char1 == char2):
            if(char2 == char3):
                temp = temp[:pos+1] + temp[pos+2:]
        pos += 1

    """
    Checking if the longest string has become longer than the orginal longest string
    Returns the largest value
    """
    if(len(temp) > baselongest):
        return temp + " " + str(len(temp))
    else:
        return baselongeststring + " " + str(baselongest)

if __name__ == "__main__":
    values = open('test.txt', 'r')
    for line in values:
        print(substringgenerator(line))

def check_same_letter(s):
    if len(s) > 256:
        print('not exist same letter')
        return False

    flag = [0] * 256
    for letter in s:
        ascii_letter = ord(letter)
        if flag[ascii_letter] == 1:
            print('exist same letter')
            return
        else:
            flag[ascii_letter] = 1    
    
    print('not exist same letter')
    return

def check_same_letter2(s):
    if len(s) > 256:
        print('not exist same letter')
        return

    flag = 0
    for letter in s:
        ascii_letter = ord(letter)
        if (flag & (1 << ascii_letter)) > 0:
            print('exist same letter')
            return
        else:
            flag |= (1 << ascii_letter)
    print('not exist same letter')
    return


check_same_letter2('hogefuga')
check_same_letter2('hogefu')
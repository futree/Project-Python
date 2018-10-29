#extract odd char and even char and combine them
def encryptStatement(msg: str) -> str:
    evenchar = ''
    oddchar = ''
    count = 0
    for ch in msg:
        if count % 2 == 0: #since even starts 1st, len(oddchar) < len(evenchar) if odd numbered letter
            evenchar += ch
        else:
            oddchar += ch
        count += 1
    return oddchar + evenchar

#since this encryption is not linear, need a whole new function to decrypt the phrase
def decryptStatement(msg: str) -> str:
    halfLength = len(msg)//2
    oddchar = msg[:halfLength]
    evenchar = msg[halfLength:]
    finalmsg = ''
    for i in range(halfLength):
        finalmsg += evenchar[i]
        finalmsg += oddchar[i]
    if len(oddchar) != len(evenchar):
        finalmsg += evenchar[halfLength]

    return finalmsg
            
        


if __name__ == "__main__":
    message = input("Give a message to encrypt: ")
    encryptedMessage = encryptStatement(message)
    print(encryptedMessage + " is your encrypted message. ")
    conditional = input("Decrypt the above?[y/n]: ")
    if conditional == 'y':
        print(decryptStatement(encryptStatement(message)))
    if conditional == 'n':
        print("You have your encryption. Use it wisely. o7 ")



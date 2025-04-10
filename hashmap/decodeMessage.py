
def decodeMessage(self, key: str, message: str) -> str:
    letters = dict();

    pos = 1;
    for i in key:
        if i not in " " and i not in letters:
            letters[i] = pos;
            pos += 1;


    decode = "";
    print(letters)
    for i  in message:
        if i not in " ":
             result =  chr(letters.get(i)+96)
             decode += result+""
        else:
            decode +=i;     
       
    return decode
        
    
 



print(decodeMessage(0,"the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))
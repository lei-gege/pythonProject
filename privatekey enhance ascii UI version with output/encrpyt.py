def encode1(pass_word, enhance1):
    neddle1 = 0
    neddle2 = 0
    outcome = []


    for z in range(len(enhance1)):    # just for enhance code does not need as long as password

        answer = ord(pass_word[neddle1]) + ord(enhance1[neddle2])    #conver letter to ascii and add them  #字母转为ascii 加上整数
        neddle1 += 1
        neddle2 += 1
        outcome.append(answer)
    return outcome

def encode2(pass_word, enhance1):
    outcome = []
    rest = pass_word[len(enhance1):len(pass_word)]    #if enhance is short than pass_word, add rest origin password to itself #enhance 短于 pass_word 加入剩余原本 pass_word.
    for y in rest:
        y = ord(y)

        outcome.append(y)
    return outcome


#decode just like reversal encode

def decode1(encrpyted_pass_word,enhance1):
    neddle1 = 0
    neddle2 = 0
    outcome = []

    for z in range(len(enhance1)):
        answer = ord(encrpyted_pass_word[neddle1]) - ord(enhance1[neddle2])
        neddle1 +=1
        neddle2 +=1
        outcome.append(answer)
    return outcome

def decode2(encrpyted_pass_word,enhance1):
    outcome=[]
    rest = encrpyted_pass_word[len(enhance1):len(encrpyted_pass_word)]
    for y in rest:
        y = ord(y)

        outcome.append(y)
    return outcome
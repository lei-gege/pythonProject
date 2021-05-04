# lei is seeking for a job!!

################### THIS IS ASCII ENCRYPT PROGRAM #################
from encrpyt import encode1,encode2,decode1,decode2
from asciiconvert import convert,deconvert

# put your password here
pass_word = "THIS IS MY PASSWORD,CanBe 898,!![]{}"
# put the content used to encrypt your password
enhance1 =  "this 1s my Enhance code,can..be<> "
# this is for decrypt your password,first time use, keep it empty, like this // encrpyted_pass_word =""
encrpyted_pass_word = "È°²Æ@zÆ@ºÒ@¯»´Å²·d²ÅÓnÈ¦gf]}{}"






if len(pass_word) !=0:
    while len(enhance1) > len(pass_word):

        print("please make sure enhance code is not longer than pass_word")
        break

    if len(enhance1) <= len(pass_word):
        final = encode1(pass_word, enhance1) + encode2(pass_word, enhance1)
        print("your original password:" + "  " + pass_word)
        print("your encrypted password:" + "  " + convert(final))

if len(encrpyted_pass_word) != 0:
    definal = decode1(encrpyted_pass_word,enhance1) + decode2(encrpyted_pass_word,enhance1)
    print("your decripted password:" + "  " + deconvert(definal))











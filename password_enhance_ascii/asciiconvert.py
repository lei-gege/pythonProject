def convert(final): #  convert ascii from list to letter string  #将ascii 码 从列表中 转为 字母 放入 string 中
    result = ''
    for i in final:
        i = chr(i)
        result += i
    return result

def deconvert(definal):
    result=''
    for i in definal:
        i = chr(i)
        result += i
    return result
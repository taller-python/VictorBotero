"""test function"""
def _eval_Palindroma(word):
    igual, aux = 0, 0
    for ind in reversed(range(0, len(word))):
        #print(ind)
        if word[ind].lower() == word[aux].lower():
            igual += 1
        aux += 1
    if len(word) == igual:
        print("TRUE! -- > "+word)
    else:
        print("FALSE! -- > "+word)
# linea nueva agregada
_eval_Palindroma("reconocer")

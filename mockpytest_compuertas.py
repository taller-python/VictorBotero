from compuertas import compuertOR
entrya = '1'
entryb = '0'
def test_compuertas():
    insCompuerta = compuertOR(entrya, entryb)
    returnTest = insCompuerta.evaluate()
    return returnTest

if entrya == test_compuertas():
    print ('iguales')
else:
    print ('DIFERENTES')
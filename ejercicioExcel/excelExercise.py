import xlrd

loc = ("\\configuration\\operaciones.xlsx")

def ExecuteSum(num1,num2):
    return num1+num2
def ExecuteRest(num1,num2):
    return num1-num2
def ExecuteMult(num1,num2):
    return num1*num2
def ExecuteDiv(num1,num2):
    return num1/num2

functionActions = {0:ExecuteSum, 
                    1:ExecuteRest, 
                    2: ExecuteMult,
                    3: ExecuteDiv
                    }
LabelActions = {0:'Suma', 
                    1:'Resta', 
                    2: 'Multiplicación',
                    3: 'División'
                    }

# evaluate the sum operation
try: 
    wb = xlrd.open_workbook(loc) 
    operation = 0
    while operation < 4:
        sheet = wb.sheet_by_index(operation) 
        print ('Operacion <'+ str(operation) )
        # For row 0 and column 0 
        sheet.cell_value(1, 0) 
        for i in range(sheet.nrows): 
            val1 = sheet.cell_value(i, 0)
            val2 = sheet.cell_value(i, 1)
            func = functionActions.get(operation)
            Calculo = func(val1,val2)
            print ('Row <'+str(i)+'>.  Operacion <'+ LabelActions.get(operation)+' > ==>'+str(Calculo) )
        operation = operation + 1

finally: 
    wb.__exit__
    
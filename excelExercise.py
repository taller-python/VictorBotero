import xlrd

loc = ("configuration/operaciones.xlsx")

def ExecuteSum(num1,num2):
    #return int(num1)+int(num2)
    try:
        valor1 = int(num1)
        valor2 = int(num2)
        valRetorno =valor1 + valor2
    except:
        valRetorno = 'Error'
    return valRetorno
def ExecuteRest(num1,num2):
    try:
        valor1 = int(num1)
        valor2 = int(num2)
        valRetorno =valor1 - valor2
    except:
        valRetorno = 'Error'
    return valRetorno
def ExecuteMult(num1,num2):
    try:
        valor1 = int(num1)
        valor2 = int(num2)
        valRetorno =valor1 * valor2
    except:
        valRetorno = 'Error'
    return valRetorno
def ExecuteDiv(num1,num2):
    try:
        valor1 = int(num1)
        valor2 = int(num2)
        valRetorno =valor1 / valor2
    except:
        valRetorno = 'Error'
    return valRetorno

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
    f= open("Operations.txt","w+")
    s_Datos = "============================== OPERACIONES ============================ \n"
    f.close()
    f= open("Operations.txt","a+")
    while operation < 4:
        sheet = wb.sheet_by_index(operation) 
        s_Datos = '====================== Operacion <'+ LabelActions.get(operation)+' > ======================\n'
        print ('====================== Operacion <'+ LabelActions.get(operation)+' > ======================' )
        # For row 0 and column 0 
        sheet.cell_value(1, 0) 
        for i in range(sheet.nrows): 
            if i == 0:
                continue
            val1 = sheet.cell_value(i, 0)
            val2 = sheet.cell_value(i, 1)
            func = functionActions.get(operation)
            Calculo = func(val1,val2)
            s_Datos = s_Datos + str(Calculo)+" \n"
            print ('    Row <'+str(i)+'>.  Operacion <'+ LabelActions.get(operation)+' > ==>'+str(Calculo) )
        f.write(s_Datos)
        operation = operation + 1
        
finally: 
    wb.__exit__
    f.close()
    
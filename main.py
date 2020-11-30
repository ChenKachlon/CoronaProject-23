import openpyxl

# Pointers to data base
wb = openpyxl.load_workbook("Hospital_Data_Base.xlsx")
ws = wb.worksheets[2]
ws_beds = wb.worksheets[1]

def Get_Row_Indicator(max_row):
    return max_row + 1

def ConvertToStr(columns,rows):
    """Convert row num and column num to str by excel format"""
    return str(chr(columns+64) + str(rows))

def Save_Data():
    """Save details in data base"""
    wb.save("Hospital_Data_Base.xlsx")

def add_patient():
    """Add patient to the data base"""
    row_location = Get_Row_Indicator(ws.max_row)
    patient_id = input("Please enter id: ")
    degree_of_difficulty = input("Please enter the degree of difficulty (mildly ill,medium ill,seriously ill,dying): ")
    ventilators = input("Need ventilator? (1-Yes,0-No): ")
    department = input("Department? ")
    data = [patient_id,degree_of_difficulty,ventilators,department]
    for i in range(4):
        ws[ConvertToStr(i+1,row_location)] = data[i]


def main():
    add_patient()
    Save_Data()

main()

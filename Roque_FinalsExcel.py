import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["A1"] = "Customer ID"
sheet["B1"] = "First Name"
sheet["C1"] = "Middle Name"
sheet["D1"] = "Last Name"
sheet["E1"] = "Age"
sheet["F1"] = "Height (In cm)"
sheet["G1"] = "Weight (In kg)"
sheet["G1"] = "BMI"
sheet["G1"] = "Streak Days"

# sheet["A2"] = 1
# sheet["B2"] = "Franz Gerald Roque"
# sheet["C2"] = 18
# sheet["D2"] = 167
# sheet["E2"] = 65
# sheet["F2"] = 23.3
# sheet["G2"] = 12

workbook.save("Roque_Database.xlsx")
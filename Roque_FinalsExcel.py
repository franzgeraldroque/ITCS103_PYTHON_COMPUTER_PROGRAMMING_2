import openpyxl as op

workbook = op.Workbook()
sheet = workbook.active

sheet["A1"] = "Customer ID"
sheet["B1"] = "Last Name"
sheet["C1"] = "First Name"
sheet["D1"] = "Middle Name"
sheet["E1"] = "Age"
sheet["F1"] = "Height (In cm)"
sheet["G1"] = "Weight (In kg)"
sheet["H1"] = "BMI"
sheet["I1"] = "Streak Days"

sheet["A2"] = 1
sheet["B2"] = "Roque"
sheet["C2"] = "Franz Gerald"
sheet["D2"] = "L."
sheet["E2"] = 18
sheet["F2"] = 167
sheet["G2"] = 65
sheet["H2"] = 23.3
sheet["I2"] = 1

workbook.save("Roque_Database.xlsx")

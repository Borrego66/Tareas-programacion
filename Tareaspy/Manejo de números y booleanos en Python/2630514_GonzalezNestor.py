"""
# Name: [NESTOR PATRICIO GONZALEZ CANO ]
# ID (Matricula): [2630514]
# Group: [IM1-2]
"""
"""
# EXECUTIVE SUMMARY
# =============================================================================
# En Python, los tipos 'int' (enteros) y 'float' (flotantes) representan datos
# numéricos; los primeros se usan para cantidades exactas y contadores, 
# mientras que los segundos manejan fracciones o decimales. Un booleano ('bool') 
# es un tipo de dato lógico que solo puede ser True o False, y se obtiene al 
# evaluar condiciones o comparaciones. Validar los rangos numéricos y evitar 
# la división entre cero es crucial para prevenir fallos en tiempo de ejecución
# o resultados ilógicos (como edades negativas). Este documento cubre la 
# resolución de 6 problemas, diseñando entradas, salidas y validaciones estrictas
# para procesar datos usando tipos numéricos y evaluar condiciones booleanas.
# =============================================================================

# =============================================================================
# PRINCIPLES AND BEST PRACTICES
# =============================================================================
# - Use appropriate types: int for counts/scores, float for money/measurements.
# - Avoid duplicating complex expressions: save intermediate results in variables.
# - Validate data before operating (e.g., negative hours, zero income).
# - Use descriptive variable names (lower_snake_case) and clear user messages.
# - Clearly document how booleans are interpreted (e.g., eligible = True).
"""

"""
# Problem 1: Temperature converter and range flag
# Description: Converts a temperature from Celsius to Fahrenheit and Kelvin.
# Evaluates a boolean flag if the temperature is 30.0 or higher.
#
# Inputs:
# - temp_c (float)
#
# Outputs:
# - "Fahrenheit:" <temp_f>
# - "Kelvin:" <temp_k>
# - "High temperature:" true|false
#
# Validations:
# - temp_c must be convertible to float.
# - temp_k must not be below absolute zero (0.0 K).
#
# Test cases:
# 1) Normal: temp_c = 25.0 (F: 77.0, K: 298.15, High: false)
# 2) Border: temp_c = 30.0 (F: 86.0, K: 303.15, High: true)
# 3) Error: temp_c = -300.0 (Error: invalid input, below absolute zero)
"""
print("--- Problem 1: Temperature converter ---")
try:
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_k = temp_c + 273.15
    
    if temp_k < 0.0:
        print("Error: invalid input (temperature below absolute zero)")
    else:
        temp_f = temp_c * 9 / 5 + 32
        is_high_temperature = (temp_c >= 30.0)
        
        print(f"Fahrenheit: {round(temp_f, 2)}")
        print(f"Kelvin: {round(temp_k, 2)}")
        print(f"High temperature: {str(is_high_temperature).lower()}")
except ValueError:
    print("Error: invalid input")


"""
# =============================================================================
# Problem 2: Work hours and overtime payment
# Description: Calculates weekly pay. Up to 40 hours at normal rate, remaining 
# hours at 150%. Generates a boolean flag if overtime was worked.
#
# Inputs:
# - hours_worked (float)
# - hourly_rate (float)
#
# Outputs:
# - "Regular pay:" <regular_pay>
# - "Overtime pay:" <overtime_pay>
# - "Total pay:" <total_pay>
# - "Has overtime:" true|false
#
# Validations:
# - hours_worked >= 0
# - hourly_rate > 0
#
# Test cases:
# 1) Normal: hours=45, rate=10 (Regular: 400.0, Overtime: 75.0, Total: 475.0, Has overtime: true)
# 2) Border: hours=40, rate=15 (Regular: 600.0, Overtime: 0.0, Total: 600.0, Has overtime: false)
# 3) Error: hours=-5, rate=10 (Error: invalid input)
"""
print("\n--- Problem 2: Work hours and overtime ---")
try:
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))
    
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        MAX_REGULAR_HOURS = 40.0
        OVERTIME_MULTIPLIER = 1.5
        
        regular_hours = min(hours_worked, MAX_REGULAR_HOURS)
        overtime_hours = max(0.0, hours_worked - MAX_REGULAR_HOURS)
        
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_MULTIPLIER
        total_pay = regular_pay + overtime_pay
        
        has_overtime = (hours_worked > MAX_REGULAR_HOURS)
        
        print(f"Regular pay: {round(regular_pay, 2)}")
        print(f"Overtime pay: {round(overtime_pay, 2)}")
        print(f"Total pay: {round(total_pay, 2)}")
        print(f"Has overtime: {str(has_overtime).lower()}")
except ValueError:
    print("Error: invalid input")


"""
# Problem 3: Discount eligibility with booleans
# Description: Checks if a user gets a 10% discount based on student status, 
# senior status, or high purchase total (>= 1000). Calculates final total.
#
# Inputs:
# - purchase_total (float)
# - is_student_text (string)
# - is_senior_text (string)
#
# Outputs:
# - "Discount eligible:" true|false
# - "Final total:" <final_total>
#
# Validations:
# - purchase_total >= 0.0
# - string inputs must be strictly "YES" or "NO" (case-insensitive).
#
# Test cases:
# 1) Normal: total=500, student="YES", senior="NO" (Eligible: true, Final: 450.0)
# 2) Border: total=1000, student="NO", senior="NO" (Eligible: true, Final: 900.0)
# 3) Error: total=200, student="MAYBE", senior="NO" (Error: invalid input)
"""
print("\n--- Problem 3: Discount eligibility ---")
try:
    purchase_total = float(input("Enter purchase total: "))
    is_student_text = input("Are you a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Are you a senior? (YES/NO): ").strip().upper()
    
    valid_responses = ["YES", "NO"]
    
    if purchase_total < 0.0 or is_student_text not in valid_responses or is_senior_text not in valid_responses:
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")
        
        DISCOUNT_THRESHOLD = 1000.0
        DISCOUNT_RATE = 0.90
        
        discount_eligible = is_student or is_senior or (purchase_total >= DISCOUNT_THRESHOLD)
        
        if discount_eligible:
            final_total = purchase_total * DISCOUNT_RATE
        else:
            final_total = purchase_total
            
        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {round(final_total, 2)}")
except ValueError:
    print("Error: invalid input")


"""
# Problem 4: Basic statistics of three integers
# Description: Reads three integers and calculates their sum, average, max, min,
# and checks if all of them are even numbers.
#
# Inputs:
# - n1, n2, n3 (int)
#
# Outputs:
# - "Sum:" <sum_value>
# - "Average:" <average_value>
# - "Max:" <max_value>
# - "Min:" <min_value>
# - "All even:" true|false
#
# Validations:
# - Inputs must be convertible to int. Negatives are allowed.
#
# Test cases:
# 1) Normal: n1=2, n2=4, n3=6 (Sum: 12, Avg: 4.0, Max: 6, Min: 2, All even: true)
# 2) Border: n1=-1, n2=0, n3=1 (Sum: 0, Avg: 0.0, Max: 1, Min: -1, All even: false)
# 3) Error: n1="two", n2=4, n3=6 (Error: invalid input)
"""
print("\n--- Problem 4: Basic statistics ---")
try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))
    
    sum_value = n1 + n2 + n3
    average_value = float(sum_value) / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Sum: {sum_value}")
    print(f"Average: {round(average_value, 2)}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {str(all_even).lower()}")
except ValueError:
    print("Error: invalid input")


"""
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Evaluates a person's loan eligibility based on monthly income,
# monthly debt, and credit score. Calculates the debt ratio.
#
# Inputs:
# - monthly_income (float)
# - monthly_debt (float)
# - credit_score (int)
#
# Outputs:
# - "Debt ratio:" <debt_ratio>
# - "Eligible:" true|false
#
# Validations:
# - monthly_income > 0.0 (prevents division by zero)
# - monthly_debt >= 0.0
# - credit_score >= 0
#
# Test cases:
# 1) Normal: income=10000, debt=3000, score=700 (Ratio: 0.3, Eligible: true)
# 2) Border: income=8000, debt=3200, score=650 (Ratio: 0.4, Eligible: true)
# 3) Error: income=0, debt=1000, score=600 (Error: invalid input)
"""
print("\n--- Problem 5: Loan eligibility ---")
try:
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))
    
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        MIN_INCOME = 8000.0
        MAX_DEBT_RATIO = 0.4
        MIN_SCORE = 650
        
        debt_ratio = monthly_debt / monthly_income
        
        eligible = (monthly_income >= MIN_INCOME) and (debt_ratio <= MAX_DEBT_RATIO) and (credit_score >= MIN_SCORE)
        
        print(f"Debt ratio: {round(debt_ratio, 2)}")
        print(f"Eligible: {str(eligible).lower()}")
except ValueError:
    print("Error: invalid input")


"""
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Calculates the BMI and sets boolean flags for underweight, 
# normal weight, and overweight categories.
#
# Inputs:
# - weight_kg (float)
# - height_m (float)
#
# Outputs:
# - "BMI:" <bmi>
# - "Underweight:" true|false
# - "Normal:" true|false
# - "Overweight:" true|false
#
# Validations:
# - weight_kg > 0.0
# - height_m > 0.0
#
# Test cases:
# 1) Normal: weight=70.0, height=1.75 (BMI: 22.86, Under: false, Normal: true, Over: false)
# 2) Border: weight=60.0, height=1.80 (BMI: 18.52, Under: false, Normal: true, Over: false)
# 3) Error: weight=75.0, height=0.0 (Error: invalid input)
"""
print("\n--- Problem 6: BMI categories ---")
try:
    weight_kg = float(input("Enter weight in kg: "))
    height_m = float(input("Enter height in meters: "))
    
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        
        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)
        
        print(f"BMI: {round(bmi, 2)}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")
except ValueError:
    print("Error: invalid input")


"""
# CONCLUSIONS
# =============================================================================
# A través de estos ejercicios comprobamos que 'int' y 'float' trabajan en 
# conjunto para dar precisión en cálculos del mundo real, desde nóminas hasta
# estadísticas. Las comparaciones numéricas devuelven booleanos que actúan 
# como "banderas", permitiendo construir árboles de decisión (if/else).
# Es vital validar que valores como denominadores o estaturas sean mayores 
# a cero para evitar excepciones matemáticas letales en nuestro programa. 
# El uso de operadores lógicos (and, or, not) resulta sumamente eficiente para
# combinar múltiples requisitos financieros o de negocios en una sola línea.
# =============================================================================

# =============================================================================
# REFERENCES
# =============================================================================
# 1) Python documentation - Built-in Types: Numeric Types — int, float, complex
#    (https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
# 2) Python documentation - Boolean type — bool
#    (https://docs.python.org/3/library/stdtypes.html#boolean-type-bool)
# 3) Real Python - "Python Booleans: Use Truth Values in Your Code" 
#    (https://realpython.com/python-boolean/)
# 4) W3Schools - Python Operators (Arithmetic, Assignment, Comparison, Logical)
#    (https://www.w3schools.com/python/python_operators.asp)
# 5) "Python for Everybody: Exploring Data Using Python 3" - Dr. Charles Severance
"""


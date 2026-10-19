"""
# Name: [NESTOR PATRICIO GONZALEZ CANO ]
# ID (Matricula): [2630514]
# Group: [IM1-2]
# =============================================================================

# =============================================================================
# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
# =============================================================================
# En Python, una lista es una colección ordenada y mutable, lo que significa
# que podemos agregar, eliminar o modificar sus elementos en cualquier momento.
# Una tupla es similar a una lista (es ordenada), pero es inmutable; sus datos
# no pueden cambiar una vez definidos, lo que las hace seguras para datos fijos.
# Un diccionario es una estructura que asocia datos en pares clave-valor, 
# permitiendo búsquedas sumamente rápidas usando una clave única.
# 
# Este documento cubrirá la resolución de 6 problemas prácticos. Se incluirá
# la descripción, diseño de entradas y salidas, así como las validaciones 
# necesarias para cada uno. Se demostrará el uso de listas, tuplas y diccionarios 
# en contextos como catálogos de productos, registro de calificaciones, 
# estadísticas de palabras y agendas de contactos.
#
# PRINCIPIOS Y BUENAS PRÁCTICAS:
# - Usar listas cuando necesites agregar o eliminar elementos con frecuencia.
# - Usar tuplas para datos que no deben cambiar (coordenadas, fechas, etc.).
# - Usar diccionarios cuando necesites buscar información por una clave (nombre, id).
# - Evitar modificar una lista mientras la recorres con un bucle for.
# - Usar nombres de claves descriptivos en los diccionarios ("name", "age", "price").
# - Escribir código legible y mensajes claros para el usuario final.
# =============================================================================


# =============================================================================
# Problem 1: Shopping list basics (list operations)
# =============================================================================
# Description: Creates a shopping list from a string, allows adding a new item,
# counts total items, and checks if a specific item exists in the list.
#
# Inputs:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
#
# Outputs:
# - "Items list:" <items_list>
# - "Total items:" <len_list>
# - "Found item:" true|false
#
# Validations:
# - Check if initial_items_text is not empty after strip().
# - Check if new_item and search_item are not empty.
#
# Test cases:
# 1) Normal: initial="apple, banana", new="orange", search="apple"
# 2) Border: initial="   milk   ", new="bread", search="water"
# 3) Error: initial="", new="", search="apple" (Should show error messages)
"""

print("--- Problem 1 ---")
initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter a new item to add: ").strip()
search_item = input("Enter an item to search for: ").strip()

if not initial_items_text:
    print("Error: invalid input, initial items cannot be empty.")
    items_list = []
else:
    # Separar por comas y eliminar espacios de cada elemento
    items_list = [item.strip() for item in initial_items_text.split(",")]

if not new_item or not search_item:
    print("Error: invalid input, new item and search item cannot be empty.")
else:
    if initial_items_text:
        items_list.append(new_item)
        
    is_in_list = search_item in items_list
    
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", str(is_in_list).lower())


"""
# Problem 2: Points and distances with tuples
# =============================================================================
# Description: Uses tuples to represent two 2D points, calculates the 
# Euclidean distance between them, and finds their midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - "Point A:" (x1, y1)
# - "Point B:" (x2, y2)
# - "Distance:" <distance>
# - "Midpoint:" (mx, my)
#
# Validations:
# - Ensure that the inputs can be converted to float.
#
# Test cases:
# 1) Normal: x1=0, y1=0, x2=3, y2=4 (Distance: 5.0, Mid: 1.5, 2.0)
# 2) Border: x1=-1.5, y1=-1.5, x2=-1.5, y2=-1.5 (Distance: 0.0, Mid: -1.5, -1.5)
# 3) Error: x1="a", y1=0, x2=1, y2=1 (Throws validation error)
"""

print("\n--- Problem 2 ---")
try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2)/2, (y1 + y2)/2)
    
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", round(distance, 4))
    print("Midpoint:", midpoint)
    
except ValueError:
    print("Error: invalid input, coordinates must be numeric.")


"""
# Problem 3: Product catalog with dictionary
# =============================================================================
# Description: Manages a small catalog of products. Reads a product name and
# quantity, and calculates the total price if the product exists.
#
# Inputs:
# - product_name (string)
# - quantity (int)
#
# Outputs:
# - "Unit price:" <unit_price>
# - "Quantity:" <quantity>
# - "Total:" <total_price>
# - "Error: product not found" (if not in dict)
#
# Validations:
# - quantity > 0
# - product_name is not empty
# - product_name exists in dictionary keys
#
# Test cases:
# 1) Normal: product_name="apple", quantity=3 (Total: 4.5)
# 2) Border: product_name="milk", quantity=1 (Total: 2.5)
# 3) Error: product_name="steak", quantity=2 (Error: product not found)
"""

print("\n--- Problem 3 ---")
product_prices = {
    "apple": 1.5,
    "bread": 2.0,
    "milk": 2.5,
    "eggs": 3.0
}

product_name = input("Enter product name: ").strip().lower()

try:
    quantity = int(input("Enter quantity: "))
    if not product_name or quantity <= 0:
        print("Error: invalid input")
    else:
        if product_name in product_prices:
            unit_price = product_prices[product_name]
            total_price = unit_price * quantity
            
            print("Unit price:", unit_price)
            print("Quantity:", quantity)
            print("Total:", total_price)
        else:
            print("Error: product not found")
except ValueError:
    print("Error: invalid quantity")


"""
# Problem 4: Student grades with dict and list
# =============================================================================
# Description: Manages student grades using a dictionary of lists. Calculates 
# a student's average and determines if they passed (average >= 70).
#
# Inputs:
# - student_name (string)
#
# Outputs:
# - "Grades:" <grades_list>
# - "Average:" <average>
# - "Passed:" true|false
# - "Error: student not found"
#
# Validations:
# - student_name is not empty
# - student_name exists in dictionary
# - grades list is not empty before calculating average
#
# Test cases:
# 1) Normal: student="Alice" (Average: 87.5, Passed: true)
# 2) Border: student="Bob" (Average: 70.0, Passed: true)
# 3) Error: student="David" (Error: student not found)
"""
print("\n--- Problem 4 ---")
PASSING_GRADE = 70.0
student_grades = {
    "alice": [90.0, 85.0],
    "bob": [70.0, 70.0],
    "charlie": [50.0, 60.0],
    "empty_student": []
}

student_name = input("Enter student name: ").strip().lower()

if not student_name:
    print("Error: invalid input")
else:
    if student_name in student_grades:
        grades_list = student_grades[student_name]
        
        if len(grades_list) == 0:
            print("Error: student has no grades to average")
        else:
            average = sum(grades_list) / len(grades_list)
            is_passed = average >= PASSING_GRADE
            
            print("Grades:", grades_list)
            print("Average:", round(average, 2))
            print("Passed:", str(is_passed).lower())
    else:
        print("Error: student not found")


""""
# Problem 5: Word frequency counter (list + dict)
# =============================================================================
# Description: Counts the frequency of each word in a given sentence,
# stores it in a dictionary, and finds the most common word.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Words list:" <words_list>
# - "Frequencies:" <freq_dict>
# - "Most common word:" <word>
#
# Validations:
# - sentence is not empty after strip
# - handles basic punctuation by replacing it
#
# Test cases:
# 1) Normal: "hello world hello python" (Most common: hello)
# 2) Border: "word" (Most common: word, Freqs: {'word': 1})
# 3) Error: "    " (Error: invalid input)
"""
print("\n--- Problem 5 ---")
sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input")
else:
    # Limpieza básica de puntuación
    clean_sentence = sentence.replace(".", "").replace(",", "").lower()
    words_list = clean_sentence.split()
    
    if not words_list:
        print("Error: list is empty")
    else:
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
                
        # Buscar la palabra más frecuente
        most_common_word = ""
        max_count = 0
        for word, count in freq_dict.items():
            if count > max_count:
                most_common_word = word
                max_count = count
                
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)


"""
# Problem 6: Simple contact book (dictionary CRUD)
# =============================================================================
# Description: Implements a basic contact book. Reads an action (ADD, SEARCH, 
# DELETE) and modifies/reads the dictionary accordingly.
#
# Inputs:
# - action_text (string)
# - name (string)
# - phone (string, only if ADD)
#
# Outputs:
# - "Contact saved:" name, phone
# - "Phone:" <phone> or "Error: contact not found"
# - "Contact deleted:" name or "Error: contact not found"
#
# Validations:
# - Normalize action_text to uppercase
# - Verify action is valid
# - name is not empty
# - phone is not empty (for ADD)
#
# Test cases:
# 1) Normal: ADD, name="John", phone="123" -> SEARCH "John" -> DELETE "John"
# 2) Border: SEARCH, name="Unknown" (Error: contact not found)
# 3) Error: action="UPDATE" (Error: invalid action)
"""

print("\n--- Problem 6 ---")
contacts = {
    "alice": "1234567890",
    "bob": "9876543210"
}

action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Enter contact name: ").strip().lower()
    if not name:
        print("Error: invalid name")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if not phone:
                print("Error: invalid phone")
            else:
                contacts[name] = phone
                print(f"Contact saved: {name}, {phone}")
                
        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")
                
        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")


"""
# CONCLUSIONS / CONCLUSIONES
# =============================================================================
# A lo largo del desarrollo de estos problemas, resulta evidente que elegir 
# la estructura de datos correcta simplifica enormemente la lógica del código.
# Las listas brindan flexibilidad para secuencias dinámicas, como la lista 
# de compras o el conteo de palabras. Las tuplas proporcionan seguridad para 
# valores que no deben alterarse (como coordenadas en el plano 2D). Por su 
# parte, los diccionarios resultan indispensables para crear mapeos y catálogos, 
# garantizando búsquedas e inserciones eficientes por clave.
# =============================================================================

# =============================================================================
# REFERENCES / REFERENCIAS
# =============================================================================
# 1) Python Software Foundation. "Built-in Types: list, tuple, dict." Python Docs.
# 2) Severance, C. (2016). "Python for Everybody: Exploring Data Using Python 3."
# 3) Sweigart, A. (2019). "Automate the Boring Stuff with Python." No Starch Press.
# 4) Real Python. "Dictionaries in Python." https://realpython.com/python-dicts/
# 5) W3Schools. "Python Data Types." https://www.w3schools.com/python/python_datatypes.asp
"""


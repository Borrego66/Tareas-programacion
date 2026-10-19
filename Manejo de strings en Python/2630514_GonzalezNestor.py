"""
# Name: [Tu Nombre / Your Name]
# ID (Matricula): [Tu Matricula / Your ID]
# Group: [Tu Grupo / Your Group]
# File: matricula_ApellidoNombre_t_strings.py
# =============================================================================

# =============================================================================
# 4. RESUMEN EJECUTIVO
# =============================================================================
# En Python, un string (tipo `str`) es una secuencia inmutable de caracteres; 
# esto significa que una vez creado, no puede modificarse, sino que cualquier 
# operación genera una nueva cadena. Las operaciones básicas incluyen concatenar 
# (+), obtener longitud (len()), extraer sub-cadenas (slicing), buscar (find, in) 
# y reemplazar (replace). Es vital validar y normalizar el texto de entrada 
# (por ejemplo, correos o nombres) para evitar errores de procesamiento y 
# garantizar la integridad de los datos. Este documento aborda seis problemas 
# prácticos utilizando métodos de string para limpieza, validación, búsqueda 
# de palíndromos, estadísticas de palabras, seguridad de contraseñas y 
# formateo de etiquetas de ancho fijo.
# =============================================================================

# =============================================================================
# 5. PRINCIPIOS Y BUENAS PRÁCTICAS
# =============================================================================
# - Los strings son inmutables: métodos como replace() devuelven una nueva cadena.
# - Es fundamental normalizar entradas con strip() y lower() antes de compararlas.
# - Se debe evitar el uso de "números mágicos" en los índices; el uso de slicing 
#   debe ser claro y documentado.
# - Preferir métodos integrados de string (isupper, split) sobre lógica manual.
# - El flujo de validación ideal es: comprobar que no esté vacío, luego el formato.
# - Escribir código con nombres descriptivos (lower_snake_case) y mensajes de error claros.
"""


"""
# Problem 1: Full name formatter (name + initials)
# Description: Normalizes a full name, converts it to Title Case, and 
# extracts its initials separated by dots.
#
# Inputs:
# - full_name (string)
#
# Outputs:
# - "Formatted name: <Title Case Name>"
# - "Initials: <X.X.X.>"
#
# Validations:
# - full_name is not empty after strip().
# - Contains at least two words.
#
# Test cases:
# 1) Normal: full_name=" juan  carlos tovar " -> J.C.T.
# 2) Border: full_name="ana   lee" -> A.L.
# 3) Error: full_name="   " or "john" -> Error: invalid input (needs 2 words)
"""
print("--- Problem 1: Full name formatter ---")
full_name = input("Enter your full name: ").strip()

if not full_name:
    print("Error: invalid input (empty string)")
else:
    name_parts = full_name.split()
    if len(name_parts) < 2:
        print("Error: invalid input (must contain at least two words)")
    else:
        # Formatted name in Title Case
        formatted_name = " ".join([word.title() for word in name_parts])
        # Extract initials
        initials = "".join([word[0].upper() + "." for word in name_parts])
        
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")


"""
# Problem 2: Simple email validator (structure + domain)
# Description: Validates basic email format (exactly one '@', at least one 
# '.' after '@', no spaces) and extracts the domain.
#
# Inputs:
# - email_text (string)
#
# Outputs:
# - "Valid email: true|false"
# - "Domain: <domain_part>" (if valid)
#
# Validations:
# - email_text is not empty.
# - Exactly one '@'.
# - No spaces in the email.
# - At least one '.' after the '@'.
#
# Test cases:
# 1) Normal: email_text="user@example.com" -> Valid: true, Domain: example.com
# 2) Border: email_text="a@b.c" -> Valid: true, Domain: b.c
# 3) Error: email_text="user @ domain.com" -> Valid: false (spaces present)
"""
print("\n--- Problem 2: Simple email validator ---")
email_text = input("Enter your email: ").strip()

if not email_text:
    print("Error: invalid input (empty string)")
else:
    is_valid = True
    
    if email_text.count("@") != 1:
        is_valid = False
    elif " " in email_text:
        is_valid = False
    else:
        at_index = email_text.find("@")
        # Check if there's a dot after the '@'
        if email_text.find(".", at_index) == -1:
            is_valid = False
            
    print(f"Valid email: {str(is_valid).lower()}")
    if is_valid:
        domain_part = email_text[at_index + 1:]
        print(f"Domain: {domain_part}")


"""
# Problem 3: Palindrome checker (ignoring spaces and case)
# Description: Checks if a phrase reads the same forwards and backwards, 
# ignoring spaces and letter casing.
#
# Inputs:
# - phrase (string)
#
# Outputs:
# - "Is palindrome: true|false"
# - "Normalized: <normalized_phrase>"
#
# Validations:
# - phrase is not empty.
# - Length >= 3 after removing spaces.
#
# Test cases:
# 1) Normal: phrase="Anita lava la tina" -> true
# 2) Border: phrase="  A b a  " -> true
# 3) Error: phrase="hi" -> Error: invalid input (length < 3)
"""
print("\n--- Problem 3: Palindrome checker ---")
phrase = input("Enter a phrase: ").strip()

if not phrase:
    print("Error: invalid input (empty string)")
else:
    normalized_phrase = phrase.replace(" ", "").lower()
    
    if len(normalized_phrase) < 3:
        print("Error: invalid input (phrase too short after cleaning)")
    else:
        # Reverse string using slicing
        reversed_phrase = normalized_phrase[::-1]
        is_palindrome = (normalized_phrase == reversed_phrase)
        
        print(f"Normalized: {normalized_phrase}")
        print(f"Is palindrome: {str(is_palindrome).lower()}")


"""
# Problem 4: Sentence word stats (lengths and first/last word)
# Description: Analyzes a sentence to find word count, first/last words, 
# and the shortest/longest words by length.
#
# Inputs:
# - sentence (string)
#
# Outputs:
# - "Word count: <n>"
# - "First word: <...>"
# - "Last word: <...>"
# - "Shortest word: <...>"
# - "Longest word: <...>"
#
# Validations:
# - sentence not empty.
# - Must contain at least one word.
#
# Test cases:
# 1) Normal: sentence="Python is a powerful language" -> count: 5, longest: powerful
# 2) Border: sentence="Hello" -> count: 1, first/last/shortest/longest: Hello
# 3) Error: sentence="   " -> Error: invalid input
"""
print("\n--- Problem 4: Sentence word stats ---")
sentence = input("Enter a sentence: ").strip()

if not sentence:
    print("Error: invalid input (empty string)")
else:
    words = sentence.split()
    if not words:
        print("Error: invalid input (no words found)")
    else:
        word_count = len(words)
        first_word = words[0]
        last_word = words[-1]
        
        shortest_word = words[0]
        longest_word = words[0]
        
        for w in words:
            if len(w) < len(shortest_word):
                shortest_word = w
            if len(w) > len(longest_word):
                longest_word = w
                
        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")


"""
# Problem 5: Password strength classifier
# Description: Evaluates a password and classifies it as weak, medium, or strong.
# Rules: 
# - Weak: length < 8.
# - Strong: length >= 8 AND contains at least one uppercase, one lowercase, 
#   one digit, and one special character (non-alphanumeric).
# - Medium: length >= 8 but doesn't meet all strong criteria.
#
# Inputs:
# - password_input (string)
#
# Outputs:
# - "Password strength: <weak/medium/strong>"
#
# Validations:
# - Password cannot be empty.
#
# Test cases:
# 1) Normal (Strong): "SecureP@ss1" -> strong
# 2) Border (Medium): "password123" -> medium (no uppercase/special)
# 3) Error (Weak): "abc" -> weak (length < 8)
"""
print("\n--- Problem 5: Password strength classifier ---")
password_input = input("Enter a password: ")

if not password_input:
    print("Error: invalid input (password cannot be empty)")
else:
    if len(password_input) < 8:
        strength = "weak"
    else:
        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False
        
        for char in password_input:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_special = True
                
        if has_upper and has_lower and has_digit and has_special:
            strength = "strong"
        else:
            strength = "medium"
            
    print(f"Password strength: {strength}")


"""
# Problem 6: Product label formatter (fixed-width text)
# Description: Generates a fixed-width 30-character label containing the 
# product name and price. Truncates if too long, pads with spaces if too short.
#
# Inputs:
# - product_name (string)
# - price_value (string converted to float for validation)
#
# Outputs:
# - "Label: '<exactly 30 chars>'"
#
# Validations:
# - product_name is not empty.
# - price_value must be a positive number.
#
# Test cases:
# 1) Normal (padding): name="Apple", price="1.5" -> "Product: Apple | Price: $1.5  "
# 2) Border (truncating): name="Super Ultra Mega Product", price="10" -> "Product: Super Ultra Mega Prod"
# 3) Error: name="", price="-5" -> Error: invalid input
"""

print("\n--- Problem 6: Product label formatter ---")
product_name = input("Enter product name: ").strip()

try:
    price_input = input("Enter product price: ").strip()
    price_value = float(price_input)
    
    if not product_name or price_value < 0:
        print("Error: invalid input")
    else:
        # Generate the base string
        raw_label = f"Product: {product_name} | Price: ${price_value}"
        TARGET_LENGTH = 30
        
        # Apply truncation or padding
        if len(raw_label) > TARGET_LENGTH:
            final_label = raw_label[:TARGET_LENGTH]
        else:
            # Pad with spaces at the end
            padding = " " * (TARGET_LENGTH - len(raw_label))
            final_label = raw_label + padding
            
        print(f"Label: '{final_label}'")
        print(f"Length: {len(final_label)}")
        
except ValueError:
    print("Error: invalid input (price must be numeric)")


"""
# 8. CONCLUSIONES
# =============================================================================
# El manejo de strings es la principal línea de defensa en la entrada de datos.
# Entender la inmutabilidad de los strings en Python nos enseña que funciones 
# como lower() o replace() no alteran la cadena original, sino que generan una 
# nueva. Operaciones como strip() y lower() son indispensables para normalizar 
# texto antes de comparaciones (ej. buscar palíndromos o correos), evitando
# fallos por espacios accidentales o mayúsculas. Diseñar validaciones estrictas
# previene la inyección de datos basura, y el uso correcto del "slicing" 
# facilita enormemente la extracción y formateo de sub-cadenas.
# =============================================================================

# =============================================================================
# 9. REFERENCIAS
# =============================================================================
# 1) Python documentation - Built-in Types: Text Sequence Type — str
#    (https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
# 2) Real Python - "Python String Formatting Best Practices"
#    (https://realpython.com/python-string-formatting/)
# 3) W3Schools - Python String Methods
#    (https://www.w3schools.com/python/python_ref_string.asp)
# 4) "Python for Everybody" - Dr. Charles Severance (Chapter on Strings)
# 5) Programiz - "Python Strings: Creation, Slicing & Methods"
#    (https://www.programiz.com/python-programming/string)
"""
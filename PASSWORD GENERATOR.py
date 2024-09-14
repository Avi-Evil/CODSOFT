import random
import string

alphabet_lower=string.ascii_lowercase 
# string.ascii_lowercase inserts the alphabet in lower case
alphabet_upper=string.ascii_uppercase
# string.ascii_uppercase inserts the alphabet in upper case means in capital
symbol_glyph=string.punctuation
# string.punctuation inserts punctuation marks 
digit_glyph=string.digits
# string.digits inserts digits or numeric values

def generate_password(length,complexity):
    if complexity=="low":
        alphabet_combintion=alphabet_lower
    elif complexity=="medium":
        alphabet_combintion=alphabet_lower+alphabet_upper
    elif complexity=="high":
        alphabet_combintion=alphabet_lower+alphabet_upper+symbol_glyph+digit_glyph
    else:
        print("Invalid complexity input. choose 'low','medium','high'")
    
    password=''.join(random.choices(alphabet_combintion,k=length))
    #password=''.join(random.choices(alphabet_combintion,k=length)),
    # creates password by joining all alphabet_combination with lenght=k

    return password


length=int(input("Enter the length of password required:"))
complexity=input("Choose the complexity of password('low','medium','high'):")
password=generate_password(length,complexity)
print(f"Generated password is {password}.")

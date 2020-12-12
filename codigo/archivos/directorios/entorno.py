
import os

"""El modulo os tambien provee de un diccionario con las variables de entorno relativas al sistema
   Se trata del diccionario envirom 
"""

for variable, valor in os.environ.items():
    print("%s: %s" %(variable, valor))
    

print(os)

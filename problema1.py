from io import open
from typing import Text

archivo_texto=open ("mi_text.txt" , "w")


Frase= "¡ Pequeño demonio! \n ¡ Eres un...!"

archivo_texto.write(Frase)


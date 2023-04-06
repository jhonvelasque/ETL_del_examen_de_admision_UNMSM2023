import barcode
from barcode import EAN13
from barcode.writer import ImageWriter

def codigo_barra(codigo):
    return str(codigo)+"0"*(12-len(str(codigo)))

numeros=[codigo_barra(i) for i in range(1,10)]
def generar_imagenes_barra(codigo,numeros):
    lista_numero =[]
    for item in numeros:
        with open(f"{item}.jpge", 'wb') as codigo_barra:
            EAN13.write(item, writer=ImageWriter()).write(codigo_barra)

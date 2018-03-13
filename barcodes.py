import barcode
from barcode.writer import ImageWriter

def generate(size):
    '''Generar lista de barcodes (strings) de tamaño `size`.'''

    seed = '00001234000'    
    barcode_list = []
    for i in range(1,size+1):
        code = str(i) + seed
        bcode = barcode.get('ean', code[0:12])
        barcode_list.append(bcode.get_fullcode())

    return barcode_list

# checar que ningún código se repita
# print(len(set(generate(800)))) # ok

def generate_png(n):
    '''Generar `n` códigos de barra (imágenes).'''

    seed = '00001234000'    
    for i in range(1,size+1):
        code = str(i) + seed
        bcode = barcode.get('ean', code[0:12], writer=ImageWriter())

        filename = 'barcode_' + bcode.get_fullcode()
        bcode.default_writer_options['quiet_zone'] = 1.0
        bcode.save(filename)

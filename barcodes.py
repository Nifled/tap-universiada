# TODO : Move somewhere else. e.g. in comidas/ dir

import barcode
from barcode.writer import ImageWriter


def generate_barcode_list(size):
    """Generar lista de barcodes (strings) de tamaño `size`."""

    seed = '00001234000'
    barcode_list = []
    for i in range(1, size + 1):
        code = str(i) + seed
        b_code = barcode.get('ean', code[0:12])
        barcode_list.append(b_code.get_fullcode())

    return barcode_list


# checar que ningún código se repita, etc
# print(len(set(generate(800)))) # ok


def generate_png(n):
    """Generar `n` códigos de barra (imágenes)."""

    seed = '00001234000'
    for i in range(1, n + 1):
        code = str(i) + seed
        b_code = barcode.get('ean', code[0:12], writer=ImageWriter())

        filename = 'barcode_' + b_code.get_fullcode()
        b_code.default_writer_options['quiet_zone'] = 1.0
        b_code.save(filename)


if __name__ == "__main__":
    # Para probar, correr solo este archivo e.g.
    # `docker-compose -f compose-local.yml run web python barcodes.py`
    b_list = generate_barcode_list(3)
    print(b_list)
    generate_png(3)

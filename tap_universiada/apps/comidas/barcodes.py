# TODO : Move somewhere else. e.g. in comidas/ dir

from django.conf import settings
import barcode
from barcode.writer import ImageWriter
from imgurpython import ImgurClient

client_id = 'e7ac6ee4153e3ab'
client_secret = '2fe03c77f8b37592ec2afe128d803aeaeda2c902'

Imgur = ImgurClient(client_id, client_secret)


def generate_one(seed):
    """Funcion para generar barcode al crear un participante. Regresa el barcode (string) y link de imgur."""
    b_code = barcode.get('ean', seed, writer=ImageWriter())
    b_code_str = b_code.get_fullcode()

    # png file
    filename = 'barcode_' + b_code_str
    b_code.default_writer_options['quiet_zone'] = 1.0
    b_code.save(filename)

    # upload to imgur
    path_to_file = '{}/{}.png'.format(settings.BASE_DIR, filename)
    imgur_link = Imgur.upload_from_path(path_to_file, anon=True)['link']
    print(imgur_link)

    return b_code_str, imgur_link


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
        
        imgur_link = Imgur.upload_from_path(filename + '.png', anon=True)['link']
        print(imgur_link)


if __name__ == "__main__":
    # Para probar, correr solo este archivo e.g.
    # `docker-compose -f compose-local.yml run web python barcodes.py`
    b_list = generate_barcode_list(3)
    print(b_list)
    generate_png(1)

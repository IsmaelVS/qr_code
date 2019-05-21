# coding: utf-8
import pyqrcode

text = raw_input('Digite o texto para geração do Qrcode: ')
image = raw_input('Digite o nome desejado para salvar a imagem: ')

code = pyqrcode.create('{}'.format(text))

code.png('{}.png'.format(image), scale=6)

if code != 0:
    print('Deu bom!!')

from pathlib import Path
import PySimpleGUI as sg
import io, os
from PIL import Image, ImageFilter, ImageEnhance
from numpy import asarray

def errorWindow(message):
    sg.Popup(message, title='Erro', auto_close=True, custom_text='Fechar', any_key_closes=True, keep_on_top=True)

def updateOriginalImage(window, imageData):
    bio = io.BytesIO()
    Image.fromarray(imageData).save(bio, format="PNG") 
    window["-IMG-"].update(data=bio.getvalue())

def updateEditedImage(window, imageData):
    bio = io.BytesIO()
    Image.fromarray(imageData).save(bio, format="PNG") 
    window["-EDITED_IMG-"].update(data=bio.getvalue())

def abrir(window):
    filename = sg.PopupGetFile('', no_window = True)
    if os.path.exists(filename):
        imageData = asarray(Image.open(filename))
        updateOriginalImage(window, imageData)
        updateEditedImage(window, imageData)
        return imageData
    return []

def save(imageData):
    if not len(imageData) > 0:
        errorWindow('Não existe imagem a ser salva') 
    else:
        filename = sg.popup_get_file('',save_as=True, file_types=(("PNG Files", "*.png"),), no_window=True)
        if os.path.exists(filename[:filename.rfind("/") + 1]):
            Image.fromarray(imageData).save(filename, format="PNG")

def sobre():
    message = open("sobre.txt").read()
    sg.Popup(message, title='Sobre', custom_text='Fechar', any_key_closes=True, keep_on_top=True)

def media(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.MedianFilter())
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def mediana(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.BoxBlur(1))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def moda(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.ModeFilter())
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def gauss(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.GaussianBlur)
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def ampliacao(window, imageData):
    imageEdited = Image.fromarray(imageData)
    largura, altura = imageEdited.size
    imageEdited = imageEdited.resize((int(largura*1.5),int(altura*1.5)))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def espelhamento(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.transpose(Image.FLIP_LEFT_RIGHT)
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def reducao(window, imageData):
    imageEdited = Image.fromarray(imageData)
    largura, altura = imageEdited.size
    imageEdited = imageEdited.resize((int(largura*0.5),int(altura*0.5)))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def rotacao(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.rotate(180)
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def translacao(window, imageData):
    image = Image.fromarray(imageData)
    largura, altura = image.size
    imageEdited = Image.new('RGB', image.size)
    imageEdited.paste(image, (int(largura*0.1),int(altura*0.1)))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def brilho(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = ImageEnhance.Brightness(imageEdited).enhance(1.5)
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def contraste(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = ImageEnhance.Contrast(imageEdited).enhance(1.5)
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData
    
def grayScale(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.convert('L')
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def erosao(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.MinFilter(3))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData


def dilatacao(window, imageData):
    imageEdited = Image.fromarray(imageData)
    imageEdited = imageEdited.filter(ImageFilter.MaxFilter(3))
    imageData = asarray(imageEdited)
    updateEditedImage(window, imageData)
    return imageData

def main_window():
    imageData = []

    menu = [
        ["  Arquivo  ", ["Abrir", "Salvar", "Sair", "Sobre"]],
        ["  Extração De Características  ", ["Desafio"]], # TODO: Desafio
        ["  Filtros  ", ["Brilho", "Contraste", "Grayscale", "Passa Alta","Passa Baixa", ["Média", "Mediana", "Moda", "Gauss"], "Threshould"]], # TODO: Passa Alta(com submenu), Threshould
        ["  Morfologia Matemática  ", ["Abertura", "Dilatação", "Erosão", "Fechamento"]], # TODO: Abertura, Fechamento
        ["  Transformações Geométricas  ", ["Ampliação (50%)", "Espelhamento", "Redução (50%)", "Rotação (180°)", "Translação (10%)"]]
    ]

    layout = [
        [sg.MenubarCustom(menu, tearoff = False, key="-MENU-")],
        [sg.Frame('Imagem Original', [[sg.Image(key="-IMG-")]], element_justification='c'), 
            sg.Frame('Imagem Editada', [[sg.Image(key="-EDITED_IMG-")]], element_justification='c')],
    ]

    window = sg.Window(settings["GUI"]["title"], layout, use_custom_titlebar=True, element_justification='c', size=(1366,720))

    while True:
        event, values = window.read()
        if event in ('Sair', sg.WINDOW_CLOSED):
            break
        if event == 'Abrir':
            imageData = abrir(window)
        if event == 'Salvar':
            save(imageData)
        if event == 'Sobre':
            sobre()
        if event == 'Média':
            imageData = media(window, imageData)
        if event == 'Mediana':
            imageData = mediana(window, imageData)
        if event == 'Moda':
            imageData = moda(window, imageData)
        if event == 'Gauss':
            imageData = gauss(window, imageData)
        if event == 'Ampliação (50%)':
            imageData = ampliacao(window, imageData)
        if event == 'Espelhamento':
            imageData = espelhamento(window, imageData)
        if event == 'Redução (50%)':
            imageData = reducao(window, imageData)
        if event == 'Rotação (180°)':
            imageData = rotacao(window, imageData)
        if event == 'Translação (10%)':
            imageData = translacao(window, imageData)
        if event == "Brilho":
            imageData = brilho(window, imageData)
        if event == "Contraste":
            imageData = contraste(window, imageData)
        if event == "Grayscale":
            imageData = grayScale(window, imageData)
        if event == "Erosão":
            imageData = erosao(window, imageData)
        if event == "Dilatação":
            imageData = dilatacao(window, imageData)
        print(event, values)
    window.close()

# Aplica estilização #
SETTINGS_PATH = Path.cwd()
settings = sg.UserSettings(path = SETTINGS_PATH, filename = "config.ini", use_config_file = True, convert_bools_and_none = True)
sg.theme(settings["GUI"]["theme"])
sg.set_options(font = (settings["GUI"]["font_family"], int(settings["GUI"]["font_size"])))

main_window()

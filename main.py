from pathlib import Path
import PySimpleGUI as sg
import io, os
from PIL import Image, ImageFilter
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

def open(window):
    filename = sg.PopupGetFile('', no_window = True)
    if os.path.exists(filename):
        imageData = asarray(Image.open(filename))
        updateOriginalImage(window, imageData)
        updateEditedImage(window, imageData)
        return imageData
    return []

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
    ## To Do Gauss ##
    updateEditedImage(window, imageData)
    return imageData

def save(imageData):
    if not len(imageData) > 0:
        errorWindow('Não existe imagem a ser salva') 
    else:
        filename = sg.popup_get_file('',save_as=True, file_types=(("PNG Files", "*.png"),), no_window=True)
        if os.path.exists(filename):
            Image.fromarray(imageData).save(filename, format="PNG")

def main_window():
    imageData = []

    menu = [
        ["  Arquivo  ", ["Abrir", "Salvar", "Sair", "Sobre"]],
        ["  Extração De Características  ", ["Desafio"]],
        ["  Filtros  ", ["Grayscale","Passa Alta","Passa Baixa", ["Média", "Mediana", "Moda", "Gauss"], "Threshould"]],
        ["  Morfologia Matemática  ", ["Abertura", "Dilatação", "Erosão", "Fechamento"]],
        ["  Transformações Geométricas  ", ["Ampliação", "Espelhamento", "Redução", "Rotação", "Translação"]]
    ]

    layout = [
        [sg.MenubarCustom(menu, tearoff = False, key="-MENU-")],
        [sg.Frame('Imagem Original', [[sg.Image(key="-IMG-")]], element_justification='c'), 
            sg.Frame('Imagem Editada', [[sg.Image(key="-EDITED_IMG-")]], element_justification='c')],
    ]

    window = sg.Window(settings["GUI"]["title"], layout, use_custom_titlebar=True, element_justification='c', size=(1366,720), keep_on_top=True)

    while True:
        event, values = window.read()
        if event in ('Sair', sg.WINDOW_CLOSED):
            break
        if event == 'Abrir':
            imageData = open(window)
        if event == 'Salvar':
            save(imageData)
        if event == 'Média':
            imageData = media(window, imageData)
        if event == 'Mediana':
            imageData = mediana(window, imageData)
        if event == 'Moda':
            imageData = moda(window, imageData)
        if event == 'Gauss':
            imageData = gauss(window, imageData)
        print(event, values)
    window.close()

# Aplica estilização #
SETTINGS_PATH = Path.cwd()
settings = sg.UserSettings(path = SETTINGS_PATH, filename = "config.ini", use_config_file = True, convert_bools_and_none = True)
sg.theme(settings["GUI"]["theme"])
sg.set_options(font = (settings["GUI"]["font_family"], int(settings["GUI"]["font_size"])))

main_window()

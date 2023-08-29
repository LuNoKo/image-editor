from pathlib import Path
import PySimpleGUI as sg
import io, os
from PIL import Image
from numpy import asarray

def error_window(message):
    sg.Popup(message, title='Erro', auto_close=True, custom_text='Fechar', any_key_closes=True)

def main_window():
    image_data = []

    menu_def = [
      ["  Arquivo  ", ["Abrir","Salvar","Sobre","Sair"]],
      ["  Transformações Geométricas  ",["Translação","Rotação","Espelhamento","Ampliação","Redução"]],
      ["  Filtros  ",["Grayscale","Passa Baixa","Passa Alta","Threshould"]],
      ["  Morfologia Matemática  ",["Dilatação", "Erosão", "Abertura", "Fechamento"]],
      ["  Extração De Características  ",["Desafio"]]
    ]

    frame_img_original = [[sg.Image(key="-IMG-")]]

    frame_img_edited = [[sg.Image(key="-NEW_IMG-")]]

    layout = [
      [sg.MenubarCustom(menu_def, tearoff = False, key="-MENU-")],
      [sg.Frame('Imagem Original', frame_img_original,element_justification='c'), 
        sg.Frame('Imagem Original', frame_img_edited, element_justification='c')],
    ]

    window_title = settings["GUI"]["title"]
    window = sg.Window(window_title, layout, use_custom_titlebar = True, element_justification='c').Finalize()
    # window.Maximize()

    while True:
        event, values = window.read()
        if event in ('Sair'):
            break
        if event == 'Abrir':
            filename = sg.PopupGetFile('', no_window = True)
            if os.path.exists(filename):
              image = Image.open(filename)
              image_data = asarray(image)
              bio = io.BytesIO()
              image.save(bio, format="PNG")
              window["-IMG-"].update(data=bio.getvalue())
              window["-NEW_IMG-"].update(data=bio.getvalue())
        if event == 'Salvar':
            if not len(image_data) > 0: 
              error_window('Não existe imagem a ser salva') 
            else:
              filename = sg.popup_get_file('',save_as=True, file_types=(("PNG Files", "*.png"),))
              Image.fromarray(image_data).save(filename, format="PNG")
        print(event, values)
    window.close()

if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
      path = SETTINGS_PATH, filename = "config.ini", 
      use_config_file = True, convert_bools_and_none = True
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])
    sg.theme(theme)
    sg.set_options(font = (font_family, font_size))
    main_window()

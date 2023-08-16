from pathlib import Path
import PySimpleGUI as sg


def main_window():
    menu_def = [
      ["  Arquivo  ", [sg.FileBrowse(),"Salvar","Sobre","Sair"]],
      ["  Transformações Geométricas  ",["Transladar","Rotacionar","Espelhar","Aumentar","Diminuir"]],
      ["  Filtros  ",["Grayscale","Passa Baixa","Passa Alta","Threshould"]],
      ["  Morfologia Matemática  ",["Dilatação", "Erosão", "Abertura", "Fechamento"]],
      ["  Extração De Características  ",["Desafio"]]
    ]

    frame_img_original = [[sg.Image(filename="teste.png")]]

    frame_img_edited = [[sg.Image(filename="teste.png")]]

    layout = [
      [sg.MenubarCustom(menu_def, tearoff = False, key="-MENU-")],
      [sg.Frame('Imagem Original', frame_img_original,element_justification='c'), 
        sg.Frame('Imagem Original', frame_img_edited, element_justification='c')],
    ]

    window_title = settings["GUI"]["title"]
    window = sg.Window(window_title, layout, use_custom_titlebar = True, element_justification='c').Finalize()
    #window.Maximize()

    window.read()
    while True:
        event, values = window.read()
        if event in ( sg.WINDOW_CLOSED, "Exit"):
            break
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

import openpyxl
import time

# import get book
from app.utils import get_book
#import route driver
from app.const import const_project
# import webdriver
from selenium import webdriver
def read_book_path():
    print("Se inicia la descarga de archivos")
    try:
        list_doucments: list = get_book.list_dir_path()
        path_book: str = (list_doucments[0])
        wb = openpyxl.load_workbook(path_book)
        list_sheets: list = wb.sheetnames
        sheet_active = wb[list_sheets[0]]

        COLUM_ID_DOC: str = "AT"
        COLUM_ESTATE: str = "BG"
        consecutive: int = 310
        print(sheet_active.cell(row=1, column=2).value)
        # start instance of navigator
        navigator = webdriver.Chrome(executable_path=const_project.PATH_DRIVER)
        # redirecte to PATH_LOGIN_DIAN
        navigator.get(const_project.PATH_LOGIN_DIAN)
        # wait 20 secons for configurate path download
        time.sleep(5)

        print("### Configure la ruta de descarga en la nueva ventana ###")
        accept_download = input("Digite la letra 'S' para confirmar: ")
        for row in sheet_active.iter_rows():
            cell_activate_id_doc: str = COLUM_ID_DOC + str(consecutive) # Cell for id documento electronic
            cell_id_doc_value = sheet_active[cell_activate_id_doc].value
            link_download = const_project.PATH_DOWNLOAD_ZIP

            navigator.execute_script('''window.open(" ''' + link_download + cell_id_doc_value + ''' ","_blank");''')
            time.sleep(5)

            cell_download: str = COLUM_ESTATE + str(consecutive) # Cell for confirmed download
            sheet_active[cell_download].value = "DESCARGADO"
            consecutive += 1

            wb.save(path_book) # Save the changes
    except Exception as e:
        print("posible en : read book")
        print(e)

    print("Ha finalizado la descarga de archivos")


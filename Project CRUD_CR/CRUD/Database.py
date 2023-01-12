from . import Operasi

DB_NAME = "Project CRUD_CR/data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":50*" ",
    "penulis":50*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME,"r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
    

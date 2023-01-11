from . import Operasi

DB_NAME = "Project CRUD_R/data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "date_add":"yyyy-mm-dd",
    "judul":50*" ",
    "penulis":50*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open("Project CRUD_R/data.txt","r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        Operasi.create_first_data()
    

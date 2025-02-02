import os

def open_scr_qlo():
    """Short cut for opening Fliqlo"""
    try:
        os.startfile("C:/Users/mandl/OneDrive/Desktop/autoOpenFliqlo/Fliqlo.scr", "open")
    except Exception as error:
        print(f"An error occured : {error}")

if __name__ == "__main__":
    open_scr_qlo()
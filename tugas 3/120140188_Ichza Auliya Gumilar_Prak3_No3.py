from iniClass import *

# Cara akses atribut protected yang baik dan benar 
class AnakNomor3(Nomor3):
    def __init__(self):
        super().__init__()
    
    def get_attr_private(self):
        return super().get_attr_private()

    # Panggil dengan menggunakan anak class
    def get_attr_protected(self):
        return self._ini_protected
    
    def get_attr_public(self):
        return super().get_attr_public()

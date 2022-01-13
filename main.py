from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QRadioButton, QButtonGroup, QLabel
from modules.bin_to_dec import bin_to_dec
from modules.dec_to_hex_bin_oct import dec_to_hex_bin_oct
from modules.hex_to_bin import hex_to_bin
from modules.oct_to_bin import oct_to_bin

class AppWindow(QWidget): # dziedziczymy z QWidget
    def __init__(self): # konstruktor klasy
        super().__init__() # inicjalizuje wszystko z QWidget

        self.setup()

    def setup(self):

        self.value_input = QLineEdit('', self) # pole do wpisywania tekstu
        self.value_input.setFixedWidth(300) # szerokość pola
        self.value_input.move(30, 50) # współrzędne

        radio_list_1 = QRadioButton('binarny', self) # pole do wyboru systemu liczbowego
        radio_list_1.move(35, 85)
        radio_list_2 = QRadioButton('ósemkowy', self)
        radio_list_2.move(35, 105)
        radio_list_3 = QRadioButton('dziesiętny', self)
        radio_list_3.move(35, 125)
        radio_list_4 = QRadioButton('szesnastkowy', self)
        radio_list_4.move(35, 145)

        self.radio_group_1 = QButtonGroup(self) # grupa radio
        self.radio_group_1.addButton(radio_list_1)
        self.radio_group_1.addButton(radio_list_2)
        self.radio_group_1.addButton(radio_list_3)
        self.radio_group_1.addButton(radio_list_4)

        radio_list_5 = QRadioButton('binarny', self) # pole do wyboru systemu liczbowego
        radio_list_5.move(215, 85)
        radio_list_6 = QRadioButton('ósemkowy', self)
        radio_list_6.move(215, 105)
        radio_list_7 = QRadioButton('dziesiętny', self)
        radio_list_7.move(215, 125)
        radio_list_8 = QRadioButton('szesnastkowy', self)
        radio_list_8.move(215, 145)

        self.radio_group_2 = QButtonGroup(self) # grupa radio
        self.radio_group_2.addButton(radio_list_5)
        self.radio_group_2.addButton(radio_list_6)
        self.radio_group_2.addButton(radio_list_7)
        self.radio_group_2.addButton(radio_list_8)

        info_label = QLabel(self)
        info_label.setText('==>')
        info_label.move(165, 115)

        self.result_label = QLabel(self)
        self.result_label.resize(300, 20)
        self.result_label.setText('')
        self.result_label.move(40, 200)
 
        submit_btn = QPushButton('Przelicz', self) # przycisk, self jest potrzebny bo trzeba dodać do czego ma być przypięty element
        submit_btn.move((360 - submit_btn.size().width()) // 2, 250) # współrzędne
        submit_btn.clicked.connect(self.submit) # wywołanie po kliknięciu przycisku
        
        self.setFixedSize(360, 300) # rozmiar okna
        self.setWindowTitle('Calculator of number systems') # nazwa okna

        self.show() # uruchamia okno

    def submit(self):
        numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
        value = self.value_input.text() # pobiera tekst
        value_number_system_1 = self.radio_group_1.checkedId() # pobiera numer zaznaczonego pola
        value_number_system_2 = self.radio_group_2.checkedId()

        if value_number_system_1  == -1 or value_number_system_2 == -1: # sprawdza czy wybrano systemy liczbowe
            self.result_label.setText('Nie wybrano systemów liczbowych!')
            return
        
        if value == '': # sprawdza czy wartość nie jest pusta
            self.result_label.setText('Nie podano danych!')
            return
        
        for i in value: # sprawdza czy wartość jest poprawna
            if i not in numbers:
                self.result_label.setText('Podano złe dane!')
                return

        for i in value: # usuwa zera z początku liczby
            if i == '0':
                value = value[1:]
            else:
                break

        if value_number_system_1 == value_number_system_2: # jeśli wybrano takie same systemy liczbowe
            self.result_label.setText('Wybrano te same systemy liczbowe!')
            return
        
        elif value_number_system_1 == -2: # z binarnego
            for i in value: # sprawdza czy wartość jest poprawna
                if i not in numbers[0:2]:
                    self.result_label.setText('Podano złe dane!')
                    return
            if value_number_system_2 == -3: # na ósemkowy
                result = bin_to_dec(value)
                result = dec_to_hex_bin_oct(result, 8)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -4: # na dziesiętny
                result = bin_to_dec(value)
                result = str(result)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -5: # na szesnastkowy
                result = bin_to_dec(value)
                result = dec_to_hex_bin_oct(result, 16)
                self.result_label.setText(result)
                return

        elif value_number_system_1 == -3: # z ósemkowego
            for i in value: # sprawdza czy wartość jest poprawna
                if i not in numbers[0:8]:
                    self.result_label.setText('Podano złe dane!')
                    return
            if value_number_system_2 == -2: # na binarny
                result = oct_to_bin(value)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -4: # na dziesiętny
                result = oct_to_bin(value)
                result = bin_to_dec(result)
                result = str(result)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -5: # na szesnastkowy
                result = oct_to_bin(value)
                result = bin_to_dec(result)
                result = dec_to_hex_bin_oct(result, 16)
                self.result_label.setText(result)
                return

        elif value_number_system_1 == -4: # z dziesiętnego
            for i in value: # sprawdza czy wartość jest poprawna
                if i not in numbers[0:10]:
                    self.result_label.setText('Podano złe dane!')
                    return
            if value_number_system_2 == -2: # na binarny
                result = dec_to_hex_bin_oct(value, 2)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -3: # na ósemkowy
                result = dec_to_hex_bin_oct(value, 8)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -5: # na szesnastkowy
                result = dec_to_hex_bin_oct(value, 16)
                self.result_label.setText(result)
                return

        elif value_number_system_1 == -5: # z szesnastkowego
            if value_number_system_2 == -2: # na binarny
                result = hex_to_bin(value)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -3: # na ósemkowy
                result = hex_to_bin(value)
                result = bin_to_dec(result)
                result = dec_to_hex_bin_oct(result, 8)
                self.result_label.setText(result)
                return
            elif value_number_system_2 == -4: # na dziesiętny
                result = hex_to_bin(value)
                result = bin_to_dec(result)
                result = str(result)
                self.result_label.setText(result)
                return
            


if __name__ == '__main__':
    app = QApplication([]) # aplikacja
    
    app_window = AppWindow() 

    app.exec() # uruchamia program
from mainGUI import Ui_MainWindow


class JSONLogFileAnalysis():
    def get_parameter_list(self):
        self.RightPayloadlabel.hide()
        self.RightPayloadpushButton.hide()
        self.RightPayloadtextEdit.hide()

    def compare_payload(self):
        self.RightPayloadlabel.show()
        self.RightPayloadpushButton.show()
        self.RightPayloadtextEdit.show()
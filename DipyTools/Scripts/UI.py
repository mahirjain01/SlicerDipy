import sys
import warnings
from Scripts.TreeStructure import list_dipy_contents
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QComboBox, QLabel

warnings.filterwarnings('ignore') 

dipy_structure = list_dipy_contents()

class DipyDialog(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("DIPY Module Selector")
        self.layout = QVBoxLayout()
        
        self.label_module = QLabel("Select DIPY Subpackage:")
        self.combo_module = QComboBox()
        self.combo_module.addItems(dipy_structure.keys())
        
        self.label_submodule = QLabel("Select Submodule:")
        self.combo_submodule = QComboBox()
        self.combo_submodule.setEnabled(False)
        
        self.label_class = QLabel("Select Function:")
        self.combo_class = QComboBox()
        self.combo_class.setEnabled(False)
        
        self.layout.addWidget(self.label_module)
        self.layout.addWidget(self.combo_module)
        self.layout.addWidget(self.label_submodule)
        self.layout.addWidget(self.combo_submodule)
        self.layout.addWidget(self.label_class)
        self.layout.addWidget(self.combo_class)
        
        self.setLayout(self.layout)
        
        self.combo_module.currentIndexChanged.connect(self.populate_submodules)
        self.combo_submodule.currentIndexChanged.connect(self.populate_classes)
    
    def populate_submodules(self):
        """Populate submodules based on the selected subpackage."""
        selected_module = self.combo_module.currentText()
        submodules = dipy_structure[selected_module]
        
        self.combo_submodule.clear()
        self.combo_class.clear()
        self.combo_class.setEnabled(False)
        
        if submodules:
            self.combo_submodule.addItems(submodules.keys())
            self.combo_submodule.setEnabled(True)
        else:
            self.combo_submodule.setEnabled(False)
    
    def populate_classes(self):
        """Populate functions based on the selected submodule."""
        selected_module = self.combo_module.currentText()
        selected_submodule = self.combo_submodule.currentText()
        
        functions = dipy_structure[selected_module].get(selected_submodule, [])
        
        self.combo_class.clear()
        if functions:
            self.combo_class.addItems(functions)
            self.combo_class.setEnabled(True)
        else:
            self.combo_class.setEnabled(False)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     dialog = DipyDialog()
#     dialog.show()
#     sys.exit(app.exec_())

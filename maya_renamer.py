from maya import cmds


class mainUi(object):
    windoww = "batchRenamer_Window"
    title = "Outliner Renamer"
        
    def __init__(self):
        self.window = "batchRenamer_Window"
        self.title = "Outliner Renamer"
        self.size = (450, 700)
    
    @classmethod
    def display(self):
        self.delete()
        
        main_window = cmds.window(self.windoww, title=self.title, sizeable=True, menuBar=True)
        main_layout = cmds.columnLayout(adjustableColumn=True, parent=main_window)
        
        # replace UI
        replace_layout = cmds.frameLayout(label="Search and Replace", parent=main_layout, bgs=True)
        replace_form = cmds.formLayout(parent=replace_layout, h=65)
        self.searchInput = cmds.textFieldGrp(label="Search for:", columnWidth=(1,75), columnWidth2=(2,426)
                                                )
        self.replaceInput = cmds.textFieldGrp(label="Replace to:", columnWidth=(1,75), columnWidth2=(2,426)
                                                )
        
        cmds.formLayout(replace_form, enable=True, attachForm=(self.searchInput, "top", 6))
        cmds.formLayout(replace_form, enable=True, attachForm=(self.searchInput, "left", 0))
        cmds.formLayout(replace_form, enable=True, attachForm=(self.replaceInput, "top", 3, self.searchInput))
        
        cmds.showWindow(main_window)
        
        
    @classmethod   
    def delete(self):
        if cmds.window(self.windoww, exists=True):
            cmds.deleteUI(self.windoww, window=True)
            

    def helpui(self):
    
        if cmds.window("batchRenamer_Window", exists=True):
            cmds.deleteUI("batchRenamer_Window", window=True)
    
    
        main_window = cmds.window("batchRenamer_Window", title="Renamer", sizeable=True, menuBar=True, widthHeight=[300,700])
        main_layout = cmds.columnLayout(adjustableColumn=True, parent=main_window)
        replace_layout = cmds.frameLayout(label="Search and Replace", labelIndent=250, font='boldLabelFont', labelWidth=100, parent=main_layout, bgc=(0.15,0.15,0.15))
        replace_form = cmds.rowColumnLayout(nc=2, cw=[(1,75),(2,500)], co=[(1, 'left', 3), (2, 'both', 3)], parent=replace_layout, h=200)
        cmds.text(1='Search for:', al='left')
        self.searchInput = cmds.textField(cc = self.searchUpdate)
        cmds.textFieldGrp(label="Replace to: ", columnWidth=(1,75), columnWidth2=(2,500), editable=True, parent=replace_form)

        rename_layout = cmds.frameLayout(label="Rename Objects", labelIndent=200, font='boldLabelFont', labelWidth=100, parent=main_layout, bgc=(0.15,0.15,0.15))
        rename_form = cmds.formLayout(parent=rename_layout, h=100)
        name_input = cmds.textFieldGrp(label="Name: ", columnWidth=(1, 75), columnWidth2=(2, 426), editable=True, parent=rename_form)
        prefix_input = cmds.textFieldGrp(label="Prefix: ", columnWidth=(1, 75), columnWidth2=(2, 426), editable=True, parent=rename_form)
        suffix_input = cmds.textFieldGrp(label="Suffix: ", columnWidth=(1, 75), columnWidth2=(2, 426), editable=True, parent=rename_form)
        cmds.intField(minValue=0, maxValue=3, value=0)
        rename_button = cmds.button(label="Rename", width=500)
        cmds.formLayout(rename_form, e=True, af=(name_input, "top", 1))
        cmds.formLayout(rename_form, e=True, ac=(prefix_input, "top", 2, name_input))
        cmds.formLayout(rename_form, e=True, ac=(suffix_input, "top", 3, prefix_input))
        #cmds.formLayout(rename_form, e=True, ac=(padding_input, "top", 3, suffix_input))
        cmds.formLayout(rename_form, e=True, ac=(rename_button, "top", 3, suffix_input))
        
        cmds.showWindow(main_window)
        
    def searchUpdate(self, *args):
        self.search = cmds.textField(self.searchInput, query=True, text=True)
        return self.search


mainUi.helpui()

        defaultIncBool = 1
        cmds.rowColumnLayout(nc=3, cw = [(1, 80), (2, 100), (3, 100)])
        incCheck = cmds.checkBox(l='Increment', v = defaultIncBool)
        cmds.setParent('..')
        
        cmds.rowColumnLayout(nc=5, cw = [(1, 20), (2, 80), (3, 40), (4,100), (5,40)])
        empty = cmds.text(l="")
        startCheck = cmds.checkBox(label='Start', v = True, en = defaultIncBool)
        startInput = cmds.intField(v=1, min=1, po=True, en = defaultIncBool)
        empty = cmds.text(l="")
        empty = cmds.text(l="")
        empty = cmds.text(l="")
        stepCheck = cmds.checkBox(label='Step', v = True, en = defaultIncBool)
        stepInput = cmds.intField(v=1, min=1, po=True, en = defaultIncBool)
        empty = cmds.text(l="")
        empty = cmds.text(l="")
        empty = cmds.text(l="")
        paddingCheck = cmds.checkBox(label='Padding', v = True, en = defaultIncBool)
        paddingInput = cmds.intField(v=1, min=1, po=True, en = defaultIncBool)
        empty = cmds.text(l="")
        empty = cmds.text(l="")
        
        cmds.separator(style='none', h=5)
        cmds.setParent('..')
        
        cmds.columnLayout(adj = True)
        applyRename = cmds.button(l = "Rename")
        
        cmds.separator(height=20)
        cmds.setParent('..')


     main_window = cmds.window("batchRenamer_Window", title="Outliner Renamer", sizeable=True, menuBar=True, widthHeight=[300,700])
        main_layout = cmds.columnLayout(adjustableColumn=True, parent=main_window)
    
        # Search and Rplace UI
        replace_layout = cmds.frameLayout(label="Search and Replace", labelIndent=200, font='boldLabelFont', labelWidth=100, parent=main_layout, bgc=(0.15,0.15,0.15))
        replace_form = cmds.formLayout(parent=replace_layout, h=85)
        search_input = cmds.textFieldGrp(label="Search For: ", columnWidth=(1, 75), columnWidth2=(2, 426), editable=True, parent=replace_form)
        replace_input = cmds.textFieldGrp(label="Replace to: ", columnWidth=(1, 75), columnWidth2=(2, 426), editable=True, parent=replace_form)
        replace_button = cmds.button(label="Replace", width=500)
        
        cmds.formLayout(replace_form, e=True, af=(search_input, "top", 1))
        #cmds.formLayout(replace_form, e=True, af=(search_input, "left", 0))
        cmds.formLayout(replace_form, e=True, ac=(replace_input, "top", 2, search_input))
        cmds.formLayout(replace_form, e=True, ac=(replace_button, "top", 3, replace_input))
        separatoer = cmds.separator(style="none", h=5)
        cmds.formLayout(replace_form, e=True, ac=(separatoer, "top", 3, replace_button))
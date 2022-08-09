# ─── IMPORTS ────────────────────────────────────────────────────────────────────
from importlib.resources import path
from remi.gui import *
from remi import start, App

from Config import *
import userdb

import PyATEMMax
# ─── APIS CONFIG AND SETUP ──────────────────────────────────────────────────────
#PyATEMMax config and setup
atem = PyATEMMax.ATEMMax()

#atem.connect(SWITCHERIP)
#atem.waitForConnection()

# ─── WEB ────────────────────────────────────────────────────────────────────────
class HUB(App):
    def __init__(self, *args, **kwargs):
        super(HUB, self).__init__(*args)
        self.sourceTallyStatus = False
        self.sourceTallySource = None
        

    def idle(self):
        #Switcher state updater
        def tally_detection(self, src):    
            tally = str(atem.tally.bySource.flags[src])
            change = f'''
if tally == "[PGM]":
    self.src{src}.css_background_color = "rgb(220,69,69)"
    self.tally{src}.css_background_color = "rgb(220,69,69)"
    if self.sourceTallyStatus == True and self.sourceTallySource == {src}:
        self.sourceTally.css_background_color = "rgb(220,69,69)"
        self.sourceTally.text = "ON AIR"
elif tally == "[PVW]":
    self.src{src}.css_background_color = "rgb(165,240,120)"
    self.tally{src}.css_background_color = "rgb(165,240,120)"
    if self.sourceTallyStatus == True and self.sourceTallySource == {src}:
        self.sourceTally.css_background_color = "rgb(165,240,120)"
        self.sourceTally.text = "PREVIEW"
elif tally == "[]":
    self.src{src}.css_background_color = "rgb(170,170,170)"
    self.tally{src}.css_background_color = "rgb(170,170,170)"
    if self.sourceTallyStatus == True and self.sourceTallySource == {src}:
        self.sourceTally.css_background_color = "rgb(170,170,170)"
        self.sourceTally.text = "NONE"
elif tally == "[PGM][PVW]":
    self.src{src}.css_background_color = "rgb(220,69,69)"
    self.tally{src}.css_background_color = "rgb(220,69,69)"
    if self.sourceTallyStatus == True and self.sourceTallySource == {src}:
        self.sourceTally.css_background_color = "rgb(220,69,69)"
        self.sourceTally.text = "ON AIR"
'''
            exec(change)
            

        #Source background update
        tally_detection(self, 1)
        tally_detection(self, 2)
        tally_detection(self, 3)
        tally_detection(self, 4)
        
        #Key background update
        key = atem.keyer[0][0].onAir.enabled
        if key == True:
            self.key.css_background_color = "rgb(220,69,69)"
        elif key == False:
            self.key.css_background_color = "rgb(170,170,170)"
        pass
    
    
    def main(self):
        #Run web data
        return HUB.construct_ui(self)
    

    # ─── WEB DATA ───────────────────────────────────────────────────────────────────
    @staticmethod
    def construct_ui(self):
        # ─── MAIN ────────────────────────────────────────────────────────
        self.main = Container()
        self.main.attr_class = "Container"
        self.main.attr_editor_newclass = False
        self.main.css_background_color = "rgb(54,57,59)"
        self.main.css_height = "100%"
        self.main.css_left = "0%"
        self.main.css_position = "absolute"
        self.main.css_top = "0%"
        self.main.css_width = "100%"
        self.main.variable_name = "main"

        # ─── MULTIMAIN ──────────────────────────────────────────────────────────────────
        self.multiMain = TabBox()
        self.multiMain.attr_class = "TabBox"
        self.multiMain.attr_editor_newclass = False
        self.multiMain.css_background_color = "rgb(54,57,59)"
        self.multiMain.css_height = "90%"
        self.multiMain.css_left = "0%"
        self.multiMain.css_position = "absolute"
        self.multiMain.css_top = "7%"
        self.multiMain.css_width = "100%"
        self.multiMain.css_border_radius = "22px"
        self.multiMain.variable_name = "multiMain"

        # ─── LOGIN ───────────────────────────────────────────────────────
        #Login container
        self.login = Container()
        self.login.attr_class = "Container"
        self.login.attr_editor_newclass = False
        self.login.css_background_color = "rgb(54,57,59)"
        self.login.css_height = "100%"
        self.login.css_left = "0%"
        self.login.css_position = "absolute"
        self.login.css_top = "0%"
        self.login.css_width = "100%"
        self.login.variable_name = "main"

        #Login Box
        self.box = Container()
        self.box.attr_class = "Container"
        self.box.attr_editor_newclass = False
        self.box.css_background_color = "rgb(165,216,255)"
        self.box.css_border_color = "rgb(255,255,255)"
        self.box.css_border_radius = "26px"
        self.box.css_border_style = "solid"
        self.box.css_height = "60%"
        self.box.css_left = "12.5%"
        self.box.css_position = "absolute"
        self.box.css_top = "15%"
        self.box.css_width = "75%"
        self.box.variable_name = "box"

        #Login Brand
        self.brand = Label()
        self.brand.attr_class = "Label"
        self.brand.attr_editor_newclass = False
        self.brand.css_color = "rgb(255,255,255)"
        self.brand.css_font_size = "300%"
        self.brand.css_height = "10%"
        self.brand.css_left = "0%"
        self.brand.css_position = "absolute"
        self.brand.css_text_align = "center"
        self.brand.css_top = "20%"
        self.brand.css_width = "100%"
        self.brand.text = BRAND
        self.brand.variable_name = "brand"

        #Login Code Input
        self.inputform = TextInput()
        self.inputform.attr_class = "TextInput"
        self.inputform.attr_editor_newclass = False
        self.inputform.attr_maxlength = "15"
        self.inputform.css_background_color = "rgb(54,57,59)"
        self.inputform.css_border_color = "rgb(255,255,255)"
        self.inputform.css_border_radius = "22px"
        self.inputform.css_border_style = "dashed"
        self.inputform.css_border_width = "3px"
        self.inputform.css_color = "rgb(255,255,255)"
        self.inputform.css_font_size = "350%"
        self.inputform.css_height = "10%"
        self.inputform.css_left = "25%"
        self.inputform.css_position = "absolute"
        self.inputform.css_text_align = "center"
        self.inputform.css_top = "50%"
        self.inputform.css_width = "50%"
        self.inputform.text = ""
        self.inputform.variable_name = "input"

        #Your Code Text
        self.ycode = Label()
        self.ycode.attr_class = "Label"
        self.ycode.attr_editor_newclass = False
        self.ycode.css_color = "rgb(255,252,255)"
        self.ycode.css_font_size = "200%"
        self.ycode.css_height = "5%"
        self.ycode.css_left = "30%"
        self.ycode.css_position = "absolute"
        self.ycode.css_text_align = "center"
        self.ycode.css_top = "40%"
        self.ycode.css_width = "40%"
        self.ycode.text = "Your code:"
        self.ycode.variable_name = "ycode"

        #Login sumbimition button
        self.submit = Button()
        self.submit.attr_class = "Button"
        self.submit.attr_editor_newclass = False
        self.submit.css_background_color = "rgb(145,200,245)"
        self.submit.css_border_width = "2px"
        self.submit.css_font_size = "200%"
        self.submit.css_height = "8%"
        self.submit.css_left = "37.5%"
        self.submit.css_position = "absolute"
        self.submit.css_top = "64%"
        self.submit.css_width = "25%"
        self.submit.css_border_radius = "22px"
        self.submit.text = "Tune in"
        self.submit.variable_name = "submit"

        #Append items to login
        self.login.append(self.box,'box')
        self.login.append(self.brand,'brand')
        self.login.append(self.inputform,'inputform')
        self.login.append(self.ycode,'ycode')
        self.login.append(self.submit,'submit')
        
        #Append login to main
        self.main.append(self.login,'login')

        # ─── STATUS BAR ─────────────────────────────────────────────────────────────────
        #Status Bar logOut
        self.logout = Button()
        self.logout.attr_class = "Button"
        self.logout.attr_editor_newclass = False
        self.logout.css_background_color = "rgb(255,87,95)"
        self.logout.css_border_radius = "22px"
        self.logout.css_height = "7%"
        self.logout.css_position = "absolute"
        self.logout.css_right = "1%"
        self.logout.css_top = "0%"
        self.logout.css_width = "15%"
        self.logout.css_font_size = "125%"
        self.logout.text = "Log out"
        self.logout.variable_name = "logOut"

        #Status Bar previousCode
        self.previousCode = Button()
        self.previousCode.attr_class = "Button"
        self.previousCode.attr_editor_newclass = False
        self.previousCode.css_background_color = "rgb(255,87,95)"
        self.previousCode.css_border_radius = "22px"
        self.previousCode.css_font_size = "200%"
        self.previousCode.css_height = "9%"
        self.previousCode.css_left = "20%"
        self.previousCode.css_position = "absolute"
        self.previousCode.css_top = "64%"
        self.previousCode.css_width = "25%"
        self.previousCode.text = "Previous Code"
        self.previousCode.variable_name = "PreviousCode"

        #Status Bar sourceTally
        self.sourceTally = Button()
        self.sourceTally.attr_class = "Button"
        self.sourceTally.attr_editor_newclass = False
        self.sourceTally.css_background_color = "rgb(220,54,65)"
        self.sourceTally.css_border_radius = "22px"
        self.sourceTally.css_font_size = "200%"
        self.sourceTally.css_height = "6%"
        self.sourceTally.css_left = "40%"
        self.sourceTally.css_position = "absolute"
        self.sourceTally.css_top = "0"
        self.sourceTally.css_width = "20%"
        self.sourceTally.text = "STATUS"
        self.sourceTally.variable_name = "sourceTally"

        # ─── SWITCHER ────────────────────────────────────────────────────
        #Switcher container
        self.switcher = Container()
        self.switcher.attr_class = "Container"
        self.switcher.attr_editor_newclass = False
        self.switcher.css_background_color = "rgb(54,57,59)"
        self.switcher.css_border_radius = "22px"
        self.switcher.css_height = "88%"
        self.switcher.css_left = "0%"
        self.switcher.css_position = "absolute"
        self.switcher.css_top = "12%"
        self.switcher.css_width = "100%"
        self.switcher.variable_name = "switcher"

        #Switcher source 1
        self.src1 = Button()
        self.src1.attr_class = "Button"
        self.src1.attr_editor_newclass = False
        self.src1.css_background_color = "rgb(170,170,170)"
        self.src1.css_border_radius = "22px"
        self.src1.css_font_size = "250%"
        self.src1.css_height = "14.5%"
        self.src1.css_left = "1%"
        self.src1.css_position = "absolute"
        self.src1.css_top = "83.5%"
        self.src1.css_width = "12%"
        self.src1.text = "1"
        self.src1.variable_name = "src1"

        #Switcher source 2
        self.src2 = Button()
        self.src2.attr_class = "Button"
        self.src2.attr_editor_newclass = False
        self.src2.css_background_color = "rgself.main.append(self.login, 'login')b(170,170,170)"
        self.src2.css_border_radius = "22px"
        self.src2.css_font_size = "250%"
        self.src2.css_height = "14.5%"
        self.src2.css_left = "15%"
        self.src2.css_position = "absolute"
        self.src2.css_top = "83.5%"
        self.src2.css_width = "12%"
        self.src2.text = "2"
        self.src2.variable_name = "src2"

        #Switcher source 3
        self.src3 = Button()
        self.src3.attr_class = "Button"
        self.src3.attr_editor_newclass = False
        self.src3.css_background_color = "rgb(170,170,170)"
        self.src3.css_border_radius = "22px"
        self.src3.css_font_size = "250%"
        self.src3.css_height = "14.5%"
        self.src3.css_left = "29%"
        self.src3.css_position = "absolute"
        self.src3.css_top = "83.5%"
        self.src3.css_width = "12%"
        self.src3.text = "3"
        self.src3.variable_name = "src3"

        #Switcher source 4
        self.src4 = Button()
        self.src4.attr_class = "Button"
        self.src4.attr_editor_newclass = False
        self.src4.css_background_color = "rgb(170,170,170)"
        self.src4.css_border_radius = "22px"
        self.src4.css_font_size = "250%"
        self.src4.css_height = "14.5%"
        self.src4.css_left = "43%"
        self.src4.css_position = "absolute"
        self.src4.css_top = "83.5%"
        self.src4.css_width = "12%"
        self.src4.text = "4"
        self.src4.variable_name = "src4"

        #Switcher cut
        self.cut = Button()
        self.cut.attr_class = "Button"
        self.cut.attr_editor_newclass = False
        self.cut.css_background_color = "rgb(170,170,170)"
        self.cut.css_border_radius = "22px"
        self.cut.css_font_size = "250%"
        self.cut.css_height = "14.5%"
        self.cut.css_left = "68%"
        self.cut.css_position = "absolute"
        self.cut.css_top = "83.5%"
        self.cut.css_width = "12%"
        self.cut.text = "CUT"
        self.cut.variable_name = "cut"

        #Switcher auto
        self.auto = Button()
        self.auto.attr_class = "Button"
        self.auto.attr_editor_newclass = False
        self.auto.css_background_color = "rgb(170,170,170)"
        self.auto.css_border_radius = "22px"
        self.auto.css_font_size = "250%"
        self.auto.css_height = "14.5%"
        self.auto.css_left = "82%"
        self.auto.css_position = "absolute"
        self.auto.css_top = "83.5%"
        self.auto.css_width = "12%"
        self.auto.text = "AUTO"
        self.auto.variable_name = "auto"

        #Append items to switcher
        self.switcher.append(self.src1,'src1')
        self.switcher.append(self.src2,'src2')
        self.switcher.append(self.src3,'src3')
        self.switcher.append(self.src4,'src4')
        self.switcher.append(self.cut,'cut')
        self.switcher.append(self.auto,'auto')

        # ─── TALLY ──────────────────────────────────────────────────────────────────────
        #Tally container
        self.tally = Container()
        self.tally.attr_class = "Container"
        self.tally.attr_editor_newclass = False
        self.tally.css_background_color = "rgb(54,57,59)"
        self.tally.css_border_radius = "22px"
        self.tally.css_height = "88%"
        self.tally.css_left = "0%"
        self.tally.css_position = "absolute"
        self.tally.css_top = "12%"
        self.tally.css_width = "100%"
        self.tally.variable_name = "tally"

        #Tally tally 1
        self.tally1 = Button()
        self.tally1.attr_class = "Button"
        self.tally1.attr_editor_newclass = False
        self.tally1.css_background_color = "rgb(170,170,170)"
        self.tally1.css_border_radius = "22px"
        self.tally1.css_font_size = "300%"
        self.tally1.css_height = "37.335%"
        self.tally1.css_left = "2%"
        self.tally1.css_position = "absolute"
        self.tally1.css_top = "7.33%"
        self.tally1.css_width = "45%"
        self.tally1.text = "1"
        self.tally1.variable_name = "tally1"

        #Tally tally 2
        self.tally2 = Button()
        self.tally2.attr_class = "Button"
        self.tally2.attr_editor_newclass = False
        self.tally2.css_background_color = "rgb(170,170,170)"
        self.tally2.css_border_radius = "22px"
        self.tally2.css_font_size = "300%"
        self.tally2.css_height = "37.335%"
        self.tally2.css_position = "absolute"
        self.tally2.css_right = "2%"
        self.tally2.css_top = "7.33%"
        self.tally2.css_width = "45%"
        self.tally2.text = "2"
        self.tally2.variable_name = "tally2"

        #Tally tally 3
        self.tally3 = Button()
        self.tally3.attr_class = "Button"
        self.tally3.attr_editor_newclass = False
        self.tally3.css_background_color = "rgb(170,170,170)"
        self.tally3.css_border_radius = "22px"
        self.tally3.css_bottom = "7.33%"
        self.tally3.css_font_size = "300%"
        self.tally3.css_height = "37.335%"
        self.tally3.css_left = "2%"
        self.tally3.css_position = "absolute"
        self.tally3.css_width = "45%"
        self.tally3.text = "3"
        self.tally3.variable_name = "tally3"

        #Tally tally 4
        self.tally4 = Button()
        self.tally4.attr_class = "Button"
        self.tally4.attr_editor_newclass = False
        self.tally4.css_background_color = "rgb(170,170,170)"
        self.tally4.css_border_radius = "22px"
        self.tally4.css_bottom = "7.33%"
        self.tally4.css_font_size = "300%"
        self.tally4.css_height = "37.335%"
        self.tally4.css_position = "absolute"
        self.tally4.css_right = "2%"
        self.tally4.css_width = "45%"
        self.tally4.text = "4"
        self.tally4.variable_name = "tally4"

        #Append items to tally
        self.tally.append(self.tally1,'tally1')
        self.tally.append(self.tally2,'tally2')
        self.tally.append(self.tally3,'tally3')
        self.tally.append(self.tally4,'tally4')

        # ─── KEYER ──────────────────────────────────────────────────────────────────────
        #Keyer container
        self.keyer = Container()
        self.keyer.attr_class = "Container"
        self.keyer.attr_editor_newclass = False
        self.keyer.css_background_color = "rgb(54,57,59)"
        self.keyer.css_border_radius = "22px"
        self.keyer.css_height = "88%"
        self.keyer.css_left = "0%"
        self.keyer.css_position = "absolute"
        self.keyer.css_top = "12%"
        self.keyer.css_width = "100%"
        self.keyer.variable_name = "keyer"

        #Keyer key
        self.key = Button()
        self.key.attr_class = "Button"
        self.key.attr_editor_newclass = False
        self.key.css_background_color = "rgb(170,170,170)"
        self.key.css_border_radius = "22px"
        self.key.css_font_size = "650%"
        self.key.css_height = "90%"
        self.key.css_left = "2.5%"
        self.key.css_position = "absolute"
        self.key.css_top = "5%"
        self.key.css_width = "95%"
        self.key.text = "KEY"
        self.key.variable_name = "key"

        #Append items to keyer
        self.keyer.append(self.key,'key')

        # ─── White Balance ──────────────────────────────────────────────────────────────
        #White Balance Container
        self.whitebalance = Container()
        self.whitebalance.attr_class = "Container"
        self.whitebalance.attr_editor_newclass = False
        self.whitebalance.css_height = "100%"
        self.whitebalance.css_position = "absolute"
        self.whitebalance.css_width = "100%"
        self.whitebalance.variable_name = "main"

        #White Balance Status
        self.WBstatus = TextInput()
        self.WBstatus.attr_class = "TextInput"
        self.WBstatus.attr_editor_newclass = False
        self.WBstatus.attr_maxlength = "4"
        self.WBstatus.css_border_radius = "22px"
        self.WBstatus.css_font_size = "350%"
        self.WBstatus.css_height = "15%"
        self.WBstatus.css_left = "5%"
        self.WBstatus.css_position = "absolute"
        self.WBstatus.css_text_align = "center"
        self.WBstatus.css_top = "40%"
        self.WBstatus.css_width = "90%"
        self.WBstatus.text = "3800"
        self.WBstatus.variable_name = "WBstatus"

        #White Balance Minus
        self.minus = Button()
        self.minus.attr_class = "Button"
        self.minus.attr_editor_newclass = False
        self.minus.css_background_color = "rgb(220,69,69)"
        self.minus.css_border_radius = "22px"
        self.minus.css_font_size = "300%"
        self.minus.css_height = "15%"
        self.minus.css_left = "20%"
        self.minus.css_position = "absolute"
        self.minus.css_top = "65%"
        self.minus.css_width = "25%"
        self.minus.text = "-"
        self.minus.variable_name = "button0"

        #White Balance Plus
        self.plus = Button()
        self.plus.attr_class = "Button"
        self.plus.attr_editor_newclass = False
        self.plus.css_background_color = "rgb(165,240,120)"
        self.plus.css_border_radius = "22px"
        self.plus.css_font_size = "300%"
        self.plus.css_height = "15%"
        self.plus.css_position = "absolute"
        self.plus.css_right = "20%"
        self.plus.css_top = "65%"
        self.plus.css_width = "25%"
        self.plus.text = "+"
        self.plus.variable_name = "button1"
        
        #White Balance Submition
        self.SubBtn = Button()
        self.SubBtn.attr_class = "Button"
        self.SubBtn.attr_editor_newclass = False
        self.SubBtn.css_background_color = "rgb(165,240,120)"
        self.SubBtn.css_border_radius = "22px"
        self.SubBtn.css_font_size = "300%"
        self.SubBtn.css_height = "15%"
        self.SubBtn.css_position = "absolute"
        self.SubBtn.css_right = "37.5%"
        self.SubBtn.css_top = "82.5%"
        self.SubBtn.css_width = "25%"
        self.SubBtn.text = "Submit"
        self.SubBtn.variable_name = "SubBtn"
        

        #Apend items to white balance
        self.whitebalance.append(self.WBstatus,'WBstatus')

        self.whitebalance.append(self.plus,'plus')
        self.whitebalance.append(self.minus,'minus')

        self.whitebalance.append(self.SubBtn,'SubBtn')


        # ─── BUTTON DETECTION ────────────────────────────────────────────
        #Login
        self.submit.onclick.do(self.on_submit_pressed)

        #Status Bar
        self.logout.onclick.do(self.on_logOut_pressed)
        self.previousCode.onclick.do(self.on_previousCode_pressed)

        #Switcher
        self.cut.onclick.do(self.on_cut_pressed)
        self.auto.onclick.do(self.on_auto_pressed)

        self.src1.onclick.do(self.on_src1_pressed)
        self.src2.onclick.do(self.on_src2_pressed)
        self.src3.onclick.do(self.on_src3_pressed)
        self.src4.onclick.do(self.on_src4_pressed)

        #Keyer
        self.key.onclick.do(self.on_key_pressed)

        #White Balance
        self.SubBtn.onclick.do(self.on_wbsubmit_pressed)

        self.minus.onclick.do(self.on_minus_pressed)
        self.plus.onclick.do(self.on_plus_pressed)

        return self.main

    #Login
    def on_submit_pressed(self, widget):
        #Check all the users codes
        for i in range(1, userdb.userCount + 1):
            
            #Take user input
            inputcode = self.inputform.get_text()

            #Get user and their states
            states = locals()
            exec(f'''
if inputcode == userdb.user{i}.code:
    correctCode = True
    if userdb.user{i}.tally == True:
        self.main.append(self.sourceTally, 'sourceTally')
        self.sourceTallyStatus = True
        self.sourceTallySource = userdb.user{i}.source
    else:
        self.sourceTallyStatus = False
        self.sourceTallySource = None
    if userdb.user{i}.multipleWorkspaces == True:
        multipleWorkspaces = True
        workspaceNum = userdb.user{i}.workspaceNum
        userNum = {i}
    else:
        multipleWorkspaces = False
else:
    correctCode = False
''', globals(), states)
            if states["correctCode"] == True:
                if states["multipleWorkspaces"] == True: 
                    self.main.empty()
                    for i in range (0, states["workspaceNum"]):
                        if self.sourceTallyStatus == True:
                            self.main.append(self.sourceTally, 'sourceTally')
                        workspace = locals()
                        userNumber = states["userNum"]
                        exec(f"workspace = userdb.user{userNumber}.workspace.split(',')[{i}]", globals(), workspace)
                        selfWork = 'self.' + workspace["workspace"]
                        selfWorkAns = str(workspace["workspace"])
                        workspace = workspace["workspace"]
                        code = f'''
name = selfWorkAns
self.main.append(self.multiMain, 'multiMain')
self.{selfWorkAns}.css_top = "7.5%"
self.{selfWorkAns}.css_height = "93%"
self.multiMain.append({selfWork}, str(name))
self.main.append(self.logout, 'logOut')
'''                     
                        exec(code)
                else:
                    workspace = locals()
                    exec(f"workspace = userdb.user{i}.workspace", globals(), workspace)
                    selfWork = 'self.' + workspace["workspace"]
                    code = f'''
self.main.empty()
workspace = str(workspace["workspace"])
self.main.append({selfWork}, workspace)
self.main.append(self.logout, 'logOut')
if self.sourceTallyStatus == True:
    self.sourceTally.css_height = "15%"
    self.main.append(self.sourceTally, 'sourceTally')
'''
                    exec(code)

    #Status Bar
    def on_logOut_pressed(self, widget):
        self.main.empty()
        self.main.append(self.login, 'login')
        self.submit.css_left = "55%"
        self.main.append(self.previousCode,'PreviousCode')
        self.codetxt = self.inputform.get_text()
        self.inputform.text = ""

    def on_previousCode_pressed(self, widget):
        self.inputform.text = self.codetxt
        self.on_submit_pressed(widget)

    #Switcher
    def on_cut_pressed(self, widget):
        atem.execCutME(0)

    def on_auto_pressed(self, widget):
        atem.execAutoME(0)

    def on_src1_pressed(self, widget):
        atem.setPreviewInputVideoSource(0,1)

    def on_src2_pressed(self, widget):
        atem.setPreviewInputVideoSource(0,2)

    def on_src3_pressed(self, widget):
        atem.setPreviewInputVideoSource(0,3)

    def on_src4_pressed(self, widget):
        atem.setPreviewInputVideoSource(0,4)

    #Keyer
    def on_key_pressed(self, widget):
        status = atem.keyer[0][KEYERKEY].onAir.enabled
        if status == True:
            atem.setKeyerOnAirEnabled(0, KEYERKEY, False)
        elif status == False:
            atem.setKeyerOnAirEnabled(0, KEYERKEY, True)
    
    #White Balance
    def on_wbsubmit_pressed(self, widget):
        atem.setCameraControlWhiteBalance(1, int(self.WBstatus.text))
    def on_minus_pressed(self, widget):
        self.WBstatus.text = str(int(self.WBstatus.text) - 50)
    def on_plus_pressed(self, widget):
        self.WBstatus.text = str(int(self.WBstatus.text) + 50)
# ─── WEB STARTUP ────────────────────────────────────────────────────────────────
start(HUB, address='0.0.0.0', port=8080, multiple_instance=True, enable_file_cache=True, update_interval=0.08, start_browser=False)

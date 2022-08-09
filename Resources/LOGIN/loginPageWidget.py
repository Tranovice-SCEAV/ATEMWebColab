
# -*- coding: utf-8 -*-

from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        loginContainer = Container()
        loginContainer.attr_class = "Container"
        loginContainer.attr_editor_newclass = False
        loginContainer.css_background_color = "rgb(54,57,59)"
        loginContainer.css_height = "100%"
        loginContainer.css_left = "0%"
        loginContainer.css_position = "absolute"
        loginContainer.css_top = "0%"
        loginContainer.css_width = "100%"
        loginContainer.variable_name = "loginContainer"
        box = Container()
        box.attr_class = "Container"
        box.attr_editor_newclass = False
        box.css_background_color = "rgb(165,216,255)"
        box.css_border_color = "rgb(255,255,255)"
        box.css_border_radius = "26px"
        box.css_border_style = "solid"
        box.css_height = "60%"
        box.css_left = "12.5%"
        box.css_position = "absolute"
        box.css_top = "15%"
        box.css_width = "75%"
        box.variable_name = "box"
        loginContainer.append(box,'box')
        brand = Label()
        brand.attr_class = "Label"
        brand.attr_editor_newclass = False
        brand.css_color = "rgb(255,255,255)"
        brand.css_font_size = "300%"
        brand.css_height = "10%"
        brand.css_left = "0%"
        brand.css_position = "absolute"
        brand.css_text_align = "center"
        brand.css_top = "20%"
        brand.css_width = "100%"
        brand.text = "BRAND"
        brand.variable_name = "brand"
        loginContainer.append(brand,'brand')
        atemModel = Label()
        atemModel.attr_class = "Label"
        atemModel.attr_editor_newclass = False
        atemModel.css_color = "rgb(255,255,255)"
        atemModel.css_font_size = "200%"
        atemModel.css_height = "6%"
        atemModel.css_position = "absolute"
        atemModel.css_text_align = "center"
        atemModel.css_top = "30%"
        atemModel.css_width = "100%"
        atemModel.text = "ATEM MODEL"
        atemModel.variable_name = "atemModel"
        loginContainer.append(atemModel,'label0')
        input = TextInput()
        input.attr_class = "TextInput"
        input.attr_editor_newclass = False
        input.attr_maxlength = "15"
        input.css_background_color = "rgb(54,57,59)"
        input.css_border_color = "rgb(255,255,255)"
        input.css_border_radius = "22px"
        input.css_border_style = "dashed"
        input.css_border_width = "3px"
        input.css_color = "rgb(255,255,255)"
        input.css_font_size = "350%"
        input.css_height = "10%"
        input.css_left = "25%"
        input.css_position = "absolute"
        input.css_text_align = "center"
        input.css_top = "50%"
        input.css_width = "50%"
        input.text = ""
        input.variable_name = "input"
        loginContainer.append(input,'input')
        ycode = Label()
        ycode.attr_class = "Label"
        ycode.attr_editor_newclass = False
        ycode.css_color = "rgb(255,252,255)"
        ycode.css_font_size = "200%"
        ycode.css_height = "5%"
        ycode.css_left = "30%"
        ycode.css_position = "absolute"
        ycode.css_text_align = "center"
        ycode.css_top = "40%"
        ycode.css_width = "40%"
        ycode.text = "Your code:"
        ycode.variable_name = "ycode"
        loginContainer.append(ycode,'ycode')
        submit = Button()
        submit.attr_class = "Button"
        submit.attr_editor_newclass = False
        submit.css_background_color = "rgb(145,200,245)"
        submit.css_border_radius = "22px"
        submit.css_border_width = "2px"
        submit.css_font_size = "200%"
        submit.css_height = "8%"
        submit.css_left = "37.5%"
        submit.css_position = "absolute"
        submit.css_top = "64%"
        submit.css_width = "25%"
        submit.text = "Tune in"
        submit.variable_name = "submit"
        loginContainer.append(submit,'submit')
        
        

        self.loginContainer = loginContainer
        return self.loginContainer
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

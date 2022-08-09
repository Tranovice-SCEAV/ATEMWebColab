
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
        switcher = Container()
        switcher.attr_class = "Container"
        switcher.attr_editor_newclass = False
        switcher.css_background_color = "rgb(54,57,59)"
        switcher.css_border_radius = "22px"
        switcher.css_height = "88%"
        switcher.css_left = "0%"
        switcher.css_position = "absolute"
        switcher.css_top = "12%"
        switcher.css_width = "100%"
        switcher.variable_name = "switcher"
        src1 = Button()
        src1.attr_class = "Button"
        src1.attr_editor_newclass = False
        src1.css_background_color = "rgb(170,170,170)"
        src1.css_border_radius = "22px"
        src1.css_font_size = "250%"
        src1.css_height = "14.5%"
        src1.css_left = "1%"
        src1.css_position = "absolute"
        src1.css_top = "83.5%"
        src1.css_width = "12%"
        src1.text = "1"
        src1.variable_name = "src1"
        switcher.append(src1,'src1')
        src2 = Button()
        src2.attr_class = "Button"
        src2.attr_editor_newclass = False
        src2.css_background_color = "rgb(170,170,170)"
        src2.css_border_radius = "22px"
        src2.css_font_size = "250%"
        src2.css_height = "14.5%"
        src2.css_left = "15%"
        src2.css_position = "absolute"
        src2.css_top = "83.5%"
        src2.css_width = "12%"
        src2.text = "2"
        src2.variable_name = "src2"
        switcher.append(src2,'src2')
        src3 = Button()
        src3.attr_class = "Button"
        src3.attr_editor_newclass = False
        src3.css_background_color = "rgb(170,170,170)"
        src3.css_border_radius = "22px"
        src3.css_font_size = "250%"
        src3.css_height = "14.5%"
        src3.css_left = "29%"
        src3.css_position = "absolute"
        src3.css_top = "83.5%"
        src3.css_width = "12%"
        src3.text = "3"
        src3.variable_name = "src3"
        switcher.append(src3,'src3')
        src4 = Button()
        src4.attr_class = "Button"
        src4.attr_editor_newclass = False
        src4.css_background_color = "rgb(170,170,170)"
        src4.css_border_radius = "22px"
        src4.css_font_size = "250%"
        src4.css_height = "14.5%"
        src4.css_left = "43%"
        src4.css_position = "absolute"
        src4.css_top = "83.5%"
        src4.css_width = "12%"
        src4.text = "4"
        src4.variable_name = "src4"
        switcher.append(src4,'src4')
        cut = Button()
        cut.attr_class = "Button"
        cut.attr_editor_newclass = False
        cut.css_background_color = "rgb(170,170,170)"
        cut.css_border_radius = "22px"
        cut.css_font_size = "250%"
        cut.css_height = "14.5%"
        cut.css_left = "68%"
        cut.css_position = "absolute"
        cut.css_top = "83.5%"
        cut.css_width = "12%"
        cut.text = "CUT"
        cut.variable_name = "cut"
        switcher.append(cut,'cut')
        auto = Button()
        auto.attr_class = "Button"
        auto.attr_editor_newclass = False
        auto.css_background_color = "rgb(170,170,170)"
        auto.css_border_radius = "22px"
        auto.css_font_size = "250%"
        auto.css_height = "14.5%"
        auto.css_left = "82%"
        auto.css_position = "absolute"
        auto.css_top = "83.5%"
        auto.css_width = "12%"
        auto.text = "AUTO"
        auto.variable_name = "auto"
        switcher.append(auto,'auto')
        

        self.switcher = switcher
        return self.switcher
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

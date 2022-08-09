
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
        tally = Container()
        tally.attr_class = "Container"
        tally.attr_editor_newclass = False
        tally.css_background_color = "rgb(54,57,59)"
        tally.css_border_radius = "22px"
        tally.css_height = "88%"
        tally.css_left = "0%"
        tally.css_position = "absolute"
        tally.css_top = "12%"
        tally.css_width = "100%"
        tally.variable_name = "tally"
        tally1 = Button()
        tally1.attr_class = "Button"
        tally1.attr_editor_newclass = False
        tally1.css_background_color = "rgb(170,170,170)"
        tally1.css_border_radius = "22px"
        tally1.css_font_size = "300%"
        tally1.css_height = "37.335%"
        tally1.css_left = "2%"
        tally1.css_position = "absolute"
        tally1.css_top = "7.33%"
        tally1.css_width = "45%"
        tally1.text = "1"
        tally1.variable_name = "tally1"
        tally.append(tally1,'tally1')
        tally2 = Button()
        tally2.attr_class = "Button"
        tally2.attr_editor_newclass = False
        tally2.css_background_color = "rgb(170,170,170)"
        tally2.css_border_radius = "22px"
        tally2.css_font_size = "300%"
        tally2.css_height = "37.335%"
        tally2.css_position = "absolute"
        tally2.css_right = "2%"
        tally2.css_top = "7.33%"
        tally2.css_width = "45%"
        tally2.text = "2"
        tally2.variable_name = "tally2"
        tally.append(tally2,'tally2')
        tally3 = Button()
        tally3.attr_class = "Button"
        tally3.attr_editor_newclass = False
        tally3.css_background_color = "rgb(170,170,170)"
        tally3.css_border_radius = "22px"
        tally3.css_bottom = "7.33%"
        tally3.css_font_size = "300%"
        tally3.css_height = "37.335%"
        tally3.css_left = "2%"
        tally3.css_position = "absolute"
        tally3.css_width = "45%"
        tally3.text = "3"
        tally3.variable_name = "tally3"
        tally.append(tally3,'tally3')
        tally4 = Button()
        tally4.attr_class = "Button"
        tally4.attr_editor_newclass = False
        tally4.css_background_color = "rgb(170,170,170)"
        tally4.css_border_radius = "22px"
        tally4.css_bottom = "7.33%"
        tally4.css_font_size = "300%"
        tally4.css_height = "37.335%"
        tally4.css_position = "absolute"
        tally4.css_right = "2%"
        tally4.css_width = "45%"
        tally4.text = "4"
        tally4.variable_name = "tally4"
        tally.append(tally4,'tally4')
        

        self.tally = tally
        return self.tally
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

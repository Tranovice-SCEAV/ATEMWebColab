
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
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "100%"
        container0.css_left = "0%"
        container0.css_position = "absolute"
        container0.css_top = "0%"
        container0.css_width = "100%"
        container0.variable_name = "container0"
        sourceTally = Button()
        sourceTally.attr_class = "Button"
        sourceTally.attr_editor_newclass = False
        sourceTally.css_background_color = "rgb(220,54,65)"
        sourceTally.css_border_radius = "22px"
        sourceTally.css_font_size = "250%"
        sourceTally.css_height = "7%"
        sourceTally.css_left = "40%"
        sourceTally.css_position = "absolute"
        sourceTally.css_top = "1.8%"
        sourceTally.css_width = "20%"
        sourceTally.text = "STATUS"
        sourceTally.variable_name = "sourceTally"
        container0.append(sourceTally,'sourceTally')
        

        self.container0 = container0
        return self.container0
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

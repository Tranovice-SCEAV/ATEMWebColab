
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
        main = Container()
        main.attr_class = "Container"
        main.attr_editor_newclass = False
        main.css_height = "100%"
        main.css_left = "0%"
        main.css_position = "absolute"
        main.css_top = "0%"
        main.css_width = "100%"
        main.variable_name = "main"
        multiMain = TabBox()
        multiMain.attr_class = "TabBox"
        multiMain.attr_editor_newclass = False
        multiMain.css_background_color = "rgb(54,57,59)"
        multiMain.css_height = "93%"
        multiMain.css_left = "0%"
        multiMain.css_position = "absolute"
        multiMain.css_top = "7%"
        multiMain.css_width = "100%"
        multiMain.variable_name = "multiMain"
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_display = "block"
        container0.css_height = "250px"
        container0.css_left = "20px"
        container0.css_position = "absolute"
        container0.css_top = "20px"
        container0.css_width = "250px"
        container0.variable_name = "container0"
        multiMain.append(container0,'container0')
        container1 = Container()
        container1.attr_class = "Container"
        container1.attr_editor_newclass = False
        container1.css_display = "none"
        container1.css_height = "250px"
        container1.css_left = "20px"
        container1.css_position = "absolute"
        container1.css_top = "20px"
        container1.css_width = "250px"
        container1.variable_name = "container1"
        multiMain.append(container1,'container1')
        main.append(multiMain,'multiMain')
        

        self.main = main
        return self.main
    


#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])

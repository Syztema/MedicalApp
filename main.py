import kivy
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
from kivy.properties import ObjectProperty
#from screen_nav import screen_helper
Window.size = (360,540)

kivy.require('1.0.8')

class MedicalApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        LabelBase.register(name="MPoppins", fn_regular="D:\\Universidad\\Proyectos\\Fonts\\Poppins-Medium.ttf")
        LabelBase.register(name="BPoppins", fn_regular="D:\\Universidad\\Proyectos\\Fonts\\Poppins-SemiBold.ttf")
        #self.manager = ScreenManager(transition = NoTransition())
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        return screen_manager

    def show_dialog(self, title, message, destination_screen):
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title=title, text=message, buttons=[close_button])
        self.dialog.destination_screen = destination_screen  # Guarda la pantalla de destino
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        if self.dialog.destination_screen:
            destination_screen = self.dialog.destination_screen
            self.root.get_screen(destination_screen).manager.transition.direction = 'left'
            self.root.get_screen(destination_screen).manager.current = destination_screen


if __name__ == '__main__':
    MedicalApp().run()
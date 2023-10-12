import kivy
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window

Window.size = (360,540)

kivy.require('1.0.8')

class MedicalApp(MDApp):
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(Builder.load_file("home.kv"))
        screen_manager.add_widget(Builder.load_file("guides.kv"))
        screen_manager.add_widget(Builder.load_file("therapy.kv"))
        screen_manager.add_widget(Builder.load_file("results.kv"))
        return screen_manager

    def show_dialog(self, title, message, destination_screen, transition_direction):
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.dialog = MDDialog(title=title, text=message, buttons=[close_button])
        self.dialog.destination_screen = destination_screen  # Guarda la pantalla de destino
        self.dialog.transition_direction = transition_direction
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        if self.dialog.destination_screen:
            destination_screen = self.dialog.destination_screen
            transition_direction = self.dialog.transition_direction
            self.root.get_screen(destination_screen).manager.transition.direction = transition_direction
            self.root.get_screen(destination_screen).manager.current = destination_screen


if __name__ == '__main__':
    MedicalApp().run()
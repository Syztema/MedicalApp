from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.core.window import Window
#from screen_nav import screen_helper
Window.size = (360,540)


class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class HomeScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignupScreen(name='signup'))
sm.add_widget(SignupScreen(name='home'))

class DemoApp(MDApp):

    def build(self):
        #Builder.load_file("screen.kv")
        screen = Builder.load_file("screen.kv")
        #screen = Builder.load_string(screen_helper)
        LabelBase.register(name="MPoppins", fn_regular="D:\\Universidad\\Proyectos\\Fonts\\Poppins-Medium.ttf")
        LabelBase.register(name="BPoppins", fn_regular="D:\\Universidad\\Proyectos\\Fonts\\Poppins-SemiBold.ttf")
        return MainScreen()

    def show_dialog(self, title, message, destination_screen):
        close_button = MDFlatButton(text='Close', on_release = self.close_dialog)
        self.dialog = MDDialog (title = title, text= message, buttons=[close_button])
        self.dialog.destination_screen = destination_screen #Guarda la pantalla de destino
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()
        if self.dialog.destination_screen:
            destination_screen = self.dialog.destination_screen
            self.root.get_screen(destination_screen).manager.transition.direction = 'left'
            self.root.get_screen(destination_screen).manager.current = destination_screen

    # def signup_data(self, obj):
    #     check_string = 'Usuario Registrado Exitosamente!'
    #     close_button = MDFlatButton(text='Close', on_release=self.close_dialog_signup)
    #     self.dialog = MDDialog(title='Registro de Usuario', text=check_string,
    #                            buttons=[close_button])
    #     self.dialog.open()
    #
    # def login_data(self, obj):
    #     check_string = 'Ingreso Exitoso!'
    #     close_button = MDFlatButton(text='Close', on_release=self.close_dialog_login)
    #     self.dialog = MDDialog(title='Ingreso de Usuario', text=check_string,
    #                            buttons=[close_button])
    #     self.dialog.open()
    #
    # def close_dialog_signup(self, *args):
    #     self.dialog.dismiss()  # Cierra el diálogo
    #     self.root.get_screen('login').manager.transition.direction = 'left'  # Establece la dirección de la transición
    #     self.root.get_screen('login').manager.current = 'login'
    #
    # def close_dialog_login(self, *args):
    #     self.dialog.dismiss()  # Cierra el diálogo
    #     self.root.get_screen('home').manager.transition.direction = 'left'  # Establece la dirección de la transición
    #     self.root.get_screen('home').manager.current = 'home'

#DemoApp().run()

if __name__ == "__main__":
    DemoApp().run()
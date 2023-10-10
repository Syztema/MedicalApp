screen_helper = """
ScreenManager:
    MainScreen:
    LoginScreen:
    SignupScreen:
    HomeScreen:

<MainScreen>:
    name: 'main'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        Image:
            source: 'assets/logo.png'                 
            pos_hint: {'center_x': .18, 'center_y': .95}
        Image:
            source: 'assets/back1.png'      
            size_hint: .8, .8
            pos_hint: {'center_x': .5, 'center_y': .65}
        MDLabel:
            text: 'H e l l o !'
            font_name: 'BPoppins'
            font_size: '23sp'
            pos_hint: {'center_y': .38}
            halign: 'center'
            color: rgba (34, 34, 34, 255)
        MDLabel:
            text: 'The best app for your health'
            font_name: 'MPoppins'
            font_size: '13sp'
            size_hint_x: .85
            pos_hint: {'center_x': .5, 'center_y': .3}            
            halign: 'center'
            color: rgba (127, 127, 127, 255)
        Button:
            text: 'LOGIN'
            size_hint: .66, .065
            pos_hint: {'center_x': .5, 'center_y': .18}
            background_color: 0, 0, 0, 0
            font_name: 'BPoppins'
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'login'
            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
        Button:
            text: 'SIGN UP'
            size_hint: .66, .065
            pos_hint: {'center_x': .5, 'center_y': .09}
            background_color: 0, 0, 0, 0
            font_name: 'BPoppins'
            color: rgba(52, 0, 231, 255)
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'signup'
            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                Line:
                    width: 1.2
                    rounded_rectangle: self.x, self.y, self.width, self.height, 5, 5, 5, 5, 100

<LoginScreen>:
    name: 'login'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_y': .95}
            user_font_size: '30sp'
            theme_text_color: 'Custom'
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'main'
        MDLabel:
            text: 'W e l c o m e !'
            font_name: 'BPoppins'
            font_size: '26sp'
            pos_hint: {'center_x': .6, 'center_y': .85}            
            color: rgba (0, 0, 59, 255)
        MDLabel:
            text: 'Sign in to continue'
            font_name: 'MPoppins'
            font_size: '18sp'            
            pos_hint: {'center_x': .6, 'center_y': .79}                        
            color: rgba (135, 135, 193, 255)
        MDFloatLayout:
            size_hint: .7, .07            
            pos_hint: {'center_x': .5, 'center_y': .63}
            TextInput: 
                hint_text: 'Email'
                font_name: 'MPoppins' 
                size_hint_y: .75                
                pos_hint: {'center_x': .43, 'center_y': .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: '14sp'
                cursor_width: '2sp'
                multiline: False
            MDFloatLayout:
                pos_hint: {'center_x': .45, 'center_y': 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)  
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {'center_x': .5, 'center_y': .5}
            TextInput: 
                hint_text: 'Password'
                font_name: 'MPoppins' 
                size_hint_y: .75
                pos_hint: {'center_x': .43, 'center_y': .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: '14sp'
                cursor_width: '2sp'
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {'center_x': .45, 'center_y': 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)       
        Button:
            text: 'LOGIN'
            size_hint: .66, .065
            pos_hint: {'center_x': .5, 'center_y': .34}
            background_color: 0, 0, 0, 0
            font_name: 'BPoppins'
            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]         
            check_string = 'Ingreso Exitoso!'            
            on_release: app.show_dialog('Ingreso de Usuario', check_string, 'home')
        MDTextButton:
            text: 'Forgot Password?'
            pos_hint: {'center_x': .5, 'center_y': .28}      
            color: rgba(68, 78, 132, 255)
            font_size: '12sp'
            font_name: 'BPoppins'
        MDLabel:
            text: 'or'
            color: rgba(52, 0, 231, 255)
            pos_hint: {'center_y': .22}
            font_size: '13sp'
            font_name: 'BPoppins'
            halign: 'center'
        MDFloatLayout:
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .3, 'center_y': .218}
        MDFloatLayout:
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .7, 'center_y': .218}
        MDLabel:
            text: 'Social Media Login'
            font_name: 'BPoppins'
            font_size: '13sp'
            halign: 'center'
            pos_hint: {'center_y': .16}
            color: rgba(135, 133, 193, 255)
        MDGridLayout:
            cols: 3
            size_hint: .48, .07
            pos_hint: {'center_x': .5, 'center_y': .1}
            Image:
                source: 'assets/google.png'
            Image:
                source: 'assets/facebook.png'
            Image:
                source: 'assets/apple.png'
        MDLabel:
            text: "Don't have an account?"
            font_name: 'BPoppins'
            font_size: '11sp'
            pos_hint: {'center_x': .68, 'center_y': .04}
            color: rgba(135, 133, 193, 255)
        MDTextButton:
            text: "Sign up"
            font_name: 'BPoppins'
            font_size: '11sp'
            pos_hint: {'center_x': .75, 'center_y': .04}
            color: rgba(52, 0, 231, 255) 
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'signup'
            
<SignupScreen>:
    name: 'signup'
    MDFloatLayout:
        md_bg_color: 1, 1, 1, 1
        MDIconButton:
            icon: 'arrow-left'
            pos_hint: {'center_y': .95}
            user_font_size: '30sp'
            theme_text_color: 'Custom'
            text_color: rgba(26, 24, 58, 255)
            on_release:
                root.manager.transition.direction = 'right'
                root.manager.current = 'main'
        MDLabel:
            text: 'H i !'
            font_name: 'BPoppins'
            font_size: '26sp'
            pos_hint: {'center_x': .6, 'center_y': .85}            
            color: rgba (0, 0, 59, 255)
        MDLabel:
            text: 'Create a new account'
            font_name: 'MPoppins'
            font_size: '18sp'            
            pos_hint: {'center_x': .6, 'center_y': .79}                        
            color: rgba (135, 135, 193, 255)
        MDFloatLayout:
            size_hint: .7, .07            
            pos_hint: {'center_x': .5, 'center_y': .68}
            TextInput: 
                hint_text: 'Username'
                font_name: 'MPoppins' 
                size_hint_y: .75                
                pos_hint: {'center_x': .43, 'center_y': .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: '14sp'
                cursor_width: '2sp'
                multiline: False
            MDFloatLayout:
                pos_hint: {'center_x': .45, 'center_y': 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
        MDFloatLayout:
            size_hint: .7, .07            
            pos_hint: {'center_x': .5, 'center_y': .56}
            TextInput: 
                hint_text: 'Email'
                font_name: 'MPoppins' 
                size_hint_y: .75                
                pos_hint: {'center_x': .43, 'center_y': .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: '14sp'
                cursor_width: '2sp'
                multiline: False
            MDFloatLayout:
                pos_hint: {'center_x': .45, 'center_y': 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)  
        MDFloatLayout:
            size_hint: .7, .07
            pos_hint: {'center_x': .5, 'center_y': .44}
            TextInput: 
                hint_text: 'Password'
                font_name: 'MPoppins' 
                size_hint_y: .75
                pos_hint: {'center_x': .43, 'center_y': .5}
                background_color: 1, 1, 1, 0
                foreground_color: rgba(0, 0, 59, 255)
                cursor_color: rgba(0, 0, 59, 255)
                font_size: '14sp'
                cursor_width: '2sp'
                multiline: False
                password: True
            MDFloatLayout:
                pos_hint: {'center_x': .45, 'center_y': 0}
                size_hint_y: .03
                md_bg_color: rgba(178, 178, 178, 255)
        Button:
            text: 'SIGN UP'
            size_hint: .66, .065
            pos_hint: {'center_x': .5, 'center_y': .3}
            background_color: 0, 0, 0, 0
            font_name: 'BPoppins'
            canvas.before:
                Color:
                    rgb: rgba(52, 0, 231, 255)
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
            check_string = 'Usuario Registrado Exitosamente!'            
            on_release: app.show_dialog('Registro de Usuario', check_string, 'login')            
        MDLabel:
            text: 'or'
            color: rgba(52, 0, 231, 255)
            pos_hint: {'center_y': .22}
            font_size: '13sp'
            font_name: 'BPoppins'
            halign: 'center'
        MDFloatLayout:
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .3, 'center_y': .218}
        MDFloatLayout:
            md_bg_color: rgba(178, 178, 178, 255)
            size_hint: .3, .002
            pos_hint: {'center_x': .7, 'center_y': .218}
        MDLabel:
            text: 'Social Media Login'
            font_name: 'BPoppins'
            font_size: '13sp'
            halign: 'center'
            pos_hint: {'center_y': .16}
            color: rgba(135, 133, 193, 255)
        MDGridLayout:
            cols: 3
            size_hint: .48, .07
            pos_hint: {'center_x': .5, 'center_y': .1}
            Image:
                source: 'assets/google.png'
            Image:
                source: 'assets/facebook.png'
            Image:
                source: 'assets/apple.png'
        MDLabel:
            text: 'Already have an account?'
            font_name: 'BPoppins'
            font_size: '11sp'
            pos_hint: {'center_x': .68, 'center_y': .04}
            color: rgba(135, 133, 193, 255)
        MDTextButton:
            text: "Sign in"
            font_name: 'BPoppins'
            font_size: '11sp'
            pos_hint: {'center_x': .79, 'center_y': .04}
            color: rgba(52, 0, 231, 255) 
            on_release:
                root.manager.transition.direction = 'left'
                root.manager.current = 'login'
<HomeScreen>:
    name: 'home'
    MDLabel:
        text: 'Hello World!'
        font_style: 'Caption'
        halign: 'center'
        theme_text_color: 'Custom'
        text_color: 236/255, 98/255, 81/255, 1
        pos_hint: {'center_y': .38}
"""
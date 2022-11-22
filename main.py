from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.behaviors.focus_behavior import FocusBehavior


KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: 'MyApp'
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
        TelaLogin:

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: 0.7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}

    MDBoxLayout: 
        size_hint_y: .2
        md_bg_color: app.theme_cls.primary_color
        padding: [25, 0, 25, 0]
        MDLabel:
            text: 'Mudar Senha'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 

        MDIconButton:
            icon:'close'
            theme_text_color: 'Custom'
            text_color: 1,1,1,1 
            on_release: root.fechar()

    MDFloatLayout:

        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Código Enviado por email'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Nova senha'
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha'


        MDRaisedButton:
            text: 'Recadastrar!'
            pos_hint: {'center_x': .5}
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9

<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'language-python'
        icon_size: '75sp'
    MDTextField:
        size_hint_x: .8
        hint_text: 'Email:'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDTextField:
        size_hint_x: .8
        hint_text: 'Senha:'
        pos_hint: {'center_x': .5, 'center_y': .6}
    ButtonFocus:
        size_hint_x: .8 
        pos_hint: {'center_x': .5, 'center_y': .5}
        text: 'Login'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    MDLabel:
        halign: 'center'
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Esquecer sua senha?'
    MDTextButton:
        id: text_buttom
        pos_hint: {'center_x': .5, 'center_y': .35}
        text: 'Clique aqui!'
        on_release: root.abrir_card()

'''

#class MyApp(MDApp):
#    def build(self):
#        fl = FloatLayout()
#        fl.add_widget(MDRaisedButton(text='Clica em mim'))
#        return fl

class ButtonFocus(MDRaisedButton, FocusBehavior):
    ...


class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())
        print('Abrindo card')

class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = '700'
        #self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(KV)



MyApp().run()
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen, ScreenManager

class JanelaGerenciadora(ScreenManager):
    pass

class JanelaPrincipal(Screen):
    pass

class Janela1(Screen):
    pass

class Janela2(Screen):
    pass


KV = '''
FloatLayout:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .9}
        icon: 'language-python'
        icon_size: '75sp'
    MDDropDownItem:
        id: drop_item
        size_hint_x: .8
        text: 'Clarinete'
        text: 'Flauta'
        pos_hint: {'center_x': .5, 'center_y': .8}
        on_release: print("Press item")
    MDTextField:
        size_hint_x: .8
        hint_text: 'Professor(a):'
        pos_hint: {'center_x': .5, 'center_y': .7}
    MDTextField:
        size_hint_x: .8
        hint_text: 'Aluno:'
        pos_hint: {'center_x': .5, 'center_y': .6}
    MDTextField:
        size_hint_x: .8
        hint_text: 'Avaliador(a):'
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDRaisedButton:
        size_hint_x: .8 
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Avaliar'
'''

#class MyApp(MDApp):
#    def build(self):
#        fl = FloatLayout()
#        fl.add_widget(MDRaisedButton(text='Clica em mim'))
#        return fl

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)


MyApp().run()
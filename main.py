import kivy
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.app import App

class maniPro(GridLayout):
    def __init__(self,**kwargs):
        super(maniPro, self).__init__(**kwargs)
        self.cols = 2
        self.rows =4

        self.add_widget(Label( font_size = 30 ,color = (255,0,130,1), text = ' ten :'))
        self.name =TextInput(font_size= 80,multiline = False, foreground_color = (255,0,130,1) )
        self.add_widget(self.name)

        self.add_widget(Label(text='last name: '))
        self.lastname = TextInput(multiline=True)
        self.add_widget(self.lastname)

        self.add_widget(Label(text='Email: '))
        self.email = TextInput(multiline=True)
        self.add_widget(self.email)

        self.add_widget(Label(text='Emuuuu: '))
        self.em= TextInput(multiline=True)
        self.add_widget(self.em)
class myapp(App):
    def build(self):
        return maniPro()

if __name__=='__main__':
    myapp().run()



from kivy.app import App

from kivy.uix.widget import Widget
from kivy_deps import sdl2, glew
class pro(Widget):
	print("ssss")
	pass
class apppro(App):
	def build(self):
		return pro()
if __name__=='__main__':
		apppro().run()
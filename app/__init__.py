from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout

class MyBoxLayout(BoxLayout):
    my_list = ListProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_list = ['item 1', 'item 2', 'item 3']

class TestApp(App):
    def build(self):
        return MyBoxLayout()

if __name__ == '__main__':
    TestApp().run()
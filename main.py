from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

class MyApp(App):
    def build(self):
        layout = AnchorLayout(anchor_x='center', anchor_y='center', padding=[50])

        btn = Button(text='0', on_press=self.increase_by_one, size_hint=(.5, .5))
        layout.add_widget(btn)

        return layout


    def increase_by_one(self, instance):
        instance.text = str(int(instance.text) + 1)


if __name__ == '__main__':
    MyApp().run()
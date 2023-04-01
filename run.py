from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MainApp(App):
    def update_label(self):  
        self.lbl.text=self.formula

    Window.clearcolor = (0.19, 0.47, 0.3, 0)

    def calc_result(self, instance):
        my_list = [ el for el in self.lbl.text]
        t = 0
        for i in my_list:
            if i != 0:
                t+=0.5
        y=str(eval(self.lbl.text))
        y=int(y)/t
        y=round(y,2)
        self.lbl.text=str(y)
        self.formula="0"

    def add_number(self, instance):
        if (self.formula=="0"):
            self.formula=""
    
        self.formula+=str(instance.text)
        self.update_label()
    
    def build(self):
        self.formula = "0"
        bl = BoxLayout(orientation='vertical', padding=20)
        gl = GridLayout(cols = 3, spacing=2, size_hint=(1,.6))

        self.lbl=Label(text='Введите свои оценки', font_size=30, size_hint=(1,.4))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='+1', on_press = self.add_number, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        gl.add_widget(Button(text='+2', on_press = self.add_number, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        gl.add_widget(Button(text='+3', on_press = self.add_number, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        gl.add_widget(Button(text='+4', on_press = self.add_number, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        gl.add_widget(Button(text='+5', on_press = self.add_number, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        gl.add_widget(Button(text='Cредний балл',on_press = self.calc_result, background_color=[0.32, 0.7, 0.47, 1], background_normal=''))
        
        bl.add_widget(gl)
        return bl
    
if __name__ == '__main__':
    MainApp().run()
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
  def __init__(self,**kwargs):
      super().__init__(**kwargs)
      btn=Button(text="Click me",size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.5})
      self.label=Label(text="Welcome",size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.7})
      self.label2 = Label(size_hint=(0.5, 0.1), pos_hint={"center_x": 0.5, "center_y": 0.4})
      self.textInput=TextInput(size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.6})
      btn.bind(on_press=self.button_press)
      self.add_widget(btn)
      self.add_widget(self.label)
      self.add_widget(self.textInput)
      self.add_widget(self.label2)
  def button_press(self,obj):
      data=self.textInput.text
      data2="Welcome " +data
      self.label2.text=data2

class FirstApp(App):
   def build(self):
       return Interface()





FirstApp().run()
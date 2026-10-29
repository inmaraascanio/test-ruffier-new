from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from timer import Timer


from logic import *

from instructions import * 

# Variables globales 
name, age = "", 7
pulse_1, pulse_2, pulse_3 = 0,0,0

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #WIDGETS
        instructions = Label(text=txt_instruction)
        txt_name = Label(text= "Ingrese su nombre:")
        txt_age = Label (text="Ingrese su edad:")
        self.input_name = TextInput(multiline=False)
        self.input_age = TextInput(multiline=False, text="")

        self.btn = Button(
            text="Iniciar Test", 
            size_hint=(0.5, None), 
            height="50dp", 
            pos_hint={"center_x": 0.5}, 
            on_press=self.next_screen
            )

        #LAYAOUT
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        # linea 1
        row_1 = BoxLayout(padding=5, spacing=10, size_hint_y=None, height="50dp")
        row_1.add_widget(txt_name)
        row_1.add_widget(self.input_name)
        # linea 2
        row_2 = BoxLayout(padding=5, spacing=10, size_hint_y=None, height="50dp")
        row_2.add_widget(txt_age)
        row_2.add_widget(self.input_age)

        main_layout.add_widget(instructions)
        main_layout.add_widget(row_1)
        main_layout.add_widget(row_2)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def next_screen(self, *args):
        global name, age
        nombre_ingresado = self.input_name.text.strip()
        if nombre_ingresado == "":
            name = "Usuario"
        else:
            name = nombre_ingresado

        edad_validada = check_int(self.input_age.text)

        if edad_validada is False:
            return
        
        age = edad_validada
        self.manager.current = "pulse1"
        

class Pulse1Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # WIDGETS
        instructions = Label(text=txt_test1)
 
        self.text_pulse1 = Label(text=txt_test1) 
        self.input_pulse1 = TextInput(multiline=False)

        self.btn = Button(
            text="Siguiente", 
            pos_hint={"center_x":0.5}, 
            size_hint= (0.3, 0.2),
            height="50dp",
            on_press=self.next_screen
            )

        # LAYOUT
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # linea 1
        row_1 = BoxLayout(padding=10, spacing=10, size_hint_y=None, height="50dp")
        
      
        row_1.add_widget(self.text_pulse1) 
        row_1.add_widget(self.input_pulse1)

        main_layout.add_widget(instructions)
        main_layout.add_widget(row_1)
        main_layout.add_widget(self.btn)

        self.add_widget(main_layout)

    def next_screen(self, *args):
        global pulse_1
        pulse_1 = int(self.input_pulse1.text)
        self.manager.current = "pulse2"


class Pulse2Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # 1. Creamos los widgets con sus configuraciones una sola vez
        instructions = Label(text=txt_test2)
        
        self.counter_label = Label(text="45", font_size=40, size_hint_y=None, height="60dp")
        
        self.btn_start = Button(
            text="Iniciar",
            pos_hint={"center_x": 0.5},
            size_hint=(0.5, None),
            height="50dp",
            on_press=self.start_timer  # Aquí llama al método que crearemos abajo
        )
        
        self.btn_next = Button(
            text="Siguiente",
            size_hint=(0.5, None),
            height="50dp",
            pos_hint={"center_x": 0.5},
            on_press=self.next_screen,
            disabled=True
        )
        
        # 2. Los organizamos en el layout
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        main_layout.add_widget(instructions)
        main_layout.add_widget(self.counter_label)
        main_layout.add_widget(self.btn_start)
        main_layout.add_widget(self.btn_next)
        
        self.add_widget(main_layout)
        
        # 3. Inicializamos tu clase Timer aquí mismo para que exista al abrir la ventana
        self.mi_temporizador_1 = Timer(
            counter_label=self.counter_label,
            btn_start=self.btn_start,
            btn_next=self.btn_next,
            segundos_iniciales=45
        )

    # 4. Creamos el método que el botón está buscando
    def start_timer(self, *args):
        self.mi_temporizador_1.start_timer()

    def next_screen(self, *args):
        self.manager.current = "pulse3"


class Pulse3Screen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # WIDGETS DE INSTRUCCIONES Y ETIQUETAS
        instructions = Label(text=txt_test3)
        
        txt_result1 = Label(text="Resultado:")
        txt_result2 = Label(text="Resultado después de descanso:")
        
        # Campos de texto para los dos pulsos de esta fase
        self.input_pulse2 = TextInput(multiline=False, text="0")
        self.input_pulse3 = TextInput(multiline=False, text="0")
        
        # Botón de finalizar
        self.btn = Button(
            text="Finalizar", 
            pos_hint={"center_x": 0.5}, 
            size_hint=(0.5, None), 
            height="50dp", 
            on_press=self.next_screen
        )
        
        # LAYOUT PRINCIPAL
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)
        
        # Fila 1 para el primer resultado
        row_1 = BoxLayout(padding=5, spacing=10, size_hint_y=None, height="50dp")
        row_1.add_widget(txt_result1)
        row_1.add_widget(self.input_pulse2)
        
        # Fila 2 para el segundo resultado (después de descanso)
        row_2 = BoxLayout(padding=5, spacing=10, size_hint_y=None, height="50dp")
        row_2.add_widget(txt_result2)
        row_2.add_widget(self.input_pulse3)
        
        # Agregamos todos los elementos al layout principal en orden
        main_layout.add_widget(instructions)
        main_layout.add_widget(row_1)
        main_layout.add_widget(row_2)
        main_layout.add_widget(self.btn)
        
        self.add_widget(main_layout)

    def next_screen(self, *args):
        global pulse_2, pulse_3
        # Guardamos ambos valores en las variables globales correspondientes
        pulse_2 = int(self.input_pulse2.text)
        pulse_3 = int(self.input_pulse3.text)
        
        self.manager.current = "result"

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.result_label = Label(text="", halign="center", valign="middle")
        
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=20)
        main_layout.add_widget(self.result_label)
        
        self.add_widget(main_layout)

    def on_enter(self):
        global name, pulse_1, pulse_2, pulse_3
        
        self.result_label.text = resultado_test_ruffier(name, pulse_1, pulse_2, pulse_3)
        
        
class RuffierApp(App):

    def build(self):
        manager = ScreenManager()
        manager.add_widget(MainScreen(name="main"))
        manager.add_widget(Pulse1Screen(name="pulse1"))
        manager.add_widget(Pulse2Screen(name="pulse2"))
        manager.add_widget(Pulse3Screen(name="pulse3"))
        manager.add_widget(ResultScreen(name="result"))

        
        return manager

if __name__ == "__main__":
    app = RuffierApp()
    app.run()

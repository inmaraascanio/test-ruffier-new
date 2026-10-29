# escribe un módulo para cronómetro

from kivy.clock import Clock
from kivy.uix.label import Label

class Timer(Label):
   
    def __init__(self, counter_label, btn_start, btn_next, segundos_iniciales=45, **kwargs):
        super().__init__(**kwargs)
        self.counter_label = counter_label
        self.btn_start = btn_start
        self.btn_next = btn_next
        self.segundos_iniciales = segundos_iniciales
        self.seconds = segundos_iniciales

    def start_timer(self, *args):
        self.btn_start.disabled = True
        self.seconds = self.segundos_iniciales
        self.counter_label.text = str(self.seconds)

        Clock.schedule_interval(self.update_timer, 1)

    def update_timer(self, dt):
        if self.seconds > 0:
            self.seconds -= 1
            self.counter_label.text = str(self.seconds)

        else:
            self.counter_label.text = "¡Tiempo terminado!"
            self.btn_next.disabled = False  
            return False  
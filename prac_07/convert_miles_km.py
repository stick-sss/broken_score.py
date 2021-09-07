from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.core.window import Window

m_to_km = 1.60934

class ConvertMilestoKilometresApp(App):

    message = StringProperty()

    def build(self):
        Window.size = (600, 300)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.get_validated_miles()
        result = value * m_to_km
        self.message = str(result)

    def get_validated_miles(self):
        try:
            value = float(self.root.ids.number_input.text)
            return value
        except ValueError:
            return 0

    def handle_increase(self, change):
        miles = self.get_validated_miles() + change
        self.root.ids.number_input.text = str(miles)
        self.handle_calculate()

ConvertMilestoKilometresApp().run()
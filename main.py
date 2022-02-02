from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class KankuVisits(MDApp):

    def build(self):
        return MDLabel(text="Hello, Kanku", halign="center")


KankuVisits().run()
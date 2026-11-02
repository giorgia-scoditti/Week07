# COME VOGLIO ORGANIZZARE IL CODICE?
# CREO 3 CARTELLE: ui, model e database.

import flet as ft
from ui.view import View
from ui.controller import Controller
from model.model import Model

def main(page : ft.Page):
    model = Model()
    view = View(page)
    controller = Controller(model, view)

    view.set_controller(controller)
    view.initialize_ui()

ft.run(main)
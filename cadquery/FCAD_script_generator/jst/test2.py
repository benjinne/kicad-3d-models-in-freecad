from PySide import QtGui
import FreeCADGui as Gui
from CQGui.display import show_object
import cadquery as cq
Gui.activateWorkbench("CadQueryWorkbench")
try:
    box = cq.Workplane().box(10, 10, 5)
    box.val().label = "My_Box"
    show_object(box)
except Exception as e: # catch *all* exceptions
    print(e)

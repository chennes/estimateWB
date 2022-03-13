import FreeCAD, FreeCADGui
from datetime import datetime

'''# for development
def listProperties():
	sel = FreeCADGui.Selection.getSelection()
	for obj in sel:
		for p in dir(obj):
			FreeCAD.Console.PrintMessage("\n"+p)
'''

# supported materials. dependence with command-icons. name:density
materials={
	'ABS': 1.05,
	'PA12': 1.01,
	'PC': 1.4,
	'PLA': 1.25,
	'TPU': 1.22
}

def report(msg):
	now=datetime.now().strftime("%H:%M:%S")
	FreeCAD.Console.PrintMessage(f"\n{now} {msg}")

def volumeOf(name):
	t = FreeCAD.ActiveDocument.getObjectsByLabel(name)[0]
	if hasattr(t, 'Shape'):
		return t.Shape.Volume / 1000
	else:
		report(f"{name} has no shape nor volume")
		return False

def selectedObject():
	sel = FreeCADGui.Selection.getSelection()
	return sel[0].Label if len(sel) else None

def estimateVolume(*void):
	object = selectedObject()
	volume = volumeOf(object)
	if object and volume:
		report(f"{object} has a volume of {volume:.2f} cm³")
	else:
		report("please select a part or a body...")

def estimateWeight(material = None):
	object = selectedObject()
	volume = volumeOf(object)
	if object and volume and material:
		mass = volume * materials[material]
		report(f"{object} needs about {mass:.2f} g of {material}")
	else:
		report("please select a part or a body...")
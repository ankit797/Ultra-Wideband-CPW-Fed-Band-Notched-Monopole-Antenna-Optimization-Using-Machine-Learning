# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:27:30  Jul 16, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-30.5mm",
		"YPosition:="		, "-24mm",
		"ZPosition:="		, "-25mm",
		"XSize:="		, "61mm",
		"YSize:="		, "68mm",
		"ZSize:="		, "51.6mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 60,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])

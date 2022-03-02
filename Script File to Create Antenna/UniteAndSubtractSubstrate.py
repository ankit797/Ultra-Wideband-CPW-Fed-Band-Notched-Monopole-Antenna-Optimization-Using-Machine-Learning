# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:38:20  Jul 16, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Cylinder4",
		"Tool Parts:="		, "Cylinder5"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Box1,Cylinder6"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Cylinder2",
		"Tool Parts:="		, "Cylinder3"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:42:04  Jul 16, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder4,Cylinder1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"copper\"",
		"SolveInside:="		, False,
		"IsMaterialEditable:="	, True
	])
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"Selections:="		, "Box1"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"FR4_epoxy\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.AssignMaterial(
	[
		"NAME:Selections",
		"Selections:="		, "Cylinder2"
	], 
	[
		"NAME:Attributes",
		"MaterialValue:="	, "\"Teflon (tm)\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])

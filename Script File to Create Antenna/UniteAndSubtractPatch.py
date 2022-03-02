# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 17:59:28  Jul 18, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Circle1"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "patch",
		"Tool Parts:="		, "Circle3"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Rectangle6,Rectangle7"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Rectangle8"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Circle6",
		"Tool Parts:="		, "Rectangle11"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Circle6"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "patch",
		"Tool Parts:="		, "Polyline1,Polyline2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Rectangle13,Rectangle12"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "patch,Rectangle9,Rectangle10"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "patch",
		"Tool Parts:="		, "Rectangle14"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "patch",
		"Tool Parts:="		, "Rectangle15"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

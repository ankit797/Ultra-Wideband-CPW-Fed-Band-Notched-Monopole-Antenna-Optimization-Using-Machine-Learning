# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:41:21  Jul 18, 2021
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
		"Blank Parts:="		, "Circle4",
		"Tool Parts:="		, "Circle5"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

oModule.AssignLumpedPort(
	[
		"NAME:1",
		"Objects:="		, ["Circle4"],
		"RenormalizeAllTerminals:=", True,
		"DoDeembed:="		, False,
		[
			"NAME:Modes",
			[
				"NAME:Mode1",
				"ModeNum:="		, 1,
				"UseIntLine:="		, True,
				[
					"NAME:IntLine",
					"Start:="		, ["-1.23077003314309e-016mm","-14mm","-0.61mm"],
					"End:="			, ["-1.83697019872103e-016mm","-14mm","0.8mm"]
				],
				"AlignmentGroup:="	, 0,
				"CharImp:="		, "Zpi",
				"RenormImp:="		, "50ohm"
			]
		],
		"ShowReporterFilter:="	, False,
		"ReporterFilter:="	, [True],
		"Impedance:="		, "50ohm"
	])
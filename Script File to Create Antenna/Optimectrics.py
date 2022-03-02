# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 13:55:27  Jul 27, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "9mm"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:d",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "0.3mm"
				]
			]
		]
	])
oEditor = oDesign.SetActiveEditor("3D Modeler")
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle14:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:XSize",
					"Value:="		, "l"
				],
				[
					"NAME:YSize",
					"Value:="		, "d"
				]
			]
		]
	])
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:h",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "-5mm"
				]
			]
		]
	])
oEditor.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:Geometry3DCmdTab",
			[
				"NAME:PropServers", 
				"Rectangle15:CreateRectangle:1"
			],
			[
				"NAME:ChangedProps",
				[
					"NAME:Position",
					"X:="			, "l-5mm",
					"Y:="			, "9.3mm",
					"Z:="			, "0.8mm"
				],
				[
					"NAME:XSize",
					"Value:="		, "-d"
				],
				[
					"NAME:YSize",
					"Value:="		, "h"
				]
			]
		]
	])
oModule = oDesign.GetModule("Optimetrics")
oModule.InsertSetup("OptiParametric", 
	[
		"NAME:ParametricSetup1",
		"IsEnabled:="		, True,
		[
			"NAME:ProdOptiSetupDataV2",
			"SaveFields:="		, False,
			"CopyMesh:="		, False,
			"SolveWithCopiedMeshOnly:=", True
		],
		[
			"NAME:StartingPoint"
		],
		"Sim. Setups:="		, ["Setup1"],
		[
			"NAME:Sweeps",
			[
				"NAME:SweepDefinition",
				"Variable:="		, "l",
				"Data:="		, "LIN 7mm 10mm 0.2mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			],
			[
				"NAME:SweepDefinition",
				"Variable:="		, "d",
				"Data:="		, "LIN 0.2mm 0.4mm 0.1mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			],
			[
				"NAME:SweepDefinition",
				"Variable:="		, "h",
				"Data:="		, "LIN -3mm -7mm -0.2mm",
				"OffsetF1:="		, False,
				"Synchronize:="		, 0
			]
		],
		[
			"NAME:Sweep Operations"
		],
		[
			"NAME:Goals"
		]
	])

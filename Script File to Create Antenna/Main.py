# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 21:56:20  Jul 16, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oEditor = oDesign.SetActiveEditor("3D Modeler")
oModule = oDesign.GetModule("BoundarySetup")

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-5mm",
		"YPosition:="		, "-9mm",
		"ZPosition:="		, "0mm",
		"XSize:="		, "10mm",
		"YSize:="		, "18mm",
		"ZSize:="		, "0.8mm"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Box1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "9mm",
		"ZCenter:="		, "0mm",
		"Radius:="		, "5mm",
		"Height:="		, "0.8mm",
		"WhichAxis:="		, "Z",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "-9mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "3.6mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Y",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "-9mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "2.01mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Y",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "-7mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "0.6mm",
		"Height:="		, "-7mm",
		"WhichAxis:="		, "Y",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "-9mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "2.01mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Y",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCylinder(
	[
		"NAME:CylinderParameters",
		"XCenter:="		, "0mm",
		"YCenter:="		, "-9mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "0.6mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Y",
		"NumSides:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Cylinder3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
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
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
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
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5.5mm",
		"YStart:="		, "-9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "4.05mm",
		"Height:="		, "7mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "gnd_1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-1.2mm",
		"YStart:="		, "-1.7mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-0.6mm",
		"Height:="		, "-2.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5.5mm",
		"YStart:="		, "-1.7mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "0.5mm",
		"Height:="		, "-7.3mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "5.5mm",
		"YStart:="		, "-9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-4.05mm",
		"Height:="		, "7mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "gnd_2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "1.2mm",
		"YStart:="		, "-1.7mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "0.6mm",
		"Height:="		, "-2.5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "5.5mm",
		"YStart:="		, "-1.7mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-0.5mm",
		"Height:="		, "-7.3mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])

oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "gnd_1",
		"Tool Parts:="		, "Rectangle1"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "gnd_1",
		"Tool Parts:="		, "Rectangle4"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "gnd_2",
		"Tool Parts:="		, "Rectangle2"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "gnd_2",
		"Tool Parts:="		, "Rectangle5"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "-14mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "2.01mm",
		"WhichAxis:="		, "Y",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle4",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "-14mm",
		"ZCenter:="		, "1.4mm",
		"Radius:="		, "0.6mm",
		"WhichAxis:="		, "Y",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle5",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
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
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-1mm",
		"YStart:="		, "-9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "2mm",
		"Height:="		, "9mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "patch",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "4mm",
		"ZCenter:="		, "0.8mm",
		"Radius:="		, "5mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "3mm",
		"ZCenter:="		, "0.8mm",
		"Radius:="		, "3.8mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle3",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "2.5mm",
		"Height:="		, "-7mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-2.5mm",
		"Height:="		, "-7mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle7",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "4mm",
		"Height:="		, "-0.41742430504416mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle8",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateCircle(
	[
		"NAME:CircleParameters",
		"IsCovered:="		, True,
		"XCenter:="		, "0mm",
		"YCenter:="		, "9mm",
		"ZCenter:="		, "0.8mm",
		"Radius:="		, "5mm",
		"WhichAxis:="		, "Z",
		"NumSegments:="		, "0"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Circle6",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, True,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "-1mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-0.75mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1mm",
				"Y:="			, "-2.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "-1mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Polyline2",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreatePolyline(
	[
		"NAME:PolylineParameters",
		"IsPolylineCovered:="	, True,
		"IsPolylineClosed:="	, True,
		[
			"NAME:PolylinePoints",
			[
				"NAME:PLPoint",
				"X:="			, "1mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "0.75mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1mm",
				"Y:="			, "-2.9mm",
				"Z:="			, "0.8mm"
			],
			[
				"NAME:PLPoint",
				"X:="			, "1mm",
				"Y:="			, "-0.9mm",
				"Z:="			, "0.8mm"
			]
		],
		[
			"NAME:PolylineSegments",
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 0,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 1,
				"NoOfPoints:="		, 2
			],
			[
				"NAME:PLSegment",
				"SegmentType:="		, "Line",
				"StartIndex:="		, 2,
				"NoOfPoints:="		, 2
			]
		],
		[
			"NAME:PolylineXSection",
			"XSectionType:="	, "None",
			"XSectionOrient:="	, "Auto",
			"XSectionWidth:="	, "0mm",
			"XSectionTopWidth:="	, "0mm",
			"XSectionHeight:="	, "0mm",
			"XSectionNumSegments:="	, "0",
			"XSectionBendType:="	, "Corner"
		]
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Polyline1",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])

oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "2.5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-0.5mm",
		"Height:="		, "-1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle13",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-2.5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "0.5mm",
		"Height:="		, "-1mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle12",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5mm",
		"YStart:="		, "2mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "1mm",
		"Height:="		, "-1.8mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle9",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "5mm",
		"YStart:="		, "2mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-1mm",
		"Height:="		, "-1.8mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle10",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "9mm",
		"Height:="		, "0.3mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle14",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "4mm",
		"YStart:="		, "9.3mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "-0.3mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle15",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-5mm",
		"YStart:="		, "9mm",
		"ZStart:="		, "0.8mm",
		"Width:="		, "10mm",
		"Height:="		, "-5mm",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Rectangle11",
		"Flags:="		, "",
		"Color:="		, "(132 132 193)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True
	])
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
		"Selections:="		, "patch,Rectangle12,Rectangle13"
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

oModule.AssignPerfectE(
	[
		"NAME:PerfE1",
		"Objects:="		, ["gnd_1"],
		"InfGroundPlane:="	, False
	])
oModule.AssignPerfectE(
	[
		"NAME:PerfE2",
		"Objects:="		, ["gnd_2"],
		"InfGroundPlane:="	, False
	])
oModule.AssignPerfectE(
	[
		"NAME:PerfE3",
		"Objects:="		, ["patch"],
		"InfGroundPlane:="	, False
	])
oModule.AssignRadiation(
	[
		"NAME:Rad1",
		"Objects:="		, ["Box2"],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:Infinite Sphere1",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "0deg",
		"ThetaStop:="		, "90deg",
		"ThetaStep:="		, "90deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "360deg",
		"PhiStep:="		, "2deg",
		"UseLocalCS:="		, False
	])
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "10GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 20,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True,
		"RayDensityPerWavelength:=", 4,
		"MaxNumberOfBounces:="	, 5,
		"InfiniteSphereSetup:="	, -1
	])
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearCount",
		"RangeStart:="		, "0.1GHz",
		"RangeEnd:="		, "30GHz",
		"RangeCount:="		, 201,
		"Type:="		, "Fast",
		"SaveFields:="		, False,
		"SaveRadFields:="	, False,
		"ExtrapToDC:="		, False
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

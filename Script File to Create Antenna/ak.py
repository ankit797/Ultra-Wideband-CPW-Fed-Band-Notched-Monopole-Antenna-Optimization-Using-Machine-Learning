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
		"Type:="		, "Discrete",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"ExtrapToDC:="		, False
	])

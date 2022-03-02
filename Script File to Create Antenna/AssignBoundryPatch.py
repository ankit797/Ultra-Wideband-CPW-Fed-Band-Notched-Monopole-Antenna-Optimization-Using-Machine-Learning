# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2017.0.0
# 22:48:22  Jul 18, 2021
# ----------------------------------------------
import ScriptEnv
ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.SetActiveProject("Project1")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oModule = oDesign.GetModule("BoundarySetup")
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

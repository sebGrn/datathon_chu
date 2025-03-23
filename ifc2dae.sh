@echo off
cd /d %~dp0

del "./bocage.dae"
del "./bocage_sud.dae"

"./tools/IfcConvert-0.4.0-rc2-win64/IfcConvert.exe" "./resources/050_BOCAGE CENTRAL_FC_PROJET_20 02 2024.ifc" "./resources/bocage.dae" --include=entities IfcSpace --exclude=entities IfcOpeningElement ifcWall ifcSlab ifcColumn ifcBeam ifcStair ifcRamp ifcRoof ifcWindow ifcDoor ifcCurtainWall ifcBuildingElementProxy
"./tools/IfcConvert-0.4.0-rc2-win64/IfcConvert.exe" "./resources/050_BOCAGE CENTRAL SUD_EDL_20 02 2024.ifc" "./resources/bocage_sud.dae" --include=entities IfcSpace --exclude=entities IfcOpeningElement ifcWall ifcSlab ifcColumn ifcBeam ifcStair ifcRamp ifcRoof ifcWindow ifcDoor ifcCurtainWall ifcBuildingElementProxy

del "./bocage.gltf"
del "./bocage_sud.gltf"

"./tools/COLLADA2GLTF-v2.1.5-windows-Release-x64/COLLADA2GLTF-bin.exe" -i ./resources/bocage.dae -o ./resources/bocage.gltf -p
"./tools/COLLADA2GLTF-v2.1.5-windows-Release-x64/COLLADA2GLTF-bin.exe" -i ./resources/bocage_sud.dae -o ./resources/bocage_sud.gltf -p

pause

import ifcopenshell

# Input and output file paths
input_file_path = './050_BOCAGE CENTRAL_FC_PROJET_20 02 2024.ifc'
output_file_path = './bocage_cleanup.ifc'


# Load the IFC file
input_file = ifcopenshell.open(input_file_path)

# Get all IfcSpace entities
spaces = input_file.by_type('IfcSpace')

# Create a new IFC file
output_file = ifcopenshell.file()

# Add a new IfcSpace entity to the new file for each IfcSpace entity in the input file
for space in spaces:
    new_space = output_file.createIfcSpace(space.GlobalId, space.OwnerHistory, space.Name, space.Description, space.ObjectType, space.ObjectPlacement, space.Representation, space.LongName)
    output_file.add(new_space)

# Save the new file
output_file.write(output_file_path)
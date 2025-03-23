

filename = 'project.svg'
lines = open(filename).readlines()
storeys = [i for i,line in enumerate(lines) if 'IfcBuildingStorey' in line]
storeys.append(len(lines)-1)
init_parts = lines[:storeys[0]]
final_part = lines[-1] 
storey_parts = [lines[storeys[i]:storeys[i+1]] for i in range(len(storeys)-1)]

for i,storey in enumerate(storey_parts):
        svg_text = init_parts+storey+[final_part]
        svg_text = ('').join(svg_text)
        new_filename = filename.replace('.svg', f'_storey{i}.svg')
        with open(new_filename, "w") as file:
            file.write(svg_text)

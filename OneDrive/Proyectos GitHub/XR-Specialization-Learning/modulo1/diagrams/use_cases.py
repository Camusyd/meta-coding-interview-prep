# modulo1/diagrams/use_cases.py
from graphviz import Digraph

# Configuración básica
dot = Digraph('UseCases_XR_Education', filename='modulo1/diagrams/use_cases', format='svg')
dot.attr(rankdir='LR')  # izquierda -> derecha
dot.attr('node', shape='ellipse', fontsize='11')

# Actores
dot.node('Student', 'Estudiante', shape='box', style='filled', fillcolor='#E8F6FF')
dot.node('Teacher', 'Profesor', shape='box', style='filled', fillcolor='#FFF3E0')

# Casos de uso
dot.node('Lab', 'Laboratorios virtuales', shape='ellipse', style='filled', fillcolor='#E2F7E1')
dot.node('History', 'Aprendizaje inmersivo de historia', shape='ellipse', style='filled', fillcolor='#E2F7E1')
dot.node('Science', 'Simulaciones de ciencias', shape='ellipse', style='filled', fillcolor='#E2F7E1')
dot.node('Manage', 'Configurar experiencias XR', shape='ellipse', style='filled', fillcolor='#FFF6E6')

# Conexiones
dot.edge('Student', 'Lab')
dot.edge('Student', 'History')
dot.edge('Student', 'Science')
dot.edge('Teacher', 'Manage')
dot.edge('Teacher', 'Lab')
dot.edge('Teacher', 'History')
dot.edge('Teacher', 'Science')

# Exportar el archivo
print("Rendering use_cases SVG...")
dot.render(cleanup=False)  # genera modulo1/diagrams/use_cases.svg
print("Done: modulo1/diagrams/use_cases.svg")

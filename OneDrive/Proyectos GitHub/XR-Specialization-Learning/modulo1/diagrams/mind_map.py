# modulo1/diagrams/mind_map.py
from graphviz import Graph

# Usamos 'neato' para un layout tipo "mind-map" (más libre)
g = Graph('MindMap_XR', filename='modulo1/diagrams/mind_map', engine='neato', format='svg')
g.attr(overlap='false')
g.attr('node', shape='ellipse', fontsize='11')

# Nodo central
g.node('XR', 'XR\n(Extended Reality)', style='filled', fillcolor='#F0F8FF', fontsize='14')

# Conceptos principales
concepts = {
    'AR': 'AR\n(Realidad Aumentada)',
    'VR': 'VR\n(Realidad Virtual)',
    'MR': 'MR\n(Realidad Mixta)',
    'AV': 'AV\n(Virtualidad Aumentada)',
    'Continuum': 'Continuo\nRealidad–Virtualidad'
}

# Casos de uso / dispositivos / herramientas
cases = {
    'Devices': 'Dispositivos\n(smartphone, HoloLens, Quest)',
    'Apps': 'Apps\n(IKEA Place, Pokemon Go, Beat Saber)',
    'Tools': 'Herramientas\n(Unity, Unreal, WebXR)',
    'Edu': 'Educación\n(lab VR, historia inmersiva)'
}

# Añadir nodos y aristas
for k, label in concepts.items():
    g.node(k, label, style='filled', fillcolor='#E8F7FF')
    g.edge('XR', k)

for k, label in cases.items():
    g.node(k, label, style='filled', fillcolor='#FFF4E6')
    g.edge('XR', k)

# Conexiones adicionales (ejemplos)
g.edge('AR', 'Devices')
g.edge('VR', 'Apps')
g.edge('MR', 'Tools')
g.edge('Continuum', 'Edu')

print("Rendering mind_map SVG...")
g.render(cleanup=False)
print("Done: modulo1/diagrams/mind_map.svg")

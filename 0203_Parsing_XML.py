from defusedxml import ElementTree as ET
from defusedxml import EntitiesForbidden


# Fix: Use defusedxml
try:
    tree1 = ET.parse('billion_laughs.xml')
    print(len(tree1._root.text))
except EntitiesForbidden:
    print("Bad XML found")

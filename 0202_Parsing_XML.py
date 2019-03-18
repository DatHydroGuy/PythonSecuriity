from xml.etree import ElementTree as ET


"""
The "billion laughs" exploit works by taking advantage of element expansion within an XML file.
Note: ALL of the following standard XML parsers are vulnerable to this attack:
      sax, etree, minidom, pulldom, xmlrpc
"""
tree1 = ET.parse('billion_laughs.xml')

print(len(tree1._root.text))

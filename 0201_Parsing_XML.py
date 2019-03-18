from xml.etree import ElementTree as ET


# Note: ALL of the following standard XML parsers are vulnerable to this attack:
# sax, etree, minidom, pulldom, xmlrpc
tree1 = ET.parse('test.xml')

print(tree1._root.text)

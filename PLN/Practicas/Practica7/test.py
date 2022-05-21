import pandas as pd
import xml.etree.ElementTree as ET



tree = ET.parse('one.xml')
 
# getting the parent tag of
# the xml document
root = tree.getroot()
 
# printing the root (parent) tag
# of the xml document, along with
# its memory location
print(root.text)
 
# printing the attributes of the
# first tag from the parent

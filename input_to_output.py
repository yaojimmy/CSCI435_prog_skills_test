from lib2to3.pgen2.parse import ParseError
from pathlib import Path
import xml.etree.ElementTree as ET

if __name__ == '__main__':

    # iterate through every xml file in folder
    for file in Path("Programming-Assignment-Data").iterdir():

        if file.suffix == '.xml':
            print(file)
            try:
                myTree = ET.parse(file)
                myRoot = myTree.getroot()

                for node in myTree.iter('*'):
                    if len(node) == 0:
                        print(node.attrib['text'])
            except ParseError:
                pass
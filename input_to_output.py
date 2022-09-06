from pathlib import Path
import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

if __name__ == '__main__':

    # iterate through every xml file in folder
    for file in Path("Programming-Assignment-Data").iterdir():

        if file.suffix == '.xml':
            myTree = ET.parse(file)
            myRoot = myTree.getroot()

            with Image.open("Programming-Assignment-Data/" + os.path.splitext(file.name)[0] + ".png") as im:
                draw = ImageDraw.Draw(im)
                for node in myTree.iter('*'):
                    if len(node) == 0:
                        bounds = node.attrib['bounds']
                        bounds = bounds[1:]
                        bounds = bounds[:-1]

                        bounds = bounds[0:bounds.index(']')] + ',' + bounds[bounds.index('[')+1:]
                        bounds = bounds.split(',')
                        bounds = list(map(int, bounds))
                        w, h = bounds[2] - bounds[0], bounds[3] - bounds[1]
                        bounds = [(bounds[0], bounds[1]), (bounds[2], bounds[3])]

                        draw.rounded_rectangle(bounds, outline="yellow", width=3)
            
            im.save("Programming-Assignment-Output/" + os.path.splitext(file.name)[0] + ".png")
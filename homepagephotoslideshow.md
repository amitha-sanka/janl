**San Diego County, officially the County of San Diego, is a county in the southwestern corner of the U.S. state of California. San Diego is home to 3,298,634, making it California's second-most populous county and the fifth-most populous in the United States of America. The County provides a wide range of health, public safety, and community services to residents of the region's 18 cities and a large unincorporated area. San Diego County consists of several modern neighborhoods and communities. It is home to several beaches some popular beaches include La Jolla, Windansea, and Del Mar.** 

<script>
from IPython.display import HTML, display
from pathlib import Path   
from PIL import Image as pilImage 
from io import BytesIO
import base64
import numpy as np


class Image_Data:

    def __init__(self, source, label, file, path, baseWidth=320):
        self._source = source   
        self._label = label
        self._file = file
        self._filename = path / file 
        self._baseWidth = baseWidth

        # Open image and scale to needs
        self._img = pilImage.open(self._filename)
        self._format = self._img.format
        self._mode = self._img.mode
        self._originalSize = self.img.size
        self.scale_image()
       


    @property
    def source(self):
        return self._source  
    
    @property
    def label(self):
        return self._label 
    
    @property
    def file(self):
        return self._file   
    
    @property
    def filename(self):
        return self._filename   
    
    @property
    def img(self):
        return self._img
             
    @property
    def format(self):
        return self._format
    
    @property
    def mode(self):
        return self._mode
    
   @property
    def html(self):
        return self._html
    
    @property
    def html_grey(self):
        return self._html_grey

    def image_data(path=Path("images/"), images=None):  # path of static images is defaulted
    if images is None:  # default image
        images = [
            {'source': "Google", 'label': "Little Italy", 'file': "italy.jpeg"},
        ]
    return path, images

# turns data into objects
def image_objects():        
    id_Objects = []
    path, images = image_data()
    for image in images:
        id_Objects.append(Image_Data(source=image['source'], 
                                  label=image['label'],
                                  file=image['file'],
                                  path=path,
                                  ))
    return id_Objects

# Jupyter Notebook Visualization of Images
if __name__ == "__main__":
    for ido in image_objects(): # ido is an Imaged Data Object
        
        print("---- meta data -----")
        print(ido.label)
        print(ido.source)
        print(ido.file)
        print(ido.format)
        print(ido.mode)
        
        print("-- scaled image --")
        display(HTML(ido.html))
        
        print("--- grey image ---")
        display(HTML(ido.html_grey))
        
    print()
</script>

<style>

@charset "UTF-8";


#SLIDE_BG {
    width: 100%;
    height: 100vh;
    background-position: center center;
    background-size: cover; 
    background-repeat: no-repeat; 
    backface-visibility: hidden;
    animation: slideBg 20s linear infinite 0s; 
    animation-timing-function: ease-in-out;
    background-image: url('/lajolla.jpg');
}

@keyframes slideBg {
    0% {
        background-image: url('/lajolla.jpg'); 

    }
    10% {
        background-image: url('/balboapark.jpg'); 

    }
    20% {
        background-image: url('/padrespark.jpg'); 

    }
    30% {
        background-image: url('/pier.jpg'); 

    }
    40% {
        background-image: url('/belmont.jpeg');
    }
    50% {
        background-image: url('/airandspace.jpeg');
    }
    60% {
        background-image: url('/cliffs.jpeg');
    }
    70% {
        background-image: url('/seaport.jpeg');
    }
    80% {
        background-image: url('/gaslampquarter.jpg'); 

    }
    90% {
        background-image: url('/italy.jpeg');
    }
    100% {
        background-image: url('/sdzoo.jpeg');
    }
}

</style>

<html>
<head>
<meta charset="UTF-8">
</head>
</html>

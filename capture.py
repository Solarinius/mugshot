from cv2 import VideoCapture, imwrite, CAP_DSHOW
from datetime import datetime
from pathlib import Path

cam = VideoCapture(0,CAP_DSHOW) # initialize the camera 

def getPhoto(camera:VideoCapture):
    result, image = camera.read()
    if result:
        path = Path.home() / "Pictures/MugShots/"
        if (not Path.exists(path)):
            Path.mkdir(path)
        
        now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S-%f")

        name = f"{path / now}.png"

        imwrite(name, image) #save mugshot
    else:
        with(open(f"{path}/access.log",'w')) as f:
            f.write(f"Someone tried at {now}, but no image")

if __name__ == "__main__":
    getPhoto(cam)



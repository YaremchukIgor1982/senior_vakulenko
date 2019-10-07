import os

from imageai.Detection import ObjectDetection


def test_Image_aI():
   exec_path=os.getcwd()
   detector = ObjectDetection()
   detector.setModelTypeAsRetinaNet()
   detector.setModelPath(exec_path)
   detector.loadModel()
   list = detector.detectObjectsFromImage(input_image=os.path.join(exec_path,'home.png'))

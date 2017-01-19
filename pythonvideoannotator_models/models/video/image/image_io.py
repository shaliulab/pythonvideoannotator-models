import os, cv2
from send2trash import send2trash
from pythonvideoannotator_models.models.video.image.image_base import ImageBase

class ImageIO(ImageBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, images_path=None):
		conf_path = os.path.join(self.object_path, 'dataset.json')
		with open(conf_path, 'w') as outfile: json.dump({'factory-function':'create_image'}, outfile)
		
		image_path = os.path.join(images_path, self.name+'.png')
		cv2.imwrite(image_path, self.image)
		return data

	def load(self, data, image_path=None):
		self.image = cv2.imread(image_path)
		self.name  = os.path.basename(image_path)[:-4]
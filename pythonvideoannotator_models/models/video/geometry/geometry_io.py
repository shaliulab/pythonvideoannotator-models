import os, cv2
from send2trash import send2trash
from pythonvideoannotator_models.models.video.geometry.geometry_base import GeometryBase

class GeometryIO(GeometryBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, geometries_path=None):
		geo_path = os.path.join(geometries_path, self.name+'.geo')

		conf_path = os.path.join(self.object_path, 'dataset.json')
		with open(conf_path, 'w') as outfile: json.dump({'factory-function':'create_object'}, outfile)
		
		cv2.imwrite(image_path, self.image)
		return data

	def load(self, data, geometry_path=None):
		self.image = cv2.imread(image_path)
		self.name  = os.path.basename(image_path)[:-4]
import os, json
from pythonvideoannotator_models.models.imodel import IModel

class Dataset(IModel):

	def __init__(self, object2d):		
		super(IModel, self).__init__()

		object2d   		+= self
		self.object2d   = object2d
		self.name 		= 'dataset({0})'.format(len(object2d.datasets))


	@property
	def object2d(self): return self._object2d
	@object2d.setter
	def object2d(self,value): self._object2d = value

	@property
	def directory(self): return os.path.join( self.object2d.directory, 'datasets',self.name)


	def save(self, data, datasets_path):
		conf_path = os.path.join(self.directory, 'dataset.json')
		with open(conf_path, 'w') as outfile: json.dump(data, outfile)
		return data

	def load(self, data, dataset_path):
		pass


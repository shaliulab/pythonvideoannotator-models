import os
from pythonvideoannotator_models.models.imodel import IModel
from pythonvideoannotator_models.models.video.objects.object2d.datasets.path import Path
from pythonvideoannotator_models.models.video.objects.object2d.datasets.contours import Contours
from pythonvideoannotator_models.models.video.objects.object2d.datasets.value import Value

class Object2dBase(IModel):

	def __init__(self, video):		
		super(IModel, self).__init__()

		self._video = video
		self._video += self

		self._datasets   = []	
		self.name 		 = 'object({0})'.format(len(video)) if len(video)>0 else 'object'

		


	######################################################################
	### OBJECT FUNCTIONS #################################################
	######################################################################

	def create_path(self): return Path(self)
	def create_contours(self): return Contours(self)
	def create_value(self): return Value(self)

	def draw(self, frame, frame_index):
		for dataset in self.datasets: dataset.draw(frame, frame_index)
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): return len(self._datasets)
	def __str__(self): return self.name

	def __add__(self, obj):
		if isinstance(obj, Path): self._datasets.append(obj)
		if isinstance(obj, Contours): self._datasets.append(obj)
		if isinstance(obj, Value): self._datasets.append(obj)
		return self

	def __sub__(self, obj):
		if isinstance(obj, Path): self._datasets.remove(obj)			
		if isinstance(obj, Contours): self._datasets.remove(obj)			
		if isinstance(obj, Value): self._datasets.remove(obj)			
		return self

	def __len__(self): 				return len(self.datasets)
	def __getitem__(self, index): 	return self.datasets[index] if index<len(self) else None

	######################################################################
	### PROPERTIES #######################################################
	######################################################################

	@property
	def video(self): return self._video
	@video.setter
	def video(self, value): self._video = value

	@property
	def datasets(self): return self._datasets
	@datasets.setter
	def datasets(self, value): self._datasets = value

	@property
	def paths(self): 
		for dataset in self._datasets:
			if isinstance(dataset, Path): 
				yield dataset


	@property
	def directory(self): return os.path.join( self.video.directory, 'objects',self.name )
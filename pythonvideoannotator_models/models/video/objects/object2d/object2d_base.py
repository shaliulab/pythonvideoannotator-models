from pythonvideoannotator_models.models.video.objects.object2d.datasets.path import Path

class Object2dBase(object):

	def __init__(self, video):
		self._datasets   = []	
		self._name 		 = 'Undefined'

		self._video = video
		self._video += self


	######################################################################
	### OBJECT FUNCTIONS #################################################
	######################################################################

	def create_path(self): return Path(self)		

	def draw(self, frame, frame_index):
		for dataset in self.datasets: dataset.draw(frame, frame_index)
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __str__(self): return self.name

	def __add__(self, obj):
		if isinstance(obj, Path): self._datasets.append(obj)
		return self

	def __sub__(self, obj):
		if isinstance(obj, Path): self._datasets.remove(obj)
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
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value

	@property
	def datasets(self): return self._datasets
	@datasets.setter
	def datasets(self, value): self._datasets = value

	@property
	def paths(self): return [dataset for dataset in self._datasets if isinstance(dataset, Path)]
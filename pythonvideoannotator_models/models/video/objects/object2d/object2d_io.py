import os
from send2trash import send2trash
from pythonvideoannotator_models.models.video.objects.object2d.object2d_base import Object2dBase
from pythonvideoannotator_models.utils.tools import list_folders_in_path

class Object2dIO(Object2dBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, project_path=None):
		object_path = os.path.join(project_path, self.name)
		if not os.path.exists(object_path): os.makedirs(object_path)

		datasets_path = os.path.join(object_path, 'datasets')
		if not os.path.exists(datasets_path): os.makedirs(datasets_path)
		
		datasets = []
		for dataset in self._datasets:
			data = dataset.save(data, datasets_path)
			datasets.append(data['path'])
		
		for dataset_path in list_folders_in_path(datasets_path):
			if dataset_path not in datasets:
				if os.path.exists(dataset_path):
					send2trash(dataset_path)
					
		return data

	def load(self, data, object_path=None):
		dirname 		= os.path.basename(object_path)
		name, extension = os.path.splitext(dirname)
		self.name 		= name

		datasets_path = os.path.join(object_path, 'datasets')
		
		for dataset_path in list_folders_in_path(datasets_path):
			name = os.path.basename(dataset_path)
			dataset_type, name = name.split('-')[0], '-'.join(name.split('-')[1:])
			if dataset_type=='path':
				dataset 		= self.create_path()
				dataset.name 	= name
				dataset.load(data, dataset_path)
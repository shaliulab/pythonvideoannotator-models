from pythonvideoannotator_models.models.video.objects.object2d.datasets.dataset import Dataset

class ValueBase(Dataset):

	def __init__(self, object2d):
		super(ValueBase, self).__init__(object2d)
		self.name 	 = 'value({0})'.format(len(object2d))  if len(object2d)>0 else 'value'
		self._values = []

		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __len__(self): 				return len(self._values)
	def __getitem__(self, index): 	return self._values[index] if index<len(self) else None
	def __str__(self):				return self.name

	######################################################################
	### DATA MODIFICATION AND ACCESS #####################################
	######################################################################

	def get_value(self, index):
		if index<0 or index>=len(self): return None
		return self[index] if self[index] is not None else None

	def set_value(self, index, val):
		# add positions in case they do not exists
		if index >= len(self):
			for i in range(len(self), index + 1): self._values.append(None)

		# create a new moment in case it does not exists
		self._values[index] = val
import os
from pythonvideoannotator_models.models.video.objects.object2d.datasets.value.value_base import ValueBase

class ValueIO(ValueBase):

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, datasets_path=None):
		if not os.path.exists(self.directory): os.makedirs(self.directory)

		data['factory-function'] = 'create_value'

		dataset_file = os.path.join(self.directory, 'values.cvs')
		with open(dataset_file, 'w') as outfile:
			outfile.write(';'.join(['frame','value'])+'\n' )
			for index in range(len(self)):
				val = self.get_value(index)
				row = [index] + [val]
				outfile.write(';'.join( map(str,row) ))
				outfile.write('\n')

		super(ValueIO,self).save(data, datasets_path)
		return data

	def load(self, data, dataset_path=None):
		dataset_file = os.path.join(dataset_path, 'values.cvs')
		
		with open(dataset_file, 'r') as infile:
			infile.readline()
			for i, line in enumerate(infile):
				csvrow = line[:-1].split(';')

				if csvrow[1] is None: continue
				if len(csvrow[1])==0: continue
				if csvrow[1]=='None': continue

				frame = int(csvrow[0])
				value = eval(csvrow[1])
				self.set_value(frame, value)
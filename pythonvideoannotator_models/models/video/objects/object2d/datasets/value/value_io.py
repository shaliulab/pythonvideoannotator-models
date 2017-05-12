import os
from pythonvideoannotator_models.models.video.objects.object2d.datasets.value.value_base import ValueBase

class ValueIO(ValueBase):

	FACTORY_FUNCTION = 'create_value'

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, dataset_path=None):
		data = super(ValueIO, self).save(data, dataset_path)

		dataset_file = os.path.join(dataset_path, 'values.cvs')
		with open(dataset_file, 'wb') as outfile:
			outfile.write((';'.join(['frame','value'])+'\n' ).encode( ))
			for index in range(len(self)):
				val = self.get_value(index)
				row = [index] + [val]
				outfile.write((';'.join( map(str,row) )).encode( ) )
				outfile.write(b'\n')

		return data

	def load(self, data, dataset_path=None):
		data = super(ValueIO, self).load(data, dataset_path)

		dataset_file = os.path.join(dataset_path, 'values.cvs')
		
		with open(dataset_file, 'rb') as infile:
			infile.readline()
			for i, line in enumerate(infile):
				csvrow = line[:-1].split(b';')

				if csvrow[1] is None: continue
				if len(csvrow[1])==0: continue
				if csvrow[1]=='None': continue

				frame = int(csvrow[0])
				value = eval(csvrow[1])
				self.set_value(frame, value)

		return data
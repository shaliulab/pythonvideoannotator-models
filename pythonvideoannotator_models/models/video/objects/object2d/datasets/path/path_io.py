import os
from pythonvideoannotator_models.models.video.objects.object2d.datasets.path.path_base import PathBase

class PathIO(PathBase):

	FACTORY_FUNCTION = 'create_path'


	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, dataset_path=None):
		data = super(PathIO, self).save(data, dataset_path)

		dataset_file = os.path.join(dataset_path, 'path.cvs')
		with open(dataset_file, 'wb') as outfile:
			outfile.write((';'.join(['frame','x','y'])+'\n').encode())
			for index in range(len(self)):
				pos = self.get_position(index)
				row = [index] + ([None, None] if pos is None else list(pos))
				outfile.write((';'.join( map(str,row) )).encode( ))
				outfile.write(b'\n')


		super(PathIO,self).save(data, dataset_path)
		return data

	def load(self, data, dataset_path=None):
		data = super(PathIO, self).load(data, dataset_path)

		dataset_file = os.path.join(dataset_path, 'path.cvs')

		with open(dataset_file, 'rb') as infile:
			infile.readline()
			for i, line in enumerate(infile):
				csvrow = line[:-1].split(b';')

				if csvrow[1] is None or csvrow[2] is None: 		continue
				if len(csvrow[1])==0 or len(csvrow[2])==0: 		continue
				if csvrow[1] == b'None' or csvrow[2] == b'None':continue
				
				frame, x, y = int(csvrow[0]), int(csvrow[1]), int(csvrow[2])
				self.set_position(frame, x, y)

		return data
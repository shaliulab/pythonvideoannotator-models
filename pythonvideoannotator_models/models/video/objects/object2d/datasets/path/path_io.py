import os
from pythonvideoannotator_models.models.video.objects.object2d.datasets.path.path_base import PathBase

class PathIO(PathBase):

	def get_csvrow(self, index): 
		pos = self.get_position(index)
		if pos is None: pos = [None, None]
		return [index] + list(pos)

	def load_csvrow(self, index, csvrow): 
		if csvrow[1] is None or csvrow[2] is None or len(csvrow[1])==0 or len(csvrow[2])==0: return
		if csvrow[1] == 'None' or csvrow[2] == 'None': return
		frame, x, y = int(csvrow[0]), int(csvrow[1]), int(csvrow[2])
		self.set_position(frame, x, y)

	######################################################################################
	#### IO FUNCTIONS ####################################################################
	######################################################################################

	def save(self, data, datasets_path=None):
		if not os.path.exists(self.directory): os.makedirs(self.directory)

		data['factory-function'] = 'create_path'

		dataset_file = os.path.join(self.directory, 'path.cvs')
		with open(dataset_file, 'w') as outfile:
			outfile.write(';'.join(['frame','x','y'])+'\n' )
			for index in range(len(self)):
				pos = self.get_position(index)
				row = [index] + ([None, None] if pos is None else list(pos))
				outfile.write(';'.join( map(str,row) ))
				outfile.write('\n')


		super(PathIO,self).save(data, datasets_path)
		return data

	def load(self, data, dataset_path=None):
		dataset_file = os.path.join(dataset_path, 'path.cvs')

		

		with open(dataset_file, 'r') as infile:
			infile.readline()
			for i, line in enumerate(infile):
				csvrow = line[:-1].split(';')
				self.load_csvrow(i, csvrow)

				if csvrow[1] is None or csvrow[2] is None: 		continue
				if len(csvrow[1])==0 or len(csvrow[2])==0: 		continue
				if csvrow[1] == 'None' or csvrow[2] == 'None': 	continue
				
				frame, x, y = int(csvrow[0]), int(csvrow[1]), int(csvrow[2])
				self.set_position(frame, x, y)
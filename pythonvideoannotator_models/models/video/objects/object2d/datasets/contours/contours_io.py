import os, base64, numpy as np
from pythonvideoannotator_models.models.video.objects.object2d.datasets.contours.contours_base import ContoursBase

class ContoursIO(ContoursBase):

	FACTORY_FUNCTION = 'create_contours'

	def save(self, data, dataset_path=None):
		data = super(ContoursIO, self).save(data, dataset_path)

		contours_file = os.path.join(dataset_path, 'contours.csv')
		with open(contours_file, 'wb') as outfile:
			outfile.write(';'.join(['frame','contour','shape'])+'\n' )
			for index in range(len(self)):
				contour = self.get_contour(index)
				row = [index] + ([None, None] if contour is None else [base64.b64encode(contour), contour.shape])
				outfile.write(';'.join( map(str,row) ))
				outfile.write('\n')

		return data

	def load(self, data, dataset_path=None):
		data = super(ContoursIO, self).load(data, dataset_path)

		contours_file = os.path.join(dataset_path, 'contours.csv')
		
		if os.path.exists(contours_file):
			with open(contours_file, 'r') as infile:
				infile.readline()
				for i, line in enumerate(infile):
					csvrow = line[:-1].split(';')
					
					if csvrow[1] is None or csvrow[2] is None: 		continue
					if len(csvrow[1])==0 or len(csvrow[2])==0: 		continue
					if csvrow[1] == 'None' or csvrow[2] == 'None': 	continue
					
					frame = int(csvrow[0])
					shape = eval(csvrow[2])
					contour = np.frombuffer(base64.decodestring(csvrow[1]), np.int32)
					contour = contour.reshape(shape)
					self.set_contour(frame, contour)


		return data
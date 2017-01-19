from pythonvideoannotator_models.models.video.objects.video_object import VideoObject


class GeometryBase(VideoObject):

	def __init__(self, video):
		super(GeometryBase, self).__init__()

		self.name 	= 'geometry({0})'.format(len(video)) if len(video)>0 else 'geometry'
		self._geometry 	= []

		self._video = video
		self._video += self

	######################################################################
	### OBJECT FUNCTIONS #################################################
	######################################################################
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __str__(self): return self.name
	
	

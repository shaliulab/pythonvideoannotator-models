from pythonvideoannotator_models.models.video.objects.video_object import VideoObject


class NoteBase(VideoObject):

	def __init__(self, video):
		super(NoteBase, self).__init__()

		self.name 	= 'note({0})'.format(len(video)) if len(video)>0 else 'note'
		self._note 	= ''

		self._video = video
		self._video += self

	######################################################################
	### OBJECT FUNCTIONS #################################################
	######################################################################
		
	######################################################################
	### CLASS FUNCTIONS ##################################################
	######################################################################

	def __str__(self): return self.name
	
	######################################################################
	### PROPERTIES #######################################################
	######################################################################
	
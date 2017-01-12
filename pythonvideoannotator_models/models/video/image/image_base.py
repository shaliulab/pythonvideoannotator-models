from pythonvideoannotator_models.models.imodel import IModel

class ImageBase(IModel):

	def __init__(self, video):
		super(IModel, self).__init__()

		self.name 	= 'image({0})'.format(len(video)) if len(video)>0 else 'image'
		self.image 	= None

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

	@property
	def video(self): return self._video
	@video.setter
	def video(self, value): self._video = value

	@property 
	def video_capture(self):  return self.video.video_capture
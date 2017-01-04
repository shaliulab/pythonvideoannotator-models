

class ImageBase(object):

	def __init__(self, video):
		self.name 	= 'image-{0}'.format(len(video.images))
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
	def name(self): return self._name
	@name.setter
	def name(self, value): self._name = value

	@property 
	def video_capture(self):  return self.video.video_capture
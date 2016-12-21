# Python video annotator Model

This library is part of [Python Video Annotator](http://pythonvideoannotator.readthedocs.io) application.


## What are the models?

The models are classes used to organize the data within the application.

### Data and models structure

+-- Project (model)
|   +-- Video (model)
	|	+-- OBJECTS (concept)
		|	+-- Object2d (model)
			|	+-- DATASETS (concept)
				|	+-- Path (Model)

(model) - It means that the element in the hierarchy exists and is implemented in a class.
(concept) - It means that the element in the hierarchy is present just as a concept and does not have any class implementing it.

#### Project
| Name | Description |
|---|---|
|Project| This class is responsible for manage the videos. |
|-- Video| This class is responsible for manage the diferent types of objects present in the video. Currently only the Object2D exists. |
|---- Objects2D| This class is responsible for manage the object datasets. Currently only the path dataset is implemented|
|------ Path| Implementation of the object path dataset.|

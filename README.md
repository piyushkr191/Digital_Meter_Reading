# Automated Visual Inspection of Digital Meter Reading

Project Overview :
This project develops an automated visual inspection system for electric meter reading using traditional image processing techniques and the YOLOv8 object detection model. The system aims to enhance the accuracy and efficiency of meter reading, reducing the need for manual labor and associated costs.


Table of Contents :

	Introduction  
	Primary Objective  
	Specific Objectives  
	Technologies Used  
	Dataset  
	Methodology  
	Results  
	Conclusion  
	Learning Outcomes & Personal Experience  
	How to Run the Project  
	References  

Introduction :
	
The primary goal of this project is to develop an end-to-end application for automated electric meter reading. Leveraging advanced object detection and traditional image processing techniques, this system is designed to minimize costs and labor requirements by automating the reading process.


Primary Objective	:

The main objective is to create a robust application for detecting and reading electric meter values automatically. The application utilizes the YOLOv8 model for object detection and various traditional image processing techniques for numeric extraction.


	Specific Objectives	
	
	Object Detection with YOLOv8
	
	Develop and implement a custom-trained YOLOv8 object detection model.
	
	Detect the electric meter in the uploaded image by forming a contour around it.	
	
	Numeric Extraction with Traditional Image Processing		
	
	Utilize traditional image processing techniques to extract numeric data from the detected electric meter.		
	
	Process the uploaded image through methods such as resizing, color conversion, blurring, edge detection, and contour approximation to accurately identify and extract the numeric information displayed on the meter.		



Technologies Used :

	YOLOv8 Model for Meter Detection: Used for accurately identifying electric meters in real-time.
	
	Traditional Image Processing Techniques: Applied for preprocessing, postprocessing, and numeric extraction tasks.
	
	Django Framework: Used to develop the web application, handling user interactions, image uploads, and backend processing.
	
	Dataset Acquisition
	The dataset comprises 900 raw images of electric meters, provided by the project mentor. These images were initially non-annotated.
	
	
	Labelling
	The images were annotated using the Roboflow platform, marking the electric meters to create a labeled dataset for training the YOLOv8 model.


Methodology :

Django Web Application Implementation

The application was developed using Django, a high-level Python web framework known for its simplicity and robustness.

Meter Detection :

        Model Training: The YOLOv8 model was trained on the annotated dataset to detect electric meters accurately.
        
        Detection Process: The trained model was used to detect meters in user-uploaded images, drawing contours around detected meters.

Image Analysis :

        Preprocessing: Includes resizing, cropping, rotation, color conversion, and blurring to prepare the images for further analysis.
        
        Postprocessing: Techniques such as contour approximation, bounding box creation, and morphological transformations are used to refine detected regions.
        
        Numeric Extraction: Involves extracting numeric data from the meter's seven-segment display using edge detection and contour analysis.


        

Results :  

        Project Outcomes :
        
        The custom-trained YOLOv8 model achieved high accuracy in detecting electric meters in user-uploaded images. The traditional image processing techniques for numeric extraction further enhanced system reliability.
        
        
        Comparison with Objectives :
        
        The project met its primary and specific objectives, providing a robust and scalable solution with improved accuracy and efficiency compared to manual methods.


Conclusion :

The project successfully developed an end-to-end application for automated electric meter reading. By leveraging YOLOv8 and traditional image processing techniques, the system provided an efficient, accurate, and scalable solution for meter reading. This success lays the groundwork for future enhancements and potential integration with advanced machine learning models.


Learning Outcomes & Personal Experience :

    Learning Outcomes :
  
    Hands-on experience with YOLOv8 for object detection.
    
    Enhanced understanding of traditional image processing techniques.
    
    Skills in web application development using the Django framework.
    
    Personal Experience :
    
    The project provided valuable insights into the challenges and solutions associated with automated meter reading, offering a comprehensive learning experience and reinforcing the importance of interdisciplinary knowledge.


How to Run the Project


Clone the Repository:
	git clone <repository-url>
	cd <repository-directory>

Install Dependencies:
	pip install -r requirements.txt

Set Up the Django Application:
	python manage.py migrate
	python manage.py runserver

Access the Web Application:
	Open a web browser and go to http://127.0.0.1:8000/.

Upload Images:
	Use the web interface to upload images of electric meters for detection and reading.

References

		John Canny, "A Computational Approach to Edge Detection," IEEE Transactions on Pattern Analysis and Machine Intelligence, 1986.
		
		N. Otsu, "A Threshold Selection Method from Gray-Level Histograms," IEEE Transactions on Systems, Man, and Cybernetics, 1979.
		
		Y. LeCun, Y. Bengio, and G. Hinton, "Deep Learning," Nature, 2015.
		
		A. Krizhevsky, I. Sutskever, and G. H. Hinton, "ImageNet Classification with Deep Convolutional Neural Networks," Advances in Neural Information Processing Systems, 2012.
		
		Li Deng and Dong Yu, "Deep Learning: Methods and Applications," Foundations and Trends in Signal Processing, 2014.
		
		C. Olah, "Understanding LSTM Networks," 2015.
		
		Samuel Chan : https://github.com/onlyphantom/cvessentials/tree/master


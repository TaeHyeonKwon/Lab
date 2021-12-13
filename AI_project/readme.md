+ Music recommendation system by emotion recognition

+ Dataset and model are saved in Google Drive. This is the link. Before you implement code, you should compress the .zip file 
   + https://drive.google.com/file/d/1QkyqH9eHkGuzljyZsKFKYhKxSqeeXHbG/view?usp=sharing
   + Contains:
      + Celebrity image 
         + https://www.kaggle.com/hereisburak/pins-face-recognition
      + FER2013
         + https://www.kaggle.com/msambare/fer2013
      + Spotify 

+ Part 1 
  + Face recognition
      + Face extract from original image with **MTCNN**
      + Train image embedding with **FaceNet** 

+ Part 2 
  + Emtion analyze
      + Use **FER2013** Dataset, to recognize the emotion from extracted face

+ Part 3
  + Music recommendation
      + Use the **Spotify** dataset, divide the music by two emotion(happy,sad). it is divided by k-means clustering method.


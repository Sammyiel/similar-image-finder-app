# similar-image-finder-app
Short desc: A Deep Learning model to find similar images

# Video Demonstration on the App
https://drive.google.com/drive/folders/1AXxBMMSzgH38koRimIR_yGU8g5xeTtYa?usp=share_link

# Link to deployed Flask App on Heroku
https://similar-image-finder-app.herokuapp.com/

# Link to Project Proposal
https://docs.google.com/document/d/1x8gOq7GQxqTLIOmte6EVQ7l86ggpbnu9jUE76J2oktA/edit


# Long description
This project is setting up a deep learning model to classify images from the CIFAR-100 dataset. The CIFAR-100 dataset consists of 60,000 32x32 color training images and 10,000 test images, labeled over 100 classes. The code first loads the CIFAR-100 dataset using the cifar100 module from Keras, and then prints the shape of the training and testing data. It also prints the number of classes and the names of the classes.

Next, the code reshapes the training and testing data from (number of samples, 32, 32, 3) to (number of samples, 32, 32, 3), where the 3 represents the R, G, B channels in the image. It then normalizes the training and testing data by dividing each pixel value by 255.

The code then one-hot encodes the training labels and splits the training data into a training and validation set using the train_test_split function from sklearn.

Finally, the code sets up a deep learning model using the Keras Sequential model and adds various layers to it, including 2D convolutional layers, max pooling layers, and fully connected layers. The model will be trained using the Adam optimizer and categorical cross-entropy loss.

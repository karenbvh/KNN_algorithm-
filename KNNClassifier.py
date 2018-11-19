import os
import turtle
import time
import math
import random
import operator



class Face:
    """ A Face holds an image, an expression and some quantitative feature data.

        Attributes:
            name : An identifying name, like "David"
            image : In this case, the string registered with the turtle for this image.
            expression: A string giving the expression type. One of 'neutral', 'smiling', or 'surprised'
            smile_width_percent : The percent of the face width taken by the smile width. Stored as 0.0-1.0.
            smile_height_percent : The percent of the face width taken by the smile height. Stored as 0.0-1.0.
            distance : a number giving the error between this object and an unclassified sample.
                        Filled in by the classifier.
    """
    
    def __init__(self, name, image, expression, width, smile_width, smile_height):
        """ Initializer for Face.

        Args: # self is not listed
            name : An identifying name, like "David"
            image : In this case, the string registered with the turtle for this image.
            expression: A string giving the expression type. One of 'neutral', 'smiling', or 'surprised'
            width : The width of the face in pixels (or scaled pixels)
            smile_width : The width of the smile in pixels (or scaled pixels)
            smile_height : The height of the smile in pixels (or scaled pixels)

            Use these args to set the attributes listed above.
        
        """

    def measure_error(self, otherFace):
        """ Measure and return the error, or distance, between self and otherFace.
            The error should be the sqrt of the difference in smile_width_percent squared plus
            the difference in smile_height_percent squared.
        """

    def label(self):
        """ label should return whatever value is being classified. For
            a Face, that is its expression attribute.
        """

    def coord(self):
        """ Returns the attributes scaled to fit on a screen, in this
            case as the smile width and height as a percentage 0-100.
        """

    def color(self):
        """ The color method decides how a Face object with a given
            expression should be colored by returning a color string.
            I have chosen:
                "neutral" -> "gray"
                "smiling" -> "green"
                "surprised" -> "red"
        """

    def draw_sample(self, turtle, highlight = False):
        """ Draws a dot at the coord() location. Look at the turtle dot method and use that.
            Draw the dot the color of the object as provided by the color() method.
        Args:
            turtle: The turtle used to draw.
            highlight : An optional argument. If True, draw the dot bigger.
        """


class KNNClassifier:
    """ This class implements a simple K Nearest Neighbor classifier.
    Attributes:
        k : an int giving the number of nearest neighbors that vote on a classification.
        samples: a list of samples with known classifications.
        kSet : The set of k closest samples. Only gets filled in after calling the tally_votes method.
        votes : A dictionary of classifications and the number of samples in the kSet that voted for it.
    """
    def __init__(self, k):
        self.samples = [] # replace with code
    
    def add_sample(self, sample):
        """ Adds a sample to the internal set of samples. """
        pass
    
    def compute_error_measure_from_new_sample_to_samples(self, new_sample):
        """ Given an unknown new sample, measure the error between it and all the internal samples. """
        pass
    
    def find_k_closest(self):
        """ Once the sample error has been measured, sort them, pick the k closest.
            Store the k-closest in self.kSet.
        """
        pass
    
    def tally_votes_in_nearest_set(self):
        """ Make a dictionary of votes.
        """
        pass
    
    def find_highest_vote(self):
        """ Given a vote dictionary, pick the key that has the most votes.
            This is the classification of the unknown sample.
        """
        pass
    
    def kNN_to_sample(self, test_sample):
        """ Given a test sample, classify according to the stored samples.
            Runs the main kNN algorithm:
                - compute error to all samples
                - sort the samples by error and pick the k-closest
                - tally the votes of the k-closest
                - pick the winner
        """
        return "need to implement", 1
    
    def draw_samples(self, turtle):
        """ Given a turtle, draw all the samples by calling the samples' draw_sample method."""
        pass
    
    def draw_kSet(self, test_sample, turtle):
        """ Given a turtle, draw lines from the test_sample to the k-nearest samples."""
        pass    

# A helper function that breaks up the image name to get feature data
# and calls the Face initializer with that data.
def make_face_from_filename(filename, image):
    remove_extension = filename.split(".")[0]
    parts = remove_extension.split("_")
    return Face(parts[0], image, parts[1], int(parts[2]), int(parts[3]), int(parts[4]))


# Run the main program. It reads the images from a faces directory, puts them in a classifier, and
# computes the classification. It draws the test sample image and the closest match image, then
# draws the graph of samples plotted by their mouth width and moth height and draws lines from
# the test sample to the nearest neighbors.
def main():

    # Create the turtle screen and set its size and x and y coordinates
    screen = turtle.Screen()      # Creates a playground for turtles
    screen.setup(500,500)
    # bottom left is now (0,0) and top right is (150,150)
    # Basically 0-100% plus some extra space.
    screen.setworldcoordinates(0,0,150,150)

    # Set up the turtle    
    data_turtle = turtle.Turtle()
    data_turtle.speed(50)
    data_turtle.hideturtle()

    # collect the files in the faces folder
    files = os.listdir("faces")
    filelist = []

    # make an empty kNN classifier with a k of 5
    classifier = KNNClassifier(5)

    # For each file
    #   - register the image with the screen
    #   - make a Face object
    #   - add the Face object to the classifier sample set
    for file in files:
        if ".gif" in file:
            filename = "faces/"+file
            turtle.register_shape(filename)
            filelist.append(filename)
            face = make_face_from_filename(file, filename)
            classifier.add_sample(face)

    # If we use all the samples, we don't have any unknown ones.
    # Pull out a sample from the classifier and store in test_sample
    if classifier.samples:
        random_index = random.randint(0,len(classifier.samples)-1)
        test_sample = classifier.samples[random_index]
        classifier.samples.remove(test_sample)

        # Draw the samples as dots on the screen
        classifier.draw_samples(data_turtle)
        test_sample.draw_sample(data_turtle, True)
        # Classify the test sample with the samples stored in the classifier
        classification = classifier.kNN_to_sample(test_sample)
        
        print("The classifier voted for", classification,
              "and is it is really marked as", test_sample.label())

        # Draw connecting lines from the test_sample to the closest matches
        classifier.draw_kSet(test_sample, data_turtle)

        # Show the test sample image and the closest match image
        data_turtle.goto(30,130)
        data_turtle.shape(test_sample.image)
        data_turtle.stamp()
        data_turtle.goto(20,90)
        data_turtle.write("sample", font=("Arial",24,"normal"))
        data_turtle.goto(120,130)
        data_turtle.shape(classifier.kSet[0].image)
        data_turtle.stamp()
        data_turtle.goto(90,90)
        data_turtle.write("closest match", font=("Arial",24,"normal"))
        
main()

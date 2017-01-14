# Pack the Box.

You have a container. Given a series of items of the same size and shape, what space efficiency can be achieved by randomly selecting an x,y coordinate at which to place each item inside the container?

* Is efficiency greater or smaller when items are smaller?
* What shapes fare better than others?
* Does the size of the container matter?

Test your hypotheses, and see how efficient your outcomes can be.

![User Input](/x_documentation/user-input.gif)
![Defaults](/x_documentation/defaults-4frames.gif)
![Default Results](/x_documentation/default-results-one.png)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

PREREQUISITES: The algorithm is built to run with Python 3. The [Turtle](https://docs.python.org/3.0/library/turtle.html) graphics library executes the drawing functions to visualize the spatial outcome. Turtle uses [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) for its graphics, so be sure to install a version of Python with Tk support.

## Testing Your Hypotheses

A few instructions to start testing your hypotheses:

Clone the git repository.

```
https://github.com/tdiede/packthebox.git
```

Run the script.py file and input your initial container dimensions.


```
python script.py
What is the height of your container? default:600 >>>
What is the width of your container? default:500 >>>
```

The shape of the item is randomized between a rectangle or a circle.
Enter your desired dimensions, depending on the shape.

```
What is the desired height/width of your rectangle? default:40,90 >>>
What is the desired radius of your circle? default:40 >>>
```

The script will execute based on these parameters and the random placement of items in the container.
At the end, the spatial efficiency value is returned.

![Circles Results](/x_documentation/large-container-circles-results.gif)

## Runtime

The current solution's wost-case runtime is
```
O(n*(n-1))
```
This is because the program checks every existing item in the container before determining whether the current x,y coordinate would cause overlap. An additional runtime of ``` n*(LOOP_LIMIT-1) ``` should be considered in case the max number of placement attempts happens to have been exceeded for every single item added.

## Author

* **Therese Diede** - Software Engineer

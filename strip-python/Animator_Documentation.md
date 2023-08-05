# Documentation for the Animator class:

## What is Animator?:

Animator is a 1 dimensional pixel processor letting you create your own animations,
and easily control the rendering of frames, and even blending of several animations at the same time.

In other words, it's a class for handling processing of animations for LED light strips like the neopixel ws2812b

## How to initialize the Animator class:

To initialize the Animator class, you must provide two arguments:

* data
* config

Both of these arguments are given as dictionaries. Now let's look at their contents:

### data:

This argument contains all data needed by animations available to the Animator. For more information, see [How is an animation defined?](#how-is-an-animation-defined)

### config:

This argument contains, as the name suggests, configuration data for the Animator. Through this argument, you can define how the Animator handles data to best suit your needs. 

let's take a look at what parameters you can provide:

#### numPixels:

This value is quite simple. This value must be an integer, and tells the Animator how many pixels it has to work with.

#### frameRate:

This value Defines how many frames the Animator will render every second.

#### animateFunction:

This value must be provided as a function that will define how the Animator will animate the frames it generates. This allows you to define where the frame data will  be sent after it is rendered, meaning you can use any library you want to actually send the pixel data to your light strip.

More information on how this function is implemented can be found under [#functions](#functions)

## Functions:

## How is an animation defined?

Broken down to it's most basic structure, an animation class compatible with this animator needs two functions:

* animateFrame
* reset

Now let's look at how these two functions are implemented:

### animateFrame():

#### Arguments:

This function needs to accept only one argument: (data). This argument contains any data the animation might need in json format. The contents it will have depends on the needs of the animations in use.

Here is an example of how the data provided might look:
```
dataFile = {
        'speed': 20,
        'color': [255,255,255,1]
    }
```

#### Returned Values:

The animator class expects the returned value in the form of a list.
This list must contain the rgba values of all pixels along the strip.

Here is an example of how an animation would return a result of 3 pixels being red with full opacity:

```[[255,0,0,1],[255,0,0,1],[255,0,0,1]]```

As you can see, the animation function should return a list with lists of the pixel values. The pixel values within must be ordered like this: `[red,green,blue,alpha]`


### reset():

Reset kind of speaks for itself. This function will reset the internal state of the animation. What this means will be different for every animation.

import time, sys

from animations.colorBubbles import ColorBubbles
from animations.colorWipe import ColorWipe
from animations.fadeColor import FadeColor

class Animator:

    def __init__(self, data, config):

        requiredConfigsList = ['numPixels', 'frameRate']
        
        for x in requiredConfigsList:
            if x not in config.keys():
                raise RuntimeError(f'{x} not present in config. This value must be provided')
        
        self.numPixels = config['numPixels']
        self.frameRate = config['frameRate']
        self.delay_seconds = 1/self.frameRate # 1 split by frames per second
        self.frameStart = None

        if 'injectedFunctions' in config.keys():
            for k,v in config['injectedFunctions'].items():
                setattr(self, k, v.__get__(self))

        self.prevFrame = [] # Is populated during reset

        self.data = data

        self.animations = {}

        self.reset()

#region configuration:

    def importAnimation(self, animation, desiredName):
        self.animations[desiredName] = animation(numPixels=self.numPixels,animator=self)

#endregion configuration:

#region Pixel processing:

    def color(self, animation):
        frame = animation.animateFrame(self.data)
        if not frame:
            return False
        computedValues = []
        for pixel in frame:
            if pixel[0] > 255 or pixel[1] > 255 or pixel[2] > 255:
                raise RuntimeError(f'Color value {pixel} is out of range')
            elif pixel[3] > 1:
                raise RuntimeError(f'Alpha value {pixel} is out of range')
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            a = pixel[3]
            computedValues.append([round(r*a),round(g*a),round(b*a)])

        return computedValues
    
    def brightnessMask(self, animation):
        print("This function is not yet implemented")
    
    def shaderMask(self, animation):
        print("This function is not yet implemented")

    def processFrame(self, color=[], brightnessMask=[], shaderMask=[]):
        frameValues = {
            'color': [],
            'brightnessMask': [],
            'shaderMask': []
        }
        returnValues = []
        for x in color:
            frameValue = self.color(self.animations[x])
            if frameValue:
                frameValues['color'] = frameValue
            else:
                print(f'last frame reached by {x}')
                return False
        
        for x in frameValues['color']:
            returnValues.append(x)

        self.prevFrame = returnValues

        return returnValues
    
#endregion

#region Timing functions:

    def startFrame(self):
        self.frameStart = time.time()

    def waitForNextFrame(self, startNext=False):

        if not self.frameStart:
            self.startFrame(self)

        if self.delay_seconds - (time.time() - self.frameStart) > 0: # Wait for next frame
            time.sleep(max(self.delay_seconds - (time.time() - self.frameStart), 0))
        else:
            print('Not able to keep up with framerate! Consider lowering framerate')

        if startNext:
            self.startFrame(self)

#endregion

#region Reset functions:

    def reset(self):
        for _ in range(self.numPixels):
            self.prevFrame.append([0,0,0,0])

    def resetAnimations(self, all=False, animations=[]):
        if all:
            for animation in self.animations.values():
                animation.reset()

        elif animations:
            for animation in animations:
                if animation in self.animations.keys():
                    self.animations[animation].reset()

    def resetAll(self):
        self.resetAnimations(all=True)
        self.reset()

#endregion
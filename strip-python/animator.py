import time

from animations.colorBubbles import ColorBubbles
from animations.colorWipe import ColorWipe
from animations.fadeColor import FadeColor

class Animator:

    def __init__(self, data=None, config=None):

        requiredConfigsList = ['numPixels', 'frameRate', 'animateFunction']

        if config is None:
            raise RuntimeError('No config provided. Config is required')
        
        for x in requiredConfigsList:
            if x not in config.keys():
                raise RuntimeError(f'{x} not present in config. This value must be provided')
        
        self.numPixels = config['numPixels']
        self.frameRate = config['frameRate']
        self.delay_seconds = 1/self.frameRate # 1 split by frames per second
        self.frameStart = None

        self.injected = {
            'animate': config['animateFunction']
        }

        self.prevFrame = [] # Is populated during reset

        self.data = data

        self.animations = {
            'colorWipe': ColorWipe({'numPixels': self.numPixels}),
            'fadeColor': FadeColor({'numPixels': self.numPixels})
        }

        self.reset()

#region injectedWrappers

    def animate(self): # Wrapper for injected function
        self.injected['animate'](self)

#endregion

#region Pixel processing:

    def color(self, animation):
        frame = animation.animateFrame(self.data)
        if not frame:
            return False
        computedValues = []
        for pixel in frame:
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

if __name__ == '__main__': # Usage example

    dataFile = {
        'speed': 20,
        'color': [255,255,255,1]
    }

    def animateFunction(self):
        while True:
            self.startFrame()
            print(self.prevFrame)
            frame = self.processFrame(color=['fadeColor'])
            if frame:
                print(frame)
            else:
                print(frame)
                break
            self.waitForNextFrame()

        self.resetAnimations(all=True)

        print('Test Done...')

    configFile = {
        'numPixels': 10,
        'frameRate': 60,
        'animateFunction': animateFunction
    }

    # print("Running test...")
    # animator = Animator(data=dataFile, config=configFile)
    # while True:
    #     animator.startFrame()
    #     print(animator.prevFrame)
    #     frame = animator.processFrame(color=['fadeColor'])
    #     if frame:
    #         print(frame)
    #     else:
    #         print(frame)
    #         break
    #     animator.waitForNextFrame()

    # animator.resetAnimations(all=True)

    # print("Test Done...")

    animator = Animator(data=dataFile, config=configFile)

    animator.animate()
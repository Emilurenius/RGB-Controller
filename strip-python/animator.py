import time

from animations.colorBubbles import ColorBubbles
from animations.colorWipe import ColorWipe
from animations.fadeColor import FadeColor

class Animator:

    def __init__(self, numPixels, frameRate=60, data=None):

        self.numPixels = numPixels
        self.frameRate = frameRate
        self.delay_seconds = 1/self.frameRate # 1 split by frames per second
        self.frameStart = None

        self.prevFrame = [] # Is populated during reset

        self.data = data

        self.animations = {
            'colorWipe': ColorWipe({'numPixels': numPixels}),
            'fadeColor': FadeColor({'numPixels': numPixels})
        }

        self.reset()

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


if __name__ == '__main__': # Usage example

    dataFile = {
        'speed': 20,
        'color': [255,255,255,1]
    }

    print("Running test...")
    animator = Animator(numPixels=1, frameRate=1, data=dataFile)
    while True:
        animator.startFrame()
        print(animator.prevFrame)
        frame = animator.processFrame(color=['fadeColor'])
        if frame:
            print(frame)
        else:
            print(frame)
            break
        animator.waitForNextFrame()

    animator.resetAnimations(all=True)

    print("Test Done...")
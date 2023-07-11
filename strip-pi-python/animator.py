import time

from animations.colorBubbles import ColorBubbles
from animations.colorWipe import ColorWipe

class Animator:

    def __init__(self, numPixels, frameRate=60, data=None):

        self.numPixels = numPixels
        self.frameRate = frameRate
        self.delay_seconds = 1/self.frameRate # 1 split by frames per second
        self.frameStart = None

        self.data = data

        self.animations = {
            'colorWipe': ColorWipe({'numPixels': numPixels}),
            'colorBubbles': ColorBubbles({'numPixels': numPixels})
        }

    def color(self, animation):
        return animation.animateFrame(self.data)
    
    def brightnessMask(self, animation):
        print("This function is not yet implemented")
    
    def shaderMask(self, animation):
        print("This function is not yet implemented")

    def startFrame(self):
        self.frameStart = time.time()

    def waitForNextFrame(self, startNext=False):

        if not self.frameStart:
            self.startFrame(self)

        if time.time() - self.frameStart < self.delay_seconds: # Wait for next frame
            time.sleep(self.delay_seconds - (time.time() - self.frameStart))
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

        return returnValues
    
if __name__ == '__main__':

    dataFile = {
        'speed': 200
    }

    print("Running test...")
    animator = Animator(numPixels=10, frameRate=30, data=dataFile)
    while True:
        animator.startFrame()
        frame = animator.processFrame(color=['colorWipe'])
        print(frame)
        if frame:
            print(frame)
        else:
            break
        animator.waitForNextFrame()

    print("Test Done...")
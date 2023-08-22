from animator import Animator
from animations.fadeColor import FadeColor

dataFile = {
    'speed': 20,
    'color': [255,255,255,1]
}

def animateFunction(self, **kwargs):
    while True:
        self.startFrame()
        #print(self.prevFrame)
        frame = self.processFrame(color=kwargs['color'])
        if frame:
            #print(frame)
            pass
        else:
            #print(frame)
            break
        self.waitForNextFrame()

    self.resetAnimations(all=True)

    print('Test Done...')

configFile = {
    'numPixels': 1,
    'frameRate': 30,
    'injectedFunctions': {
        'animate': animateFunction
    }
}

animator = Animator(data=dataFile, config=configFile)

animator.importAnimation(FadeColor)

animator.data['color'] = [255,0,0,1]
animator.animate(color=['fadeColor'])
animator.data['color'] = [0,255,0,1]
animator.setBaseValues('current')
print('baseColor:', animator.baseValues)
animator.animate(color=['fadeColor'])
animator.data['color'] = [0,0,255,1]
animator.setBaseValues('current')
animator.animate(color=['fadeColor'])
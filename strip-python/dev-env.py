from animator import Animator

dataFile = {
    'speed': 20,
    'color': [255,255,255,1]
}

def animateFunction(self, **kwargs):
    while True:
        self.startFrame()
        print(self.prevFrame)
        frame = self.processFrame(color=kwargs['color'])
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
    'injectedFunctions': {
        'animate': animateFunction
    }
}

animator = Animator(data=dataFile, config=configFile)

animator.data['color'] = [255,0,0,0.5]
animator.animate(color=['fadeColor'])
animator.data['color'] = [0,255,0,0.5]
animator.animate(color=['fadeColor'])
animator.data['color'] = [0,0,255,0.5]
animator.animate(color=['fadeColor'])
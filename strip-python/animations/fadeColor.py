import time

class FadeColor:

    def __init__(self, **kwargs):
        self.name='fadeColor'
        self.numPixels = kwargs['numPixels']
        self.color = [255,255,255,1]
        self.pixelData = 0
        self.lastFrame = None
        self.doneFlag = False
        self.reset()

    def animateFrame(self, data):

        if self.doneFlag:
            self.reset()
            return False

        if 'color' in data.keys():
            if len(data['color']) == 4:
                self.color = data['color']
            else:
                raise ValueError(f'Missing value for <color>!\nExpected format: [r,g,b,a]\nValues given: {data["color"]}')
        else:
            raise RuntimeError(f'Color values missing!\nExpected list with [r,g,b,a] values')
        
        if 'speed' in data.keys():
            if self.lastFrame:
                speed = (data['speed']*100) * (time.time() - self.lastFrame)
            else:
                speed = 0
        else:
            raise ValueError(f'Speed setting missing from data file!')
        
        self.pixelData += speed

        if self.pixelData >= 1000:
            self.pixelData = 1000
            self.doneFlag = True
        
        r,g,b,a = self.color

        returnVal = []

        for _ in range(self.numPixels):
            if a > 0:
                returnVal.append([r,g,b,(self.pixelData/1000)*a])
            else:
                returnVal.append([r,g,b,a])

        self.lastFrame = time.time()

        return returnVal
        
    def reset(self):
        
        self.lastFrame = None
        self.doneFlag = False
        self.pixelData = 0
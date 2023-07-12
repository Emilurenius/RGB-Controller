import time

class FadeColor:

    def __init__(self, args):
        self.numPixels = args['numPixels']
        self.color = [255,255,255,1]
        self.pixelData = 0
        self.lastFrame = None
        self.reset()

    def animateFrame(self, data):

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
        
        r,g,b,a = self.color

        

        return self.pixelData
        self.lastFrame = time.time()
        

    def reset(self):
        
        self.lastFrame = None
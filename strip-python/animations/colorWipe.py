import time

# def map(x,inputRangeStart,inputRangeEnd,outputRangeStart,outputRangeEnd):
#    output=(x-inputRangeStart)/(inputRangeEnd-inputRangeStart)*(outputRangeEnd-outputRangeStart)+outputRangeStart
#    return output

class ColorWipe:

    def __init__(self, args):

        self.numPixels = args['numPixels']

        # if 'color' in args.keys():
        #     if len(args['color']) == 4:
        #         self.color = args['color']
        #     raise ValueError(f'Missing value for arg <color>!\nExpected format: [r,g,b,a]\nValues given: {args["color"]}')
        # else:
        self.color = [255,255,255,1]

        self.pixelData = {}

        self.lastFrame = None

        self.reset()

    def animateFrame(self, data):

        if not data:
            raise RuntimeError('Data file must be provided for this animation!')

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
        
        noneActive = True
        for i in range(self.numPixels):
            if self.pixelData[i]["active"] == True:
                noneActive = False
                break
        if noneActive:
            self.pixelData[0]["active"] = True

        for i in range(len(self.pixelData)):
            # Fade up
            if self.pixelData[i]["active"] == True and self.pixelData[i]['val'] < 1000:
                self.pixelData[i]["val"] += speed
                if self.pixelData[i]["val"] >= 1000:
                    if i+1 < self.numPixels:
                        self.pixelData[i+1]['active'] = True
                    else:
                        return False # Tells animator that the animation has ended
                    self.pixelData[i]["val"] = 1000

        rgbList = []
        for i in range(len(self.pixelData)):
            alpha = (self.pixelData[i]['val']/1000)*self.color[3]
            rgbList.append([self.color[0],self.color[1],self.color[2],alpha])
        self.lastFrame = time.time()
        return rgbList
    
    def reset(self):
        for i in range(self.numPixels):
            self.pixelData[i] = {
                'val': 0,
                'active': False
            }

        self.lastFrame = None

if __name__ == '__main__':
    print("This is a module, and is not meant to be used directly!")
    print("Animation output with following settings:")
    print("{'numPixels': 10, 'speed': 500}")
    print('\n')
    time.sleep(1)
    colorWipe = ColorWipe({'numPixels': 10, 'speed': 500})

    while True:
        colorData = colorWipe.animateFrame()
        print(colorData)
        if not colorData:
            break
        time.sleep(0.017)
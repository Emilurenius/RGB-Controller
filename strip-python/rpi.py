from animator import Animator

from rpi_ws281x import PixelStrip, Color

if __name__ == '__main__': # Own testing

    #region Configuration for rpi_ws281x:
    LED_COUNT      = 10      # Number of LED pixels.
    LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
    #LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
    LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
    #endregion

    # strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # def animate(self, strip, color=[], brightnessMask=[], shaderMask=[]):

    #     while True:
    #         self.startFrame()
    #         frame = self.processFrame(color=color, brightnessMask=brightnessMask, shaderMask=shaderMask)
    #         if frame:
    #             for i in range(self.numPixels):
    #                 strip.setPixelColor(i, Color(frame[i][0],frame[i][1],frame[i][2]))
    #             strip.show()
    #         else:
    #             print('animating shit')
    #             break
    #         self.waitForNextFrame()

    # dataFile = {
    #     'speed': 20,
    #     'color': [255,255,255,1]
    # }
    
    # configFile = {
    #     'numPixels': LED_COUNT,
    #     'frameRate': 60,
    #     'injectedFunctions': {
    #         'animate': animate
    #     }
    # }

    # animator = Animator(data=dataFile, config=configFile)

    # animator.animate(strip=strip, color=['fadeColor'])
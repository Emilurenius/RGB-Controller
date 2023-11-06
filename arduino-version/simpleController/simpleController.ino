#include <Adafruit_NeoPixel.h>

#define PIN_NEO_PIXEL 16  // The ESP32 pin GPIO16 connected to NeoPixel
#define NUM_PIXELS 10     // The number of LEDs (pixels) on NeoPixel LED strip

Adafruit_NeoPixel neopixel(NUM_PIXELS, PIN_NEO_PIXEL, NEO_GRB + NEO_KHZ800);

struct RGB {
  int red = 0;
  int green = 0;
  int blue = 0;
};

class LedStrip {
  public:
    RGB stripColor[NUM_PIXELS];

    void show() {
      for (int pixel = 0; pixel < NUM_PIXELS; ++pixel) {
        int color = neopixel.Color(stripColor[pixel].red, stripColor[pixel].green, stripColor[pixel].blue);
        neopixel.setPixelColor(pixel, color);
      }
    }

    void clearStrip() {
      for (int pixel = 0; pixel < NUM_PIXELS; pixel++) {
        stripColor[pixel].red = 0;
        stripColor[pixel].green = 0;
        stripColor[pixel].blue = 0;
      }
    }

    void setColor(int r, int g, int b) {
      for (int pixel = 0; pixel < NUM_PIXELS; pixel++) {
        stripColor[pixel].red = r;
        stripColor[pixel].green = g;
        stripColor[pixel].blue = b;
      }
    }
};

LedStrip ledStrip;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  neopixel.begin();
  neopixel.clear();
}

void loop() {
  // put your main code here, to run repeatedly:
  ledStrip.clearStrip();
  ledStrip.show();
  delay(500);
  ledStrip.setColor(255,0,0);
  ledStrip.show();
  delay(500);
  ledStrip.setColor(0,255,0);
  ledStrip.show();
  delay(500);
  ledStrip.setColor(0,0,255);
  ledStrip.show();
  delay(500);
}

void setColor(RGB rgb) {
  for (int pixel = 0; pixel < NUM_PIXELS; ++pixel) {
    neopixel.setPixelColor(pixel, neopixel.Color(rgb.red, rgb.green, rgb.blue));
  }
  neopixel.show();
}
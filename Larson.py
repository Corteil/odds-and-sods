import piconzero as pz, time

pz.init()
pz.setOutputConfig(5, 3)    # set output 5 to WS2812
pz.setBrightness(15)

delay = 0.1
colour = [0,255,125] # colour format of LEDs 0 to 7 is G R B

# Set rear light to Red
for posistion in range(4, 8, 1):
    pz.setPixel(posistion, 0, 255, 0)

try:
    while True:
        for posistion in range(0,4,1):
            pz.setPixel(posistion, colour[0], colour[1], colour[2])
            time.sleep(delay)
            for off in range(0, 4, 1):
                pz.setPixel(off, 0,0,0)
            time.sleep(delay)
        for posistion in range(2, 0, -1):
            pz.setPixel(posistion, colour[0], colour[1], colour[2])
            time.sleep(delay)
            for off in range(0, 4, 1):
                pz.setPixel(off, 0, 0, 0)
            time.sleep(delay)
except KeyboardInterrupt:
    print ('finished')
finally:
    pz.cleanup()







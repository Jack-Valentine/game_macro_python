import os
import os.path
import mss
import time
try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

def on_exists(fname):
    # type: (str) -> None
    """
    Callback example when we try to overwrite an existing screenshot.
    """

    if os.path.isfile(fname):
        newfile = fname + '.old'
        print('{0} -> {1}'.format(fname, newfile))
        os.rename(fname, newfile)

with mss.mss() as sct:
    #filename = sct.shot(output='mon-{mon}.png', callback=on_exists)
    #print(filename)
    #import mss
    # -249, 1285
    import mss.tools

    with mss.mss() as sct:
        monitor = {'top': 1268, 'left': -324, 'width': 133, 'height': 33}
        output = 'sct-{top}x{left}_{width}x{height}.png'.format(**monitor)

        # Grab the data
        sct_img = sct.grab(monitor)

        # Save to the picture file
        mss.tools.to_png(sct_img.rgb, sct_img.size, output)
        time.sleep(3)
        #print (os.path.join("D:", "revolution_macro", "healthcheck", output))
        #print(pytesseract.image_to_string(Image.open(os.path.join("D:", "revolution_macro", "healthcheck", output))))
        tessdata_dir_config = '--tessdata-dir "D:\\revolution_macro\\healthcheck"'
        print(pytesseract.image_to_string(Image.open('sct-1268x-324_133x33.png'), lang='kor', config=tessdata_dir_config))






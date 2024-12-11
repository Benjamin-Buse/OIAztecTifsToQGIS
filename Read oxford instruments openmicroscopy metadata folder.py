import tkinter
import tkinter.filedialog
from PIL import Image
import xmltodict
import os
from os import listdir

folder_dir = tkinter.filedialog.askdirectory(title="Select directory of SEM tiles unstitched")
UserPaste = ""
for images in os.listdir(folder_dir):
 
    # check if the image ends with png
    if (images.endswith(".tif")):
        print(images)
        img = folder_dir+'/'+images

        #img = tkinter.filedialog.askopenfile(title="Select Aztec tif Image")
        im = Image.open(img)
        #for t in im.tag.keys():
        #    print (t, im.tag[t])
        imdescrdict=xmltodict.parse(im.tag[270][0])
        imdict2=imdescrdict["Image"]
        print(imdict2["PixelWidth_um"])
        (float(imdict2["ImageHeight_um"])-(887/1290)*float(imdict2["ImageWidth_um"])/2)/1000
        if UserPaste == "":
            UserPaste=tkinter.simpledialog.askstring("enter data","paste image details")
            UserPasteList=UserPaste.split('\n')
        #[s fo s in UserPasteList if "Stage X" in s]
        StageX = str([s for s in UserPasteList if "Stage X" in s]).split('\\t')[1].split("'")[0].split('mm')[0]
        StageY = str([s for s in UserPasteList if "Stage Y" in s]).split('\\t')[1].split("'")[0].split('mm')[0]
        TLy = float(StageY)+((float(imdict2["ImageHeight_um"])-(887/1290)*float(imdict2["ImageWidth_um"])/2)/1000)
        TLx = float(StageX)-((float(imdict2["ImageWidth_um"])/2)/1000)
        f = open(img.split(".tif")[0]+".tfw", "w")
        #if PixelWidth==PixelHeight:
        #    print("Pixel sizes xy match")
        #else:
        #    print("Pixel sizes xy do not match")
        PixelWidth=float(imdict2["PixelWidth_um"])/1000
        f.write(str(PixelWidth))
        f.write("\n")
        f.write("0")
        f.write("\n")
        f.write("0")
        f.write("\n")
        lineA="-"+str(PixelWidth)
        f.write(lineA)
        f.write("\n")
        f.write(str(TLx))
        f.write("\n")
        f.write(str(TLy))
        f.close()

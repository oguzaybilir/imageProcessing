import numpy as np  #gerekli kütüphaneleri import ettik
import imutils
import cv2

class Stitcher:     #Stitcher classını oluşturduk
    def __init__(self): 
        self.isv3  = imutils.is_cv3(or_better=True) #kullandığımız opencv sürümünü kontrol ediyoruz, çünkü sürümden sürüme fark ediyor

    def stitch(self,images,ratio=0.75,reprojThresh=4.0,showMatches=False):  # iki görsel arasındaki ortak noktaları bulan fonksiyonumuzu yazıyoruz
        (imageA,imageB) = images
        (kpsA,featuresA) = self.detectAndDescribe(imageA)   #   A görselinin kilit noktalarını ve özelliklerini bulduruyoruz
        (kpsB,featuresB) = self.detectAndDescribe(imageB)   #   B görselinin kilit noktalarını ve özelliklerini bulduruyoruz

        M = self.matchKeyPoints(kpsA,kpsB,featuresA,featuresB,ratio,reprojThresh)   #   2 görsel arasındaki anahtar noktalar ve özellikleri eşleştiriyoruz

        if M is None:   #   Eğer bir eşleşme olmazsa None döndürüyoruz
            return None

        (matches, H, status) = M
        result = cv2.warpPerspective(imageA,H,(imageA.shape[1]+imageB.shape[1], imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        if showMatches:
            vis = self.drawMatches(imageA, imageB, kpsA, kpsB, matches, status)

            return (result,vis)

        return result
from gbdxtools.catalog import Catalog
from gbdxtools.images.catalog_image import CatalogImage
import time

#Enter catalog id of image
imageId = "104001005C434C00"

#Enter polygon coordinates of AOI
crop = "POLYGON((56.335213571289046 25.217757840251576,56.335385232666 25.176906771954453,56.36611261914061 25.17628535715365,56.36559763500975 25.21806844224977,56.335213571289046 25.217757840251576))"

print(time.strftime("%H:%M:%S") + "\n")  # displays start time
print((Catalog().get_strip_metadata(imageId)))

#c = CatalogImage(imageId, product="ortho", pansharpen=True, acomp=True)
c = CatalogImage(imageId, pansharpen=True, acomp=True)
aoi = c.aoi(wkt=crop)
image = aoi.geotiff(path="C:\\Users\\vpadmin.VIDEOINFORM\\PycharmProjects\\gbdx\\Images\\No Product ortho\\104001003EA0F000_Fujairah_OilTanks_RDA.tif")
aoi.plot()

print("\n" + (time.strftime("%H:%M:%S")))  # displays end time

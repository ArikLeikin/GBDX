from gbdxtools.catalog import Catalog
from gbdxtools.images.catalog_image import CatalogImage

imageId = "104001001BA7C400"
crop = "POLYGON ((2.273792652835591 48.87926313360808,2.2741359755894974 48.859841811415095,2.3157119750976562 48.85534106071708,2.3096698806187943 48.87553753410312,2.273792652835591 48.87926313360808))"

print(Catalog().get_strip_metadata(imageId))

c = CatalogImage(imageId, product="ortho", pansharpen=True, acomp=True)
aoi = c.aoi(wkt=crop)
image = aoi.geotiff(path="output.tif")
aoi.plot()
def ndvi(raster):
    nir = raster["near-infrared"]
    grn = raster["green"]
    numerator = nir - grn
    denominator = nir + grn
    ndvi = numerator / denominator
    return(ndvi)
import shapefile as shp
import pandas as pd
from osgeo import osr

class Shapefile:
  """
  """
  def __init__(self, filepath):
    """
    Args:
      filepath: The directory path of a shapefile
    """
    self.filepath = filepath
    self.shape = None
    self.records = None
    self.bbox = None

    try:
      self.shape = shp.Reader(self.filepath)
      self.records = self.shape.records()

    except ValueError:
      print("Connot open shapefile!!!")

def getFeaturesBBOX(shpObj, attr):
  """
  Args:
    attr: The attribute to use from shapefile table
  """
  shpObj.bbox = pd.DataFrame(index=range(len(shpObj.records)), columns=[attr, 'xmin', 'ymin','xmax', 'ymax'])

  features = shpObj.shape.shapes()

  for i in range(len(shpObj.records)):
    shpObj.bbox['ottocod'][i] = shpObj.records[i][0]
    shpObj.bbox['xmin'][i] = features[i].bbox[0]
    shpObj.bbox['ymin'][i] = features[i].bbox[1]
    shpObj.bbox['xmax'][i] = features[i].bbox[2]
    shpObj.bbox['ymax'][i] = features[i].bbox[3]

def polygonFromBBOX(bbox):
  """
  Args:
    bbox: 
  """
  pol = [[
    [bbox['xmin'].iloc()[0],bbox['ymin'].iloc()[0]],
    [bbox['xmin'].iloc()[0],bbox['ymax'].iloc()[0]],
    [bbox['xmax'].iloc()[0],bbox['ymax'].iloc()[0]],
    [bbox['xmax'].iloc()[0],bbox['ymin'].iloc()[0]],
    [bbox['xmin'].iloc()[0],bbox['ymin'].iloc()[0]]
  ]]

  return pol

def savePolygon2Shp(filename, pol, field, fieldvalue = None, epsg = 4326, fieldtype = 'C', shptype = 5):
  """
  Args:
    pol:
    epsg: 
  """
  w = shp.Writer(filename)
  w.shapeType = shptype
  w.field(field, fieldtype)
  w.poly(pol)

  w.record(fieldvalue)
  w.close()

  ## create ESRI prj-file
  sr = osr.SpatialReference()
  sr.ImportFromEPSG(epsg)
  sr.MorphToESRI()

  with open(filename.replace('.shp', '.prj'), 'w') as prj:
    prj.write(sr.ExportToWkt())
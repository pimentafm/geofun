import mappyfile as mf

class RasterMapfile:
    def __init__(self):
        self.mapfile = None
        self.m = """
MAP
    NAME "MapFileName"
    SIZE 800 650
    EXTENT BoundingBox
    
    WEB
        METADATA
        "wms_title" "MapFileName"
        "wms_enable_request" "GetCapabilities GetMap GetFeatureInfo"
        "wms_feature_info_mime_type" "text/html"
        "wms_include_items" "all"
    END
  
    LAYER
        NAME "LayerName"
        STATUS default
        TYPE raster
        DUMP true
        TOLERANCE 80
        DATA "LayerFilePath"

        CLASSITEM "[pixel]"
            CLASS
                NAME "Formações florestais"
                EXPRESSION ([pixel] == 1)
                STYLE
                    OPACITY 100
                    COLOR 0 64 0
                END
            END
            CLASS
                NAME "Formações savânicas"
                EXPRESSION ([pixel] == 2)
                STYLE
                    OPACITY 100
                    COLOR 119 166 5
                END
            END
            CLASS
                NAME "Formações campestres"
                EXPRESSION ([pixel] == 3)
                STYLE
                    OPACITY 100
                    COLOR 184 175 79
                END
            END
            CLASS
                NAME "Mosaico de agricultura ou pastagem"
                EXPRESSION ([pixel] == 4)
                STYLE
                    OPACITY 100
                    COLOR 246 230 219
                END
            END
            CLASS
                NAME "Agricultura de sequeiro"
                EXPRESSION ([pixel] == 5)
                STYLE
                    OPACITY 100
                    COLOR 255 202 255
                END
            END
            CLASS
                NAME "Agricultura irrigada"
                EXPRESSION ([pixel] == 6)
                STYLE
                    OPACITY 100
                    COLOR 255 66 249
                END
            END
            CLASS
                NAME "Pastagem"
                EXPRESSION ([pixel] == 7)
                STYLE
                    OPACITY 100
                    COLOR 244 242 134
                END
            END
            CLASS
                NAME "Corpos d'água"
                EXPRESSION ([pixel] == 8)
                STYLE
                    OPACITY 100
                    COLOR  0 0 255
                END
            END
            CLASS
                NAME "Área urbana/Construções rurais"
                EXPRESSION ([pixel] == 9)
                STYLE
                    OPACITY 100
                    COLOR 255 0 0
                END
            END
        END
    END
END
"""
    def genMapfile(self, mname = None, lname = None, lpath = None):
        """
            Args:
                mname:
                lname:
                lpath:
        """
        
        if(mname):
            self.m = self.m.replace('MapFileName', mname)
        if(lname):
            self.m = self.m.replace('LayerName', lname)

        self.mapfile = mf.loads(self.m)
    
        if(lpath):
            self.m = self.m.replace('LayerFilePath', lpath)

    def dump(self):
        """
            Dump the mapfile schema.
        """
        
        print(mf.dumps(self.mapfile, indent=1, spacer="\t"))

    def save(self, fpath):
        """
            Save mapfile docstring to a validated and formated mapfile format.
            Args:
                fname:
        """
        
        if(fpath):
            mf.save(self.mapfile, output_file=fpath)






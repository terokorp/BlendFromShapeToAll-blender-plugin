bl_info = {
    "name": "BlendFromShapeToAll",
    "description": "Does BlendFromShape to all blendshapes",
    "author": "Tero Korpela",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "Shape Key Specials",
    "wiki_url": "https://github.com/terokorp/BlendFromShapeToAll-blender-plugin/wiki",
    "tracker_url": "https://github.com/terokorp/BlendFromShapeToAll-blender-plugin/issues",
    "support": "COMMUNITY",
    "category": "Object",
}

from . import addon

def register():
    addon.register()

def unregister():
    addon.unregister()

if __name__ == "__main__":
    register()
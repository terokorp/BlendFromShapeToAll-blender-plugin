
import bpy
import os

class BlendFromShapeToAll(bpy.types.Operator):
    """BlendFromShapeToAll Script"""            # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.blend_from_shape_all"   # Unique identifier for buttons and menu items to reference.
    bl_label = "Blend from shape to all"        # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}           # Enable undo for the operator.

    def execute(self, context):                 # execute() is called when running the operator.
        if context.active_object.mode == 'EDIT':
            print ("Doing blending from shape to all")
            scene = context.scene
            obj = context.active_object
            print(obj)
            source = obj.active_shape_key.name
            startIndex = obj.active_shape_key_index
            print(startIndex)
            for index, sp in enumerate(obj.data.shape_keys.key_blocks):
                print ("Processing " + sp.name)
                if(index != 0):
                    obj.active_shape_key_index = index
                    bpy.ops.mesh.blend_from_shape(shape=source, blend=1, add=False)
            
            obj.active_shape_key_index = startIndex
        return {'FINISHED'}
    
def menu_func(self, context):
    self.layout.operator(BlendFromShapeToAll.bl_idname)
    
def register():
    print("Loading BlendFromShapeToAll")
    bpy.utils.register_class(BlendFromShapeToAll)
    bpy.types.MESH_MT_shape_key_context_menu.append(menu_func)

def unregister():
    print("Unloading BlendFromShapeToAll")
    bpy.utils.unregister_class(BlendFromShapeToAll)
    bpy.types.MESH_MT_shape_key_context_menu.remove(menu_func)

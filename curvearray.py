import bpy
from . import utilities


# CLS----------------------------------------------------
class AddCurveAOperator(bpy.types.Operator):
    bl_idname = "redtools.add_curve_array"
    bl_label = "Add Curve Array"
    bl_description = "Create array object, assign to curve"

    def execute(self, context):
        # Make curve array
        make_curve_array()
        return {'FINISHED'}

# FUNC----------------------------------------------------

def make_curve():
    curve = bpy.ops.curve.primitive_nurbs_path_add(enter_editmode=False, location=(2, 0, 0))
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)

    return bpy.context.active_object


def make_cube():
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(0, 0, 0))

    return bpy.context.active_object


def set_parent(a, b):
    a.parent = b


def make_curve_array():
    ob = bpy.context.active_object
    curve = make_curve()

    if (bpy.context.scene.BoolProps.curvearray_use_active == True):
        ob.location = (0, 0, 0)
    else:
        ob = make_cube()

    set_parent(curve, ob)
    utilities.set_smooth(ob)
    bpy.ops.object.modifier_add(type='ARRAY')
    bpy.context.object.modifiers["Array"].fit_type = 'FIT_CURVE'
    bpy.context.object.modifiers["Array"].use_merge_vertices = True
    bpy.ops.object.modifier_add(type='CURVE')
    bpy.context.object.modifiers["Curve"].object = curve
    bpy.context.object.modifiers["Array"].curve = curve

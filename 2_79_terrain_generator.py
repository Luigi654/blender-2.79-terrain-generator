bl_info = {
    "name": "Generate Terrain",
    "author": "notestr32/luigi654",
    "version": (1, 0),
    "blender": (2, 79, 0),
    "location": "Add > Mesh > Generate Terrain",
    "description": "Generates a terrain mesh with various options",
    "category": "Object",
}

import bpy
import random

class GenerateTerrainOperator(bpy.types.Operator):
    """Generates a terrain mesh"""
    bl_idname = "object.generate_terrain_operator"
    bl_label = "Generate Terrain"
    bl_options = {'REGISTER', 'UNDO'}

    grid_size = bpy.props.IntProperty(name="Grid Size", default=10, min=1, max=100)
    seed = bpy.props.IntProperty(name="Seed", default=0)
    flatness = bpy.props.FloatProperty(name="Flatness", default=0.5, min=0.0, max=1.0)
    plateau = bpy.props.FloatProperty(name="Plateau", default=0.0, min=0.0, max=1.0)
    mountain = bpy.props.FloatProperty(name="Mountain", default=0.0, min=0.0, max=1.0)
    valley = bpy.props.FloatProperty(name="Valley", default=0.0, min=0.0, max=1.0)
    ravine = bpy.props.FloatProperty(name="Ravine", default=0.0, min=0.0, max=1.0)
    ocean_enable = bpy.props.BoolProperty(name="Enable Oceans", default=False)
    ocean_magnitude = bpy.props.FloatProperty(name="Ocean Magnitude", default=0.1, min=0.0, max=1.0)
    ocean_diameter = bpy.props.FloatProperty(name="Ocean Diameter", default=0.2, min=0.0, max=1.0)
    smoothness = bpy.props.FloatProperty(name="Terrain smoothness", default=0.5, min=0.0, max=1.0)
    round_faces = bpy.props.BoolProperty(name="Round Faces", default=False)
    scale_x = bpy.props.FloatProperty(name="Scale X", default=1.0, min=0.001)
    scale_y = bpy.props.FloatProperty(name="Scale Y", default=1.0, min=0.001)
    scale_z = bpy.props.FloatProperty(name="Scale Z", default=1.0, min=0.001)

    def execute(self, context):
        bpy.ops.object.select_all(action='DESELECT')
        bpy.ops.object.select_by_type(type='MESH')
        bpy.ops.object.delete()

        random.seed(self.seed)

        bpy.ops.mesh.primitive_grid_add(x_subdivisions=self.grid_size, y_subdivisions=self.grid_size)
        obj = bpy.context.active_object

        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')

        vertices = obj.data.vertices
        for vertex in vertices:
            z_offset = random.uniform(-1, 1)

            # Marcar llanuras
            if random.random() < self.flatness:
                z_offset = 0

            # Marcar mesetas
            if random.random() < self.plateau:
                z_offset += random.uniform(0, 0.5)

            # Marcar montañas
            if random.random() < self.mountain:
                z_offset += random.uniform(0.5, 1)

            # Marcar valles
            if random.random() < self.valley:
                z_offset -= random.uniform(0, 0.5)

            # Marcar barrancos
            if random.random() < self.ravine:
                z_offset -= random.uniform(0.5, 1)

            # Generar océanos
            if self.ocean_enable:
                if random.random() < self.ocean_diameter:
                    z_offset -= random.uniform(0, self.ocean_magnitude)

            vertex.co.z += z_offset

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.vertices_smooth(factor=self.smoothness)
        if self.round_faces:
            bpy.ops.mesh.faces_shade_smooth()
        bpy.ops.object.mode_set(mode='OBJECT')

        obj.scale.x = self.scale_x
        obj.scale.y = self.scale_y
        obj.scale.z = self.scale_z

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(GenerateTerrainOperator.bl_idname)

def register():
    bpy.utils.register_class(GenerateTerrainOperator)
    bpy.types.INFO_MT_mesh_add.append(menu_func)

def unregister():
    bpy.utils.unregister_class(GenerateTerrainOperator)
    bpy.types.INFO_MT_mesh_add.remove(menu_func)

if __name__ == "__main__":
    register()

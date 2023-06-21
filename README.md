# blender-2.79-terrain-generator
blender 2.79 terrain generator addon

# Generate Terrain

Generates a terrain mesh with various options.

## Properties

- **Grid Size**: Integer. The size of the grid for generating the terrain. (Min: 1, Max: 100, Default: 10)
- **Seed**: Integer. The seed value for random generation. (Default: 0)
- **Flatness**: Float. Controls the generation of flat areas. (Min: 0.0, Max: 1.0, Default: 0.5)
- **Plateau**: Float. Controls the generation of plateaus. (Min: 0.0, Max: 1.0, Default: 0.0)
- **Mountain**: Float. Controls the generation of mountains. (Min: 0.0, Max: 1.0, Default: 0.0)
- **Valley**: Float. Controls the generation of valleys. (Min: 0.0, Max: 1.0, Default: 0.0)
- **Ravine**: Float. Controls the generation of ravines. (Min: 0.0, Max: 1.0, Default: 0.0)
- **Enable Oceans**: Boolean. Enables the generation of oceans. (Default: False)
- **Ocean Magnitude**: Float. Controls the magnitude of ocean depth. (Min: 0.0, Max: 1.0, Default: 0.1)
- **Ocean Diameter**: Float. Controls the probability of generating an ocean at each position. (Min: 0.0, Max: 1.0, Default: 0.2)
- **Terrain Smoothness**: Float. Controls the smoothness of the generated terrain. (Min: 0.0, Max: 1.0, Default: 0.5)
- **Round Faces**: Boolean. Determines whether to round the faces of the terrain mesh. (Default: False)
- **Scale X**: Float. The scale factor for the X-axis of the generated terrain. (Min: 0.001, Default: 1.0)
- **Scale Y**: Float. The scale factor for the Y-axis of the generated terrain. (Min: 0.001, Default: 1.0)
- **Scale Z**: Float. The scale factor for the Z-axis of the generated terrain. (Min: 0.001, Default: 1.0)

## Usage

1. In Blender, go to **Add > Mesh > Generate Terrain**.
2. Adjust the properties in the sidebar (press N to show/hide the sidebar).
3. Click the **Generate Terrain** button to generate the terrain mesh with the specified properties.

## Compatibility

- Blender: 2.79.0

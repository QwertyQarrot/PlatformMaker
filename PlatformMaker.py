import unreal
import sys
import random

Rotation = 0

MinRotation = int(sys.argv[1])
MaxRotation = int(sys.argv[2])

def RandomiseRotation(MinRot, MaxRot):
    return random.randint(MinRot, MaxRot)  # Corrected function call to pass MinRot and MaxRot

Rotation = RandomiseRotation(MinRotation, MaxRotation)

##print(Rotation)

# Define the function to spawn the blueprint actor
def spawn_blueprint_actor(blueprint_path, x, y, z):
    # Load the blueprint
    blueprint = unreal.EditorAssetLibrary.load_blueprint_class(blueprint_path)

    if blueprint:
        # Spawn the actor
        spawned_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(blueprint, unreal.Vector(x, y, z), unreal.Rotator(0, 0, 0 + Rotation))
        unreal.log_warning("Blueprint Actor spawned successfully.")
        return spawned_actor
    else:
        unreal.log_warning("Failed to load blueprint at path: {}".format(blueprint_path))
        return None

blueprint_path = "/Game/ViviChar/V3/Plane_Blueprint.Plane_Blueprint"

filename = r"F:\Documents (F)\Unreal Projects\Chaos_Car\Pythons\xyz.csv"
data_list = []
with open(filename, 'r') as file:
    for line in file:
        # Split the line by commas and remove leading/trailing whitespaces
        items = line.strip().split(',')
        data_list.extend(items)  # Append the individual coordinates to data_list

# Iterate over the list of coordinates and spawn cubes
for i in range(0, len(data_list), 3):
    x, y, z = data_list[i:i+3]  # Extract x, y, z coordinates
    spawned_actor = spawn_blueprint_actor(blueprint_path,float(x), float(y), float(z))  # Spawn cube at the coordinates

print("Number of cubes spawned:", len(data_list) // 3)
print(Rotation)
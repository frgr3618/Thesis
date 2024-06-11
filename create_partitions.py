import json
import os

with open("/proj/uppmax2020-2-2/frgr3618/partitions/6_partitions/sorted.json", "r", encoding='utf-8') as file:
    dataset = file.readlines()

partitions = {i: [] for i in range(1, 11)}

# Distribute lines into partitions
for index, line in enumerate(dataset):
    partition_index = (index % 11) + 1
    partitions[partition_index].append(line)

output_dir = "./partitions/6_partitions"

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)
for partition_index, lines in partitions.items():
    output_file = os.path.join(output_dir, f"partition_{partition_index}.json")
    with open(output_file, "w", encoding='utf-8') as file:
        file.writelines(lines)

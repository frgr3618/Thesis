import os

with open("/data/fragra/francesco/data/partitions/6_partitions/ordered_6_partition_dataset.txt", "r", encoding = "utf-8") as file:
    dataset = file.readlines()

partitions = {i: [] for i in range(1, 11)}
for index, line in enumerate(dataset):
    partition_index = (index % 10) + 1
    partitions[partition_index].append(line)

output_dir = "/data/fragra/francesco/data/partitions/6_partitions"
os.makedirs(output_dir, exist_ok=True)

for partition_index, lines in partitions.items():
    output_file = os.path.join(output_dir, f"partition_{partition_index}.txt")
    with open(output_file, "w", encoding = "utf-8") as file:
        file.writelines(lines)

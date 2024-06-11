import os
import shutil

partitions_dir = "/proj/uppmax2020-2-2/frgr3618/partitions/6_partitions"
fold_data_dir = "/proj/uppmax2020-2-2/frgr3618/partitions/6_partitions/folds"
os.makedirs(fold_data_dir, exist_ok=True)


for fold_index in range(10):
    fold_dir = os.path.join(fold_data_dir, f"{fold_index + 1}")
    os.makedirs(fold_dir, exist_ok=True)
    train_data = []
    for i in range(10):
        if i == fold_index:
            partition_file = os.path.join(partitions_dir, f"partition_{i + 1}.json")
            shutil.copy(partition_file, os.path.join(fold_dir, "validation.json"))
        else:
            partition_file = os.path.join(partitions_dir, f"partition_{i + 1}.json")
            with open(partition_file, "r") as f:
                train_data.extend(f.readlines())
    with open(os.path.join(fold_dir, "train.json"), "w") as f:
        f.writelines(train_data)

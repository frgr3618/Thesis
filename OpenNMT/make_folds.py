import os

partitions_dir = "/data/fragra/francesco/data/partitions/6_partitions"
fold_data_dir = "/data/fragra/francesco/data/folds/6_partitions"
os.makedirs(fold_data_dir, exist_ok=True)

for fold_index in range(10):
    train_partitions = []
    for i in range(1, 11):
        if i - 1 == fold_index:  # Skip the partition used for validation
            continue
        partition_file = os.path.join(partitions_dir, f"partition_{i}.txt")
        with open(partition_file, "r") as file:
            train_partitions.extend(file.readlines())

  
    validation_partition_file = os.path.join(partitions_dir, f"partition_{fold_index + 1}.txt")
    with open(validation_partition_file, "r") as file:
        validation_partition = file.readlines()

   
    fold_dir = os.path.join(fold_data_dir, f"{fold_index + 1}")
    os.makedirs(fold_dir, exist_ok=True)


    with open(os.path.join(fold_dir, "multi_train.src_rep"), "w") as file:
        for line in train_partitions:
                word, trans = line.strip().split("|")
                file.write(word + "\n")

    with open(os.path.join(fold_dir, "multi_train.tgt_rep"), "w") as file:
        for line in train_partitions:
            word, trans = line.strip().split("|")
            file.write(trans + "\n")

    with open(os.path.join(fold_dir, "multi_valid.src_rep"), "w") as file:
        for line in validation_partition:
            word, trans = line.strip().split("|")
            file.write(word + "\n")

    with open(os.path.join(fold_dir, "multi_valid.tgt_rep"), "w") as file:
        for line in validation_partition:
            word, trans = line.strip().split("|")
            file.write(trans + "\n")

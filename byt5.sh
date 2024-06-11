#!/bin/bash
#SBATCH -A uppmax2020-2-2
#SBATCH -M snowy
#SBATCH -J G2P
#SBATCH -t 08:00:00
#SBATCH --gres=gpu
#SBATCH -p node -n 1
#SBATCH --ntasks-per-node 1



for fold in {1..10}; do
    python "/proj/uppmax2020-2-2/frgr3618/NeMo/examples/tts/g2p/g2p_train_and_evaluate.py" \
    --config-path="/proj/uppmax2020-2-2/frgr3618/NeMo/examples/tts/g2p/conf" \
    --config-name="g2p_t5" \
    model.train_ds.manifest_filepath="/proj/uppmax2020-2-2/frgr3618/partitions/folds/${fold}/train.json" \
    model.validation_ds.manifest_filepath="/proj/uppmax2020-2-2/frgr3618/partitions/folds/${fold}/validation.json" \
    model.test_ds.manifest_filepath="/proj/uppmax2020-2-2/frgr3618/partitions/folds/${fold}/test.json" \
    trainer.devices=1 \
    do_training=True \
    do_testing=True
done

#!/bin/bash


for fold in {1..10}; do 
  python g2p_inference.py \
    pretrained_model="/proj/uppmax2020-2-2/frgr3618/NeMo/examples/tts/g2p/nemo_experiments/T5G2P/t5_base_whole/${fold}f/checkpoints/T5G2P.nemo" \
    manifest_filepath="/proj/uppmax2020-2-2/frgr3618/partitions/folds/${fold}/test.json"
    output_file="output_file.json" \
    batch_size=16 \
    num_workers=16 \
    pred_field=pred_text 
done

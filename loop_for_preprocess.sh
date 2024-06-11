#!/bin/sh
basename="multi"
basedir="/data/fragra/francesco/data"
datadir="${basedir}/folds/6_partitions"

for fold_index in {1..10}; do
    echo "Preprocessing fold ${fold_index}"
    onmt_preprocess --train_src "${datadir}/${fold_index}/${basename}_train.src_rep" \
                    --train_tgt "${datadir}/${fold_index}/${basename}_train.tgt_rep" \
                    --valid_src "${datadir}/${fold_index}/${basename}_valid.src_rep" \
                    --valid_tgt "${datadir}/${fold_index}/${basename}_valid.tgt_rep" \
                    --overwrite \
                    --save_data "${datadir}/${fold_index}/${basename}" \
                    --report_every 1000
done

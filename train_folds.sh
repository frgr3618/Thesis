#!/bin/bash
basename="multi"
emb=64
rnn_size=256
rnn_type=LSTM
batch_size=16
learning_rate=0.0002
dropout=0.025
valid_steps=1000
train_steps=10000
basedir="/data/fragra/francesco"
datadir="${basedir}/data/folds/6_partitions"

# Loop over folds
for fold in {1..10}; do
    exp="s2s_${emb}_${rnn_size}_${rnn_type}_bs_${batch_size}_fold${fold}"
    outdir="${basedir}/output/${exp}/shuf/6_partitions"
    statsdir="${basedir}/stats/${exp}/shuf/6_partitions"
    modeldir="${basedir}/models/${exp}/shuf/6_partitions"
    logdir="${basedir}/logs/${exp}/shuf/6_partitions"
    mkdir -p ${outdir}
    mkdir -p ${statsdir}
    mkdir -p ${modeldir}
    mkdir -p ${logdir}
    echo "Training fold ${fold}..."
    onmt_train --data ${datadir}/${fold}/${basename} --rnn_size ${rnn_size} --rnn_type ${rnn_type} --optim adam --learning_rate ${learning_rate} --batch_size ${batch_size} --layers 2 --dropout ${dropout} --word_vec_size ${emb} --valid_steps ${valid_steps} --train_steps ${train_steps} --save_model ${modeldir}/s2s_${emb}_${rnn_size}_${rnn_type} --world_size 1 --gpu_ranks 0 > ${logdir}/logfile.txt 2>&1

done

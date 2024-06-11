#!/bin/sh
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
outdir="${basedir}/output/shuf/6_partitions"
statsdir="${basedir}/stats/shuf/6_partitions"

for fold in {1..10}; do
    exp="s2s_${emb}_${rnn_size}_${rnn_type}_bs_${batch_size}_fold${fold}"
    modeldir="${basedir}/models/${exp}/shuf/6_partitions"
    model="${modeldir}/s2s_${emb}_${rnn_size}_${rnn_type}_step_10000.pt"
    outdir_fold="${outdir}/fold${fold}"
    statsdir_fold="${statsdir}/fold${fold}"
    mkdir -p ${outdir_fold}
    mkdir -p ${statsdir_fold}

    # Translate
    onmt_translate --model ${model} --src ${datadir}/${fold}/${basename}_test.src_rep --output ${outdir_fold}/${basename}_test.tgt_pred --gpu 1 --replace_unk

    # Compute error
    python compute_stats_and_list_errors.py ${datadir}/${fold}/${basename}_test.tgt_rep ${outdir_fold}/${basename}_test.tgt_pred > ${statsdir_fold}/${basename}_test.error
done

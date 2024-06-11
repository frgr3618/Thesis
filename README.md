The python and bash files in the home directory belong to the experiments with the NVIDIA'Nemo framework (the transformers ByT5 and T5_base and small), wheres the folder OpenNMT contains
python and bash files for the Lstm that was given to me by the company and developed with the OpenNMT framework.

The grapheme to phoneme experiments with the transformers take inspiration from the tutorial: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/g2p.html and the model and original code can be found at: https://github.com/NVIDIA/NeMo/tree/main/examples/tts/g2p.

Inference, training and configuration files were modified to my needs (such as training the folders in a loop without having to do it manually each time).

'do_training.sh' and 'do_inference.sh' are the training and testing loops to train and test the models with the different folds.
'g2p_t5.yaml' is the configuration file that specifies the parameters used (which is needed by the training and testing). In the configuration file, at line 12, one can specify the model that wants to use. These models can be found on Hugginface at this URL:https://huggingface.co/google-t5

Since the output of inference is a file with the predictions and gives only the PER, the files 'calculate_wer.py', and 'correct_words.py' are made by myself, together with create_partitions.py and k_fold.py. K_fold.py prepares the partitions in the right way to then train the models using k-fold cross validation.

Lastly, track_phonemes.py is used to make the quantitave analysis in support of the qualitative evaluation. It gives the phonemes with the highest error rates and gives the wrong replacements of the predictions. 

OPENNMT
This model starts with loop_for_preprocess.sh which creates a src and tgt vocabulary and tokenize the words the way it needs. Train_folds.sh and test.folds.sh do training and inference. In this model there is no configuration file and the params are directly in the training file. I changed a few things in 'compute_stats_and_list_errors.py' and added the option of printing correct words too (before it was only wrong ones) and also printing the number of correctly guessed words over the total amount. Make_partitions and make_folds do what as their equivalent for the transformers. First create 11 partitions, and then arrange the folds the needed way to train the models with kfold cross validation. 



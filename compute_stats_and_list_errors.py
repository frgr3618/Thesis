#!/usr/bin/env python

import re,sys
import subprocess
#import levenshtein
import Levenshtein
import numpy
import sys
import os

inptransfn = sys.argv[1]
outptransfn = sys.argv[2] # re.sub("\.txt",".pred_wc",inptransfn)

if re.search("wstress", inptransfn):
    stress_symbols = 1
else:
    stress_symbols = 0
inpwordfn = inptransfn.replace("tgt","src")

inptranslines = open(inptransfn).read().splitlines()
inpwordlines =  open(inpwordfn).read().splitlines()
predlines = open(outptransfn).read().splitlines()

# INITIALIZE STATS
total_words = 0
total_error = 0
total_phone_error = 0
total_stress_error = 0
total_phonemes = 0
total_str = 0
total_phn_str = 0
phoneme_errors = 0
symbol_errors = 0
phn_str_errors = 0
str_errors = 0
word_errors = 0

# Check to make sure the input and predicted files have the same number of lines
if not len(predlines) == len(inptranslines):
    sys.exit('Number of predictions and reference forms are different')

for (word, inptrans, predtrans) in zip(inpwordlines, inptranslines, predlines):
    inptrans = inptrans.strip()
    predtrans = predtrans.strip()
    word = re.sub(" ","", word)
    word = word.replace(">","> ")

    # Compute whether there is an error in the total transcription
    total_words += 1
    if not re.match(r"%s" % inptrans, r"%s" % predtrans):
    #    print "total_error:", inptrans, " | ", predtrans, len(inptrans), len(predtrans)
        total_error += 1  
        print(f"Error: {word} - Input: {inptrans}, Pred: {predtrans}")
    else:
        # Correctly guessed case: Print the correct word
        print(f"Correct: {word} - Input: {inptrans}, Pred: {predtrans}")

	# Phonemes only
    inp_ph = re.sub("[0123] ", " ", inptrans)
    inp_ph = re.sub("[0123]$", "", inp_ph)
    pred_ph = re.sub("[0123] "," ",predtrans)
    pred_ph = re.sub("[0123]$","",pred_ph)

    # When considering only phonemes (not stress, syll), compute whether there is an error
    if not re.match(r"%s" % inp_ph, r"%s" % pred_ph):
        #print("total_phone_error:", total_phone_error, inp_ph, " | ", pred_ph, len(inp_ph), len(pred_ph))
        total_phone_error += 1

    inp_ph = inp_ph.split(" ")
    #print(pred_ph)
    pred_ph = pred_ph.split(" ")
    total_phonemes += len(inp_ph)

    #phone_distance = levenshtein.levenshtein(inp_ph,pred_ph)
    phone_distance = Levenshtein.distance(" ".join(inp_ph)," ".join(pred_ph))
    phoneme_errors += phone_distance

    if phone_distance > 0:
        print( "Phoneme Error: %s, Test: %s, Pred: %s %d" % (word, inp_ph, pred_ph, phone_distance))

    phone_result = Levenshtein.editops("".join(inp_ph),"".join(pred_ph))
    #S Stress only
    search_term = "[0123][ $]"
    if re.search(search_term,inptrans):
        inp_stress = []
        pred_stress = []
        for el in inptrans.split(" "):
            if re.search("0",el):
                inp_stress.append("0")
            elif re.search("3",el):
                inp_stress.append("3")
            elif re.search("1",el):
                inp_stress.append("1")
            elif re.search("2",el):
                inp_stress.append("2")
        for el in predtrans.split(" "):
            if re.search("0",el):
                pred_stress.append("0")
            elif re.search("3",el):
                pred_stress.append("3")
            elif re.search("1",el):
                pred_stress.append("1")
            elif re.search("2",el):
                pred_stress.append("2")
        searchterm = re.compile(r'\b%s\b' % "".join(inp_stress))
        if not searchterm.search('%s' % "".join(pred_stress)):
            total_stress_error += 1
            print("Stress Error: Input: %s, Pred: %s %d" % (inptrans, predtrans, total_stress_error))

        str_distance = Levenshtein.distance(" ".join(inp_stress)," ".join(pred_stress))
        str_errors += str_distance
        total_str += max(len(inp_stress),len(pred_stress))


ph_acc = (1.0 - phoneme_errors/float(total_phonemes))
#print "Ave Phoneme accuracy: ", ph_acc, phoneme_errors, total_phonemes
#print "PER: %.2f" % ((float(phoneme_errors)/float(total_phonemes))*100.0)

if str_errors > 0:
    str_acc = (1.0 - str_errors/float(total_str))
    #print "Ave Stress accuracy: ", str_acc, str_errors, total_str
else:
	str_acc = 1.0
#phn_str_acc = (1.0 - phn_str_errors/float(total_phn_str))
#print "Ave Phoneme + stress accuracy: ", phn_str_acc, phn_str_errors, total_phn_str
w_acc = (1.0 - total_error/float(total_words))
#print "Ave Word accuracy: ", w_acc, total_error, total_words

wer_word = (float(total_error)/float(total_words))
wer_phones = float(total_phone_error)/float(total_words)
correctly_guessed_words = total_words - total_error


print(f"Correctly Guessed Words: {correctly_guessed_words}/{total_words}")
print(f"WER: {wer_word*100:.2f} PER: {(1-ph_acc)*100:.2f} WER stress: {(1-str_acc)*100:.2f}")
#print "WER: %.2f" % wer_word
#print "WER phonemes only: %.2f" % float(total_phone_error)/float(total_words), "Accuracy:", 1 - (float(total_phone_error)/float(total_words))
#if total_stress_error > 0:
#    print "WER stress: %.2f" % float(total_stress_error)/float(total_words), "Accuracy:", 1 - (float(total_stress_error)/float(total_words))

#print 
#junk, sys_id = os.path.split(outptransfn)
#results_line = ph_acc, syl_acc, str_acc, w_acc, wer_word,wer_phones,wer_stress
#results_line = ph_acc, str_acc, w_acc, wer_phones, wer_word
#results_line = ['%.2f'%(x*100) for x in results_line]
#results_line = [sys_id] + results_line
#results_line = '\t&\t'.join(results_line)  + ' \\\\'



#header_line = ['system', 'phon acc', 'syll acc', 'str acc', 'word acc', 'WER phon', 'WER stress', 'WER all']

#header_line = '\t&\t'.join(header_line)  + ' \\\\'

#print(header_line)
#print(results_line)

print(f"WER: {wer_word*100:.2f} PER: {(1-ph_acc)*100:.2f} WER stress: {(1-str_acc)*100:.2f}")


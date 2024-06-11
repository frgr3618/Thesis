import json
from collections import defaultdict


def read_data(file_path):
    with open(file_path, 'r') as file:
        data = [json.loads(line.strip()) for line in file]
    return data


def analyze_phoneme_errors(data, phonemes_to_track):
    phoneme_counts = defaultdict(int)
    phoneme_errors = defaultdict(int)
    phoneme_replacements = {phoneme: defaultdict(int) for phoneme in phonemes_to_track}
    for entry in data:
        gold_standard = entry["text"]
        prediction = entry["pred_text"]
        for gold_phoneme, pred_phoneme in zip(gold_standard, prediction):
            phoneme_counts[gold_phoneme] += 1
            if gold_phoneme != pred_phoneme:
                phoneme_errors[gold_phoneme] += 1
                if gold_phoneme in phonemes_to_track:
                    phoneme_replacements[gold_phoneme][pred_phoneme] += 1
    return phoneme_counts, phoneme_errors, phoneme_replacements


def print_results(phoneme_counts, phoneme_errors, phoneme_replacements):
    print("Phoneme Error Analysis:")
    for phoneme in sorted(phoneme_counts):
        total = phoneme_counts[phoneme]
        errors = phoneme_errors[phoneme]
        error_rate = (errors / total) * 100
        print(f"Phoneme: {phoneme}, Error_rate: {error_rate:.2f}%")
    print("\nPhoneme Replacements:")
    for phoneme, replacements in phoneme_replacements.items():
        print(f"\nPhoneme: {phoneme}")
        for replacement, count in replacements.items():
            print(f"  Replaced with: {replacement}, Count: {count}")


if __name__ == "__main__":
    file_path = '/proj/uppmax2020-2-2/frgr3618/partitions/folds/4/test_phonemes.json'
    phonemes_to_track = ['ɔ', 'ɛ', 'ŋ', 'ɡ', 'e', 'u', 'z', 'j', 'v', 'o'] #these are the phonemes with the highest error rate
    data = read_data(file_path)
    phoneme_counts, phoneme_errors, phoneme_replacements = analyze_phoneme_errors(data, phonemes_to_track)
    print_results(phoneme_counts, phoneme_errors, phoneme_replacements)

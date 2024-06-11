file_path = 'multi_test.error'

with open(file_path, 'r') as file:
    lines = file.readlines()
total_counts = {}
error_counts = {}
phoneme_replacements = {}

for line in lines:
    if "Test: " in line and "Pred: " in line:
        parts = line.split("Test: ")[1]
        test_phonemes = parts.split("], Pred: [")[0].strip("['").strip("']")
        pred_phonemes = parts.split("], Pred: [")[1].split("]")[0].strip("['").strip("']")
        test_phoneme_list = test_phonemes.split("', '")
        pred_phoneme_list = pred_phonemes.split("', '")
        for test, pred in zip(test_phoneme_list, pred_phoneme_list):
            if test in total_counts:
                total_counts[test] += 1
            else:
                total_counts[test] = 1
            if test != pred:
                if test in error_counts:
                    error_counts[test] += 1
                else:
                    error_counts[test] = 1
            if test != pred:
                if test in phoneme_replacements:
                    if pred in phoneme_replacements[test]:
                        phoneme_replacements[test][pred] += 1
                    else:
                        phoneme_replacements[test][pred] = 1
                else:
                    phoneme_replacements[test] = {pred: 1}


for phoneme in total_counts:
    total = total_counts[phoneme]
    errors = error_counts.get(phoneme, 0)
    error_rate = (errors / total) * 100
    print(f"Phoneme: {phoneme}, Error Rate: {error_rate:.2f}%")

print("\nPhoneme Replacements:")
for phoneme, replacements in phoneme_replacements.items():
    print(f"Phoneme: {phoneme}")
    for replacement, count in replacements.items():
        print(f"Replaced by: {replacement}, Count: {count}")



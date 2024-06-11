def count_correct_and_total_words_from_file(file_path):
    total_correct_words = 0
    total_words = 0
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                line_data = eval(line)
                original_text = line_data['text']
                predicted_text = line_data['pred_text']
                original_words = original_text.split()
                predicted_words = predicted_text.split()
                for original_word, predicted_word in zip(original_words, predicted_words):
                    if original_word == predicted_word:
                        total_correct_words += 1
                total_words += len(original_words)
    return total_correct_words, total_words

for fold in range (1,11):
    file_path = f'/proj/uppmax2020-2-2/frgr3618/partitions/6_partitions/folds/{fold}/test_phonemes.json'
    correct_words_count, total_words = count_correct_and_total_words_from_file(file_path)
    print("Number of correctly guessed words:", correct_words_count)

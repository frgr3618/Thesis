from evaluate import load

def read_texts_from_file(file_path):
    predictions = []
    references = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                line_data = eval(line)  
                predictions.append(line_data['pred_text'])
                references.append(line_data['text'])

    return predictions, references

for fold in range(1,11):
    file_path = f'/proj/uppmax2020-2-2/frgr3618/partitions/6_partitions/folds/{fold}/test_phonemes.json'
    predictions, references = read_texts_from_file(file_path)
    wer = load("wer")
    wer_score = wer.compute(predictions=predictions, references=references)
    print(wer_score)

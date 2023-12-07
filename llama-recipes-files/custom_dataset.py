import copy
import datasets
import itertools

import json
from transformers import AutoTokenizer

import random

TRAIN_SPLIT = 0.8

def get_custom_dataset(dataset_config, tokenizer, split):

    jsonl_path = '/home/talk-to-paul/llama-recipes/examples/15M.jsonl'
    print("[Dataset]: ", jsonl_path)

    with open(jsonl_path, 'r') as file:
        data = [json.loads(line) for line in file]

    # shuffle the data
    random.seed(0)
    random.shuffle(data)

    n = len(data)
    if split == 'train':
        data = data[:round(n * TRAIN_SPLIT)]
    else:
        data = data[round(n * TRAIN_SPLIT):]

    # Tokenize each dialogue in the dataset
    tokenized_data = []

    for record in data:

        input_ids, labels = [], []
        
        text = record['text']
        text = text.replace('<eot>', '').replace('<eop>', '')
        text_l = text.split('<eom>')[:-1] # nothing after the last <eom>

        for text in text_l:

            tokens = tokenizer.encode(f"{tokenizer.bos_token} {text.strip()} {tokenizer.eos_token}", add_special_tokens=False)
            input_ids += tokens
            labels += tokens
            # labels += tokens if 'Paul Christiano:' in text else [-100] * len(tokens)

        tokenized_data.append({
            "input_ids": input_ids,
            "labels": labels,
            "attention_mask": [1] * len(input_ids)
        })

    return tokenized_data

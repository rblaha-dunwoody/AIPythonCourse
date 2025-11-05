from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def preprocess_t5(examples):
    inputs = ["classify sentiment: " + doc for doc in examples["text"]]
    model_inputs = tokenizer(inputs, mex_length=128, truncation=True, padding="max_length")
    model_inputs["labels"] = tokenizer(examples["labels"], max_length=16, truncation=True, padding="max_length")["input_ids"]
    return model_inputs

tokenized_t5 = dataset.map(preprocess_t5, batched=True)
# Project: Fine-tune a pre-trained Transformer model (e.g., T5 or BART) for text summarization or translation and evaluate its performance
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, TrainingArguments, Trainer

# Load dataset for summarization
dataset = load_dataset("cnn_daily_mail", "3.0.0")
print(dataset["train"][0])

# For translation
#dataset = load_dataset("wmt14", "en-fr")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("t5-small")

# Tokenize for summarization
def tokenize(examples):
    inputs = ["summarize: "+ doc for doc in examples["articles"]]
    model_inputs = tokenizer(inputs, max_length=512, truncation=True)
    
    # Tokenize targets
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(examples["highlights"], max_length=150, truncation=True)
    
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized_datasets = dataset.map(tokenize_function, batched=True)

model = AutoModelForSeq2SeqLM.from_pretrained("t5-small")


training_args = TrainingArguments(
    output_dir="./results",
    eval_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2,
    predict_with_generate=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"],
    eval_dataset=tokenized_datasets["validation"],
    processing_class=tokenizer
)

trainer.train()

sample_text = "The Transformer model has revolutionized NPL by enabling parallel processing of sequences."
inputs = tokenizer("summarize: " + sample_text, return_tensors="pt", max_length=512, truncation=True)
outputs = model.generate(inputs["input_ids"], max_length=150, num_beams=4, early_stopping=True)

print("Generated Summary: ", tokenizer.decode(outputs[0], skip_special_tokens=True))

""" metric = load_metric("rouge") # sacrenleu
predictions = outputs["generated_text"]
references = dataset["validation"]["highlights"]

results = metric.compute(predictions=predictions, references=references)
print(results) """
import replicate

training = replicate.trainings.create(
  version="meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
  input={
    "train_data": "https://replicate.delivery/pbxt/Jt9Ilw49ID6vZaCmESBUfLATb78GohsveMNDjE6INDaLAHK1/data.jsonl",
    "num_train_epochs": 3
  },
  destination="mtrazzi/podcast-paul"
)

print(training)
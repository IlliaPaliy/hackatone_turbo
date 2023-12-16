from transformers import pipeline, set_seed
import random


def generate_history_question(model):
    # Створення підказки для генерації питання з історії України
    prompt = "Ask me question about biology"
    # Генеруємо питання використовуючи модель
    question = model(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']

    return question


# Ініціалізація моделі GPT
model = pipeline('text-generation', model='gpt2')
set_seed(42)  # Для відтворюваності результатів

# Генерація 50 питань
for _ in range(5):
    print(generate_history_question(model))
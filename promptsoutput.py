# Random prompt scripts against ollama llama3:latest & deepseek-r1 created by Rod Soto

import ollama
import json
import random
import time
from datetime import datetime

# Generate 100 random prompts
random_prompts = [
    "What is the meaning of life?",
    "Tell me a joke about AI.",
    "Explain quantum mechanics in simple terms.",
    "What's the capital of Japan?",
    "Who wrote '1984'?",
    "What are black holes?",
    "Give me 5 fun facts about space.",
    "How does the internet work?",
    "Summarize 'Pride and Prejudice' in one paragraph.",
    "Tell me a riddle.",
    "Describe a futuristic city in 2100.",
    "What are the benefits of meditation?",
    "Write a short story about a lost astronaut.",
    "How do self-driving cars work?",
    "Why is the sky blue?",
    "What is the Fibonacci sequence?",
    "Explain the Big Bang theory.",
    "What is machine learning?",
    "What are the effects of climate change?",
    "Tell me about the history of the Roman Empire.",
    "How do cryptocurrencies work?",
    "Explain relativity in simple words.",
    "Describe the process of photosynthesis.",
    "What is the difference between AI and human intelligence?",
    "Write a haiku about the ocean.",
    "Tell me a fun fact about dinosaurs.",
    "How does a neural network learn?",
    "What is dark matter?",
    "Give me a motivational quote.",
    "Describe an imaginary planet with unique life forms.",
]  # Expand this list to 100 prompts

# Shuffle and select 100 random prompts
random.shuffle(random_prompts)
selected_prompts = random_prompts[:100]

# Initialize data storage
results = []

# Model to use
model_name = "deepseek-r1"

# Loop through prompts and capture results
for i, prompt in enumerate(selected_prompts, start=1):
    start_time = time.time()  # Start execution time tracking
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Get response from Ollama
        response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
        response_text = response["message"]["content"]
    except Exception as e:
        response_text = f"Error: {str(e)}"

    end_time = time.time()  # End execution time tracking
    execution_time = round(end_time - start_time, 2)

    # Store result
    results.append({
        "timestamp": timestamp,
        "model": model_name,
        "prompt_number": i,
        "user_prompt": prompt,
        "generated_response": response_text,
        "execution_time_seconds": execution_time
    })

    print(f"Processed {i}/100 prompts...")

# Save results to a JSON file
output_filename = "ollama_results_deepseek_r1.json"
with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4, ensure_ascii=False)

print(f"✅ Completed! Results saved in {output_filename}")

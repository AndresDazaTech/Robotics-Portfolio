import ollama
import time

# 1. Define the models you have running locally
models = ['gemma3:latest', 'llama3.2:latest']

# 2. Define a prompt related to your robotics work
user_prompt = "Explain the importance of Pulse Width Modulation (PWM) in controlling a robot servo motor like the Picar X."

def query_model(model_name, prompt):
    print(f"\n--- 🤖 Asking {model_name} ---")
    start_time = time.time()
    
    try:
        # Call the local Ollama API
        response = ollama.chat(model=model_name, messages=[
            {
                'role': 'user',
                'content': prompt,
            },
        ])
        
        # Calculate inference time
        duration = time.time() - start_time
        content = response['message']['content']
        
        print(f"✅ Response received in {duration:.2f} seconds.")
        return content, duration
        
    except Exception as e:
        return f"Error: {str(e)}", 0

def main():
    print(f"Testing Local Models: {models}\n")
    results = {}

    # Loop through both models
    for model in models:
        answer, duration = query_model(model, user_prompt)
        results[model] = {
            "answer": answer,
            "time": duration
        }

    # Print a summary comparison
    print("\n" + "="*50)
    print("📝 MODEL COMPARISON SUMMARY")
    print("="*50)
    
    for model, data in results.items():
        print(f"\n🔹 Model: {model}")
        print(f"⏱️ Time taken: {data['time']:.2f}s")
        print(f"💬 Output Snippet: {data['answer'][:150]}...") # Print first 150 chars
        print("-" * 30)

if __name__ == "__main__":
    main()

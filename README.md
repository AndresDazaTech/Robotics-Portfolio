# Andres Daza ITAI 2374 

## 📄 Project 1: Picar X Robot - Assembly & Environment Setup
This project focuses on the initial hardware assembly, firmware configuration, and software environment setup for the SunFounder Picar X (v2.0). The goal was to establish a functional mobile robotics platform for future computer vision and autonomous driving tasks.

### 🔧 Hardware & Tools Used
*   **Robot Kit:** SunFounder Picar X (v2.0)
*   **Controller:** Raspberry Pi (3/4)
*   **OS:** Raspberry Pi OS (Legacy/Bullseye recommended for camera compatibility)
*   **Language:** Python 3

### 🚀 Implementation Steps
1.  **Assembly:** Constructed the chassis, servo motors, and camera module following the mechanical schematics.
2.  **Environment Configuration:**
    *   Enabled I2C, SPI, and Camera interfaces via `raspi-config`.
    *   Installed required dependencies (`ezblock` or `robot_hat` libraries).
3.  **Calibration:**
    *   Performed servo zeroing to ensure wheel alignment.
    *   Calibrated the grayscale sensor for line tracking capabilities.

### 📚 Resources & References
The setup process utilized the official documentation and community guides:
*   **Official Documentation:** [SunFounder Picar X v2.0 Docs](https://docs.sunfounder.com/projects/picar-x-v20/en/latest/index.html)
*   **Setup Tutorial Video:** [YouTube Walkthrough](https://www.youtube.com/watch?v=i5FpY3FAcyA)

### 📸 Results
*   Successfully established SSH connection to the robot.
*   Verified movement controls (forward, backward, steering).
*   Validated camera feed streaming.
*   ![My Picar X](IMG_6796.HEIC)


## Project 2: Final

### 📄 Local LLM Inference & Comparison
This project implements a local inference engine using **Ollama** to run Large Language Models (LLMs) offline. The goal was to benchmark different models to see which is most efficient for a robotics assistant (specifically for Picar X technical support).

### 🔍 The Experiment
I compared two state-of-the-art small language models:
1.  **Gemma 3** (Google)
2.  **Llama 3.2** (Meta)

The script sends a technical query ("Explain PWM for servo motors") to both models and measures:
*   Inference Latency (Time to generate response)
*   Response Quality

### 📂 Files
*   `compare_models.py`: The Python orchestration script.
*   `results.txt`: The raw output logs from the benchmark.

### 📊 Results & Analysis
Running on a MacBook Pro (Apple Silicon), the benchmark yielded significant differences:

| Model | Time (Seconds) | Observations |
| :--- | :--- | :--- |
| **Llama 3.2** | **12.59s** | **Winner.** Highly efficient and fast. Ideal for real-time robotics queries. |
| **Gemma 3** | 56.80s | Slower inference time, likely more computationally heavy for this specific hardware setup. |

### 🚀 Conclusion
For an offline robotics assistant running on this specific edge hardware, **Llama 3.2 is the superior choice** due to its 4.5x speed advantage while maintaining high accuracy on technical concepts.

### 💻 How to Run
1.  Install Ollama: `pip install ollama`
2.  Run script: `python compare_models.py`

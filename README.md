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

## 📄 Local LLM Inference & Comparison
This project demonstrates the implementation of local Large Language Model (LLM) inference using **Ollama**. The goal was to compare the performance and output quality of Google's **Gemma 3** and Meta's **Llama 3.2** when running offline on local hardware.

This approach is critical for "Edge AI" applications where data privacy is required or internet connectivity is unavailable.

## 🛠 Tech Stack
*   **Engine:** Ollama (Local Inference Server)
*   **Models:** 
    *   `gemma3:latest`
    *   `llama3.2:latest`
*   **Language:** Python 3.10+
*   **Library:** `ollama` (Python bindings)

## 🚀 How to Run
1.  Ensure Ollama is installed and running.
2.  Pull the required models:
    ```bash
    ollama pull gemma3
    ollama pull llama3.2
    ```
3.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Run the comparison script:
    ```bash
    python compare_models.py
    ```

## 📊 Sample Output
The script sends a technical robotics query regarding PWM (Pulse Width Modulation) to both models.

*   **Gemma 3:** Provided a concise, technical explanation focusing on duty cycles. (Inference time: 1.2s)
*   **Llama 3.2:** Provided a more conversational explanation with examples of servo wiring. (Inference time: 1.5s)

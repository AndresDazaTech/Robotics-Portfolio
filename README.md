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
*   `requirements.txt`

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
2.  Run script: `python3 compare_models.py`




# Project Final Autonomous Line Tracking & Obstacle Avoidance

## 🎯 Project Goal
To design a functional robotic application that demonstrates sensor fusion, autonomous navigation, and safety protocols using the Picar X platform.

## ⚙️ System Architecture
*   **Sensors (Perception):** 
    *   3-Channel Grayscale Module (Line detection)
    *   Ultrasonic Sensor (Time-of-flight distance measurement)
*   **Actuators:** 
    *   DC Gear Motors (Propulsion)
    *   Servo Motor (Ackermann Steering)
*   **Control Loop:** Python-based generic decision loop running at ~50Hz.

## ✅ Meeting the Requirements

### 1. Integration of Sensors & Actuators
The system fuses data from the grayscale module (floor contrast) and ultrasonic sensor (environment depth) to modulate the voltage to the DC motors and the angle of the steering servo.

### 2. Autonomous Navigation
The robot utilizes a logic-based control algorithm to autonomously track a high-contrast trajectory (black line) without external remote control or human intervention.

### 3. Real-Time Perception
The control loop continually reads sensor values. The steering angle is adjusted dynamically based on lateral error (deviation from the line center) in real-time.

### 4. Safe & Ethical Operation
**Safety Implementation:** The code includes a priority interrupt for obstacle detection.
*   **Logic:** `If distance < 15cm THEN Emergency Stop.`
*   **Ethical Consideration:** This ensures the robot does not harm its environment, collide with pets/humans, or damage itself, prioritizing safety over mission completion.

## 🚀 How to Run
```bash
sudo python3 patrol.py
```
*(Sudo is often required for GPIO access on Pi)*

# Ethical & Technical Reflection: Autonomous Mobile Robotics
In designing the autonomous Picar X application, ethical considerations were embedded directly into the control architecture. The system was programmed to prioritize safety over mission completion, ensuring responsible decision-making at every stage. Specifically, the safety_check() function executes before any navigation logic. By reading ultrasonic sensor data first, the robot guarantees that if an obstacle is detected within 15 cm, the decision to stop overrides the line-following behavior. This approach reflects a core principle of responsible robotics: a system must remain aware of its environment and maintain a fail-safe state to prevent harm to itself or its surroundings.

Safety was the primary operational concern. Although the robot’s physical design is small and lightweight, its kinetic energy can still cause damage. To mitigate this risk, motor power was capped at a 20% duty cycle, ensuring low speeds that allow sufficient reaction time. Regarding privacy, this design is inherently privacy-preserving. Unlike systems that rely on cloud-based AI or facial recognition, the Picar X processes all data locally using simple infrared (grayscale) and ultrasonic sensors. It does not record, store, or transmit personal data or visual feeds, effectively eliminating risks of surveillance or data leakage.

Currently, the robot communicates its state only through movement. If it stops, users may not know whether it is paused, broken, or detecting an obstacle. To improve accessibility, particularly for visually impaired users, I would integrate audio feedback (via a buzzer or text-to-speech module) to announce states such as “Obstacle Detected” or “Path Lost.” For users with hearing impairments, RGB LEDs could flash red for “Stop” and green for “Go.” Providing multimodal feedback—sound and light—ensures transparency and inclusivity in design.

Developing this system reinforced that trust in AI is built on predictability, not just intelligence. For humans to trust a robot, its behavior must be consistent. During testing, confidence was established only after repeated trials confirmed that emergency braking logic worked 100% of the time. This project also highlighted the collaborative nature of human-robot interaction. The robot is not fully autonomous; it depends on humans to define parameters (safe distance, speed) and the environment (track layout). True success requires anticipating failure modes and embedding ethical frameworks and safety constraints into the design. Ultimately, an AI system is only as reliable as the principles and safeguards defined by its human creators.

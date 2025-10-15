# LinearVoltageSupply
This is a basic linear voltage regulator supply, capable of providing voltages between 1.2V to applied input voltage. LM317 IC is used to regulate the voltage to the necessary output voltage, adjusted by a potentiometer. An improved version is capable of dimming and indicating voltage using LED.
---

## **Design 1: LM317 Adjustable Voltage Supply**

### **Description**
- **IC:** LM317 voltage regulator
- **Output Voltage:** Adjustable from **1.2V up to the required voltage**
- **Components:**
  - Two parallel capacitors on **input** and **output** (for stability and noise reduction)
  - **5k potentiometer** on the adjust pin to set the output voltage
- **Features:** Stable, low-ripple DC output with simple design

### **Operation**
1. AC mains is stepped down and rectified (if using AC input) or a DC source is connected.
2. Input capacitor smooths the incoming voltage.
3. LM317 regulates the voltage based on the potentiometer setting.
4. Output capacitor improves stability and reduces noise.

---

## **Design 2: LM317 with Power-Indicating LED**

### **Description**
- **IC:** LM317 voltage regulator
- **LED Indicator:** Uses a **2N7000 logic-level MOSFET** to drive a LED.
- **Function:** LED brightness varies with output power — higher power → brighter LED; lower power → dimmer LED.
- **Components:** Same as Design 1 plus the MOSFET and LED circuit.
- **Features:** Provides visual feedback of output power and adds a simple load-indicator functionality.

### **Operation**
1. Voltage is regulated by LM317 as in Design 1.
2. The MOSFET senses the voltage/current and adjusts the LED brightness accordingly.
3. LED provides intuitive feedback of power delivered.

---

## **Files**
- `Circuit/` → Multisim files (`.msm`) for both designs  
- `Schematic_PNGs/` → Exported schematic images  
- `Photos/` → Photos of the physical circuits  
- `Documentation/` → Optional detailed explanations

---

## **Usage**
1. Open the `.msm` files in **Multisim** to simulate the circuits.
2. Use the schematic images as a quick reference.
3. Check the photos to see the actual builds.

---

## **License**
This project is licensed under the **MIT License**. You are free to use, modify, and share the designs, but please give credit to the original creator.

---

## **Notes**
- LM317 requires **input voltage at least 3V higher than desired output voltage**.  
- Ensure capacitors are rated appropriately for your input voltage.  
- When using Design 2, the LED brightness is a simple visual indicator and not a precise power meter.  


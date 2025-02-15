# DIY Raspberry Pi Digital Microscope

## Overview
This project is a **DIY Digital Microscope** built using a **Raspberry Pi Zero**, a **Raspberry Pi Camera**, and a **custom 3D-printed enclosure**. It allows for real-time microscopic inspection, making it a great tool for electronics and PCB work.

📜 **Read the full blog post here:** [How I Built a DIY Digital Microscope](https://eliferrara.com/2025/01/02/Digital_Microscope.html)

## Features
✔ **High-resolution Raspberry Pi Camera**  
✔ **15x zoom macro lens for detailed imaging**  
✔ **Adjustable rack-and-pinion focus system**  
✔ **Custom 3D-printed enclosure**  
✔ **Built-in LED illumination powered by GPIO**  
✔ **Physical shutdown button for safe operation**  

## Hardware Components
- **Raspberry Pi Zero**
- **Raspberry Pi Camera Module**
- **15x Zoom Macro Lens**
- **Adjustable Rack & Pinion Focus System**
- **5V LED for Illumination**
- **Custom 3D-printed Enclosure**
- **Physical Power Button (GPIO Shutdown)**

## Software & Setup
The microscope uses **Raspbian Buster** and the `raspivid` command for real-time streaming. Setup steps include:

1. **Enable the Camera Stack** using `sudo raspi-config`
2. **SSH into the Raspberry Pi** using `ssh pi@<your-ip-address>`
3. **Run the Camera Stream** with the command:
   ```sh
   raspivid -t 0 -w 1920 -h 1080 -fps 30 -sa 10 -rot 180
   ```

### Example Wiring Diagram (Simplified)
```plaintext
[ Raspberry Pi ] --> [ Camera Module ]
                  --> [ LED (5V, GND) ]
                  --> [ Physical Shutdown Button (GPIO21, GND) ]
```

## 3D Printing Files & Assembly Guide
All **.STEP**, **STL**, and **wiring diagrams** are provided in the repository.

📂 **Download Here:** [GitHub Repository](https://github.com/Ballistyxx/digital-microscope)

## Known Limitations & Future Improvements
⚠ **Base Flexibility Issues** – Will be redesigned for added stability.  
⚠ **Easier Maintenance Needed** – Future designs will use heated inserts for better access.  
⚠ **Better Cable Management** – A PCB design may replace individual wires for reliability.  

## License
This project is open-source under the **MIT License**. Feel free to modify and improve!

## Author
Developed by **Ballistyxx**  
📧 **Contact:** [GitHub Issues](https://github.com/Ballistyxx/digital-microscope/issues)

---
✨ **If you like this project, consider giving it a ⭐ on GitHub!**


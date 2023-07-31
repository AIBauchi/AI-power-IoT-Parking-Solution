# AI-powered IoT Parking Solution

![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

Welcome to the AI-powered IoT Parking Solution repository! This project is a demo that showcases an automated parking management system using a Raspberry Pi, IR sensor, servo motor, and an Optical Character Recognition (OCR) model. The system detects incoming vehicles, recognizes license plate numbers using OCR, and validates them against a database to grant access. The servo motor controls the gate, allowing entry for authorized vehicles.

## Key Features

- Automatic vehicle detection using an IR sensor.
- License plate recognition using an OCR model for seamless access control.
- Integration of AI and IoT technologies for an efficient and smart parking solution.
- Database lookup to validate recognized license plates.
- Real-time gate control using a servo motor for authorized vehicles.

## Installation and Usage

1. Clone this repository to your Raspberry Pi.
2. Install the required dependencies by following the instructions in the `requirements.txt` file.
3. Set up the OCR model (pre-trained or custom-trained) and adjust the `ocr_process()` function in the PC client script to suit your model's requirements.
4. Update the database with authorized license plate numbers in the `data.txt` file.
5. Connect the IR sensor and servo motor to your Raspberry Pi.
6. Run the Raspberry Pi script on your Raspberry Pi to start the parking lot system.
7. Run the PC client script on your PC to receive frames from the Raspberry Pi and process them using the OCR model.

## List of Components Needed

To replicate this demo project, you will need the following components:

- Raspberry Pi (with power supply and SD card)
- IR sensor module
- Servo motor
- Camera module (for the Raspberry Pi)
- PC with Python and required dependencies installed

Please note that this project is intended as a demonstration and may require further refinement for practical implementation in real-world scenarios.

## Contributing

As a demo project, we appreciate any feedback, suggestions, or improvements you may have. Feel free to open issues or submit pull requests.

## License

This demo project is licensed under the [Apache License 2.0](LICENSE).

## Acknowledgments

We acknowledge the open-source community and thank them for their contributions to the libraries and tools used in this demo.


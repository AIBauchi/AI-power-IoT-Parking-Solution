- **Set Up the OCR Model**: you already have a custom-trained OCR model, adjust the ocr_process() function in the PC client script (pc_client.py) to load and process the OCR model accordingly.

- **Update the Database**: In the data.txt file, add the license plate numbers of authorized vehicles that can access the parking lot. The system will use this database to validate recognized license plates.

- **Connect Hardware Components**: Connect the IR sensor and servo motor to your Raspberry Pi correctly. Make sure they are properly powered and set up to interface with the Raspberry Pi's GPIO pins.
    - Connect the IR sensor to GPIO pin 16 of the Raspberry Pi to detect incoming vehicles.
    - Attach the servo motor to GPIO pin 25 of the Raspberry Pi for gate control.
    - Ensure the Raspberry Pi and PC are on the same network for communication.



- **Run the Scripts**: 
    - On your Raspberry Pi, execute the following command to start the parking lot system:

        ```bash
        python raspberry_pi_script.py
        ```
    - On your PC, run the following command to receive frames from the Raspberry Pi and process them using the OCR model:


        ```bash
        python pc_client.py
        ```


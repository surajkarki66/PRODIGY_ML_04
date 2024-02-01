# PRODIGY_ML_04
## Overview
Develop a hand gesture recognition model that can accurately identify and classify different hand gestures from image or video data, enabling intuitive human-computer interaction and gesture-based control systems. All the steps that are required for the experiment such as data preparation, model building, training, evaluation and saving are provided in the IPython notebook: `PRODIGY_ML_04.ipynb`. The model inference was done on `app.py` and `live_detection.py`

## How to do inference?
1. Clone this repository.
   ```bash
   git clone https://github.com/surajkarki66/PRODIGY_ML_04
   ```
2. Create a Python virtual environment and activate the environment based on your machine(Linux, MacOS, and Windows)
3. Download the trained model from [here](https://github.com/surajkarki66/PRODIGY_ML_04/releases/download/V0.0.1/hand_gesture.h5) and put it into the project root directory.
4. Install the requirements
   ```bash
   pip install -r requirements.txt
   ```
5. Run the following command
   To run the normal demo:
   ```bash
   python app.py
   ```

   To run the live detection demo:
   ```bash
   python live_detection.py
   ```

Demo
![Screenshot from 01-02-24 21:11:09](https://github.com/surajkarki66/PRODIGY_ML_04/assets/50628520/59fb09e9-1058-4520-af49-b9ed6c89a305)


Happy coding!

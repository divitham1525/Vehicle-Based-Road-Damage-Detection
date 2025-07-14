import serial
import time
data = serial.Serial(
                    'COM3',
                    baudrate = 9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS,
                    timeout=1
                    )

def Send(a):
  data.write(str.encode(a))
  print('sent............')

def Read():
    print("reading")
#   while True:
    Data = data.readline()
    Data = Data.decode('utf-8', 'ignore')
    print("Raw data is ---- {}  ---".format(Data))
    return Data


    # if Data:  # Ensure Data is not empty after stripping
    #     try:
    #         Data_parts = Data.split(':')
    #         # print("Split data: ", Data_parts)
    #         print("ghhdggdhs : {}".format(Data_parts[1]))
    #         # Add any specific processing logic here
    #         if len(Data_parts) == 7:  # Example condition
    #             print("Valid data received.")
    #             return Data_parts[1]

    #     except Exception as e:
    #         print(f"Error processing data: {e}")
    # time.sleep(0.1) 
    # break # Avoid busy-waiting
    # # return Data_parts[1]
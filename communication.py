import serial.tools.list_ports
import time


class SerialCommunication:
    def __init__(self):
        self.ports = serial.tools.list_ports.comports()
        self.serial_inst = serial.Serial()
        self.ports_list = []
        self.first_motor_flag = None
        self.second_motor_flag = None
        # first_motor = 300 #0=> -35degree; 300=> 0 degree; 600=>+35 degree left(minus) to right(positive)
        # second_motor = 225 #0=> -25degree; 225=> 0 degree; 450=>+25 degree top(minus) to buttom(positive)

    def initialize_port(self):
        for onePort in self.ports:
            self.ports_list.append(str(onePort))
            print(str(onePort))
        val = 5
        for x in range(0, len(self.ports_list)):
            if self.ports_list[x].startswith("COM" + str(val)):
                port_var = "COM" + str(val)
                print(port_var)
        self.serial_inst.baudrate = 38400
        self.serial_inst.port = port_var
        self.serial_inst.open()
        time.sleep(1)
        self.first_motor_flag = True
        self.second_motor_flag = True

    def send_data_to_stm32(self, first_motor, second_motor):
        first_motor = int(first_motor)
        second_motor = int(second_motor)
        if self.first_motor_flag:
            if first_motor < 10:
                self.serial_inst.write(f"00{first_motor}".encode())
            elif first_motor < 100:
                self.serial_inst.write(f"0{first_motor}".encode())
            else:
                self.serial_inst.write(f"{first_motor}".encode())

            self.first_motor_flag = False
            self.second_motor_flag = True
            time.sleep(0.02)

        if self.second_motor_flag:
            if second_motor < 10:
                self.serial_inst.write(f"00{second_motor}".encode())
            elif second_motor < 100:
                self.serial_inst.write(f"0{second_motor}".encode())
            else:
                self.serial_inst.write(f"{second_motor}".encode())
            self.second_motor_flag = False
            self.first_motor_flag = True
            time.sleep(0.02)

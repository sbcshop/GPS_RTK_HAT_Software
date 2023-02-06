
# The following code is a dependent on work by daymople and the awesome parsing
# capabilities of ubxtranslator: https://github.com/dalymople/ubxtranslator.


import struct
import serial

from . import ublox_predefine as sp
from .import core


_MODULE_I2C_ADD = [0x42]

class Ublox_F9P(object): 
    module_address = _MODULE_I2C_ADD

    def __init__(self, serial_1 = None):
        if serial_1 is None:
            self.serial_1 = serial.Serial("/dev/ttyS0/", 38400, timeout=1) # Default serial at a 38400 baud rate
        else:
            self.serial_1 = serial_1

        # Class message values        
        self.cfg_ms= {'RST':0x04,  'VALGET':0x8b}
        self.esf_ms= {'MEAS':0x02, 'RAW':0x03,'STATUS':0x10} 
        self.mon_ms= {'COMMS':0x36,  'GNSS':0x28,  'HW3':0x37,'PIO':0x24,'PT2':0x2b,'RF':0x38,'RXR':0x21,'SPT':0x2f}
        self.nav_ms= {'ATT':0x05,'PVT':0x07,'SAT':0x35}


    '''
    Sends a ublox message to the ublox module.
    '''
    def send_data(self, ubx_class, ubx_id, gps_payload = None):
        CHAR1 = 0xB5
        CHAR2 = 0x62

        if gps_payload == b'\x00' or gps_payload is None:
            payload_1length = 0
        elif type(gps_payload) is not bytes:
            gps_payload = bytes([gps_payload])
            payload_1length = len(gps_payload)
        else:
            payload_1length = len(gps_payload)

        if payload_1length > 0:
            message = struct.pack('BBBBBB', CHAR1, CHAR2,
                                  ubx_class.id_, ubx_id, (payload_1length & 0xFF),
                                  (payload_1length >> 8)) + gps_payload

        else:
            message = struct.pack('BBBBBB', CHAR1, CHAR2,
                                  ubx_class.id_, ubx_id, (payload_1length & 0xFF),
                                  (payload_1length >> 8))

        checksum = core.Parser._generate_fletcher_checksum(message[2:])

        self.serial_1.write(message + checksum)

        return True

    
    def uart_enable(self, enable):
        if enable is True:
            self.send_data(sp.CFG_CLS, self.cfg_ms.get('RST'), 0x00)

        parse = core.Parser([sp.CFG_CLS, sp.ACK_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg  

    
    def gps_get_data(self, key_id):
        key_id_bytes = bytes([])
        if type(key_id) != bytes:
            while key_id > 0:
                key_id_bytes = key_id_bytes + bytes([(key_id & 0xFF)])
                key_id = key_id >> 8

        key_id_bytes = key_id_bytes[::-1]
        msg = self.send_data(sp.CFG_CLS, self.cfg_ms.get('VALGET'), key_id_bytes)
        parse = core.Parser([sp.CFG_CLS, sp.ACK_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the NAV class with the PVT Message ID 
    '''
    def DateTime(self):
        self.send_data(sp.NAV_CLS, self.nav_ms.get('PVT'))
        parse = core.Parser([sp.NAV_CLS])
        cls_name, msg_name, payload = parse.receive_from(self.serial_1)
        s_payload = self.NAV_PVT(payload)
        return s_payload
    
    '''
    Sends a poll request for the NAV class with the PVT Message ID 
    '''
    def coordinates(self):
        self.send_data(sp.NAV_CLS, self.nav_ms.get('PVT'))
        parse = core.Parser([sp.NAV_CLS])
        cls_name, msg_name, payload = parse.receive_from(self.serial_1)
        s_payload = self.NAV_PVT(payload)
        return s_payload


    '''
    Sends a poll request for the NAV class with the ATT Message ID 
    '''
    def vehicle_attitude(self):
        self.send_data(sp.NAV_CLS, self.nav_ms.get('ATT'))
        parse = core.Parser([sp.NAV_CLS])
        print(parse)
        cls_name, msg_name, payload = parse.receive_from(self.serial_1)
        print(cls_name, msg_name, payload)
        s_payload = self.NAV_ATT(payload)
        return s_payload


    '''
    Sends a poll request for the MON class with the COMMS Message ID 
    '''
    def port_settings(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('COMMS'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg
    
    '''
    Reads directly from the module's data stream
    '''
    def NMEA_Stream(self):
        return self.serial_1.readline().decode('utf-8')


    '''
    Sends a poll request for the ESF class with the MEAS Message ID 
    '''
    def esf_measures(self):
        self.send_data(sp.ESF_CLS, self.get('MEAS'))
        parse = core.Parser([sp.ESF_CLS])
        cls_name, msg_name, payload = parse.receive_from(self.serial_1)
        return payload

    
    '''
        Sends a poll request for the MON class with the GNSS Message ID 
    '''
    def module_gnss(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('GNSS'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the MON class with the HW3 Message ID 
    '''
    def pin_settings(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('HW3'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the MON class with the PATCH Message ID 
    '''
    def patches_installed(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('HW3'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the MON class with the PIO Message ID 
    '''
    def prod_test_pio(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('PIO'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the MON class with the TEMP Message ID
    '''
    def temp_val_state(self):
        msg = self.send_data(sp.MON_CLS, self.mon_ms.get('TEMP'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg
    

    '''
    Ii takes the UBX-NAV-PVT payload 
    '''
    def NAV_PVT(self, payload_1):
        Long = payload_1.lon # longitude
        Lati = payload_1.lat # latitude
        head_mot = payload_1.head_motion
        head_acc = payload_1.headAcc
        pos_dop = payload_1.pDOP
        head_veh = payload_1.headVeh
        mag_dec = payload_1.magDec
        mag_acc = payload_1.magAcc

        payload_1 = payload_1._replace(lon=Long *(10**-7))
        payload_1 = payload_1._replace(lat=Lati * (10**-7))
        payload_1 = payload_1._replace(head_motion = head_mot * (10**-5))
        payload_1 = payload_1._replace(headAcc = head_acc * (10**-5))
        payload_1 = payload_1._replace(pDOP= pos_dop * 0.01)
        payload_1 = payload_1._replace(headVeh = head_veh * (10**-5))
        payload_1 = payload_1._replace(magDec = mag_dec * (10**-2))
        payload_1 = payload_1._replace(magAcc = mag_acc * (10**-2))

        return payload_1
    
    '''
    Sends a poll request for the MON class with the VER Message ID
    '''
    def app_version(self):
        msg = self.send_data(sp.MON_CLS, self.mon_ms.get('VER'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg
    

    '''
    Sends a poll request for the MON class with the PT2 Message ID 
    '''
    def prod_test_monitor(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('PT2'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    Sends a poll request for the NAV class with the SAT Message ID 
    '''
    def satellite_numbers(self):
        self.send_data(sp.NAV_CLS, self.nav_ms.get('SAT'))
        parse = core.Parser([sp.NAV_CLS])
        cls_name, msg_name, payload = parse.receive_from(self.serial_1)
        s_payload = self.NAV_SAT(payload)
        return s_payload
    

    '''
    Sends a poll request for the MON class with the RF Message ID 
    '''
    def RF_Status(self):
        msg = self.send_data(sp.MON_CLS, self.esf_ms.get('RF'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg



    '''
    Sends a poll request for the MON class with the RXR Message ID 
    '''
    def module_wake_state(self):
        msg = self.send_data(sp.MON_CLS, self.mon_ms.get('RXR'))
        parse = core.Parser([sp.MON_CLS])
        msg = parse.receive_from(self.serial_1)
        return msg


    '''
    This takes the UBX-NAV-SAT payload

    '''  
    def NAV_SAT(self, payload_1):
        pr_res = payload_1.prRes
        payload_1 = nav_payload._replace(prRes= pr_res * 0.1)

        return payload_1    

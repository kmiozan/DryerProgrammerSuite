import subprocess
import logging

class AtprogramInterface():
    """
    This class provides an interface for Atmel's atprogram executable.
    """

    def __init__(self,
                 _atprogram="C:\\Program Files (x86)\\Atmel\\Studio\\7.0\\atbackend\\atprogram.exe",
                 _tool=None,
                 _device=None,
                 _interface=None,
                 #_command="program",
                 _clock=None,
                 _file="emperor.hex",
                 #_fuses=None,
                 _verbose=False,
                 _userInterface=None):

        #self.device = _device
        #self.interface = _interface
        #self.command = _command
        #self.clock = _clock
        #self.file = _file
        #self.fuses = _fuses
        self.verbose = _verbose
        self.userInterface = _userInterface
        #self.atprogram = _atprogram
        #self.tool = _tool
        self.callList = []
        self.callList.extend([_atprogram, "--tool", _tool, "--device", _device, "--interface", _interface])
        print("a " + str(self.callList))

        self.atprogramVersion(_atprogram)

        #self.chipErase()
        #self.writeFuses("E2D9FD")
        #self.programCalib("rc_calib.hex")
        #self.writeFuses("D2D9FD")
        #self.program(_command,_file)

    def atprogramVersion(self, atprogram):
        callList = [atprogram, "--version"]
        try:
            subprocess.call(callList)
        except:
            print("Please point the atprogram.exe location")
            raise


    def program(self, memory, file, clock="125khz", verify=False, verifyFile=None, verifyFileFormat=None, offset=False, offsetValue="0"):

        if verify:
            callList = self.callList + ["--clock", clock, "program", memory, "--verify", "--format", verifyFileFormat  "--file", verifyFile]
        else:
            if offset:
                callList = self.callList + ["--clock", clock, "program", memory, "--file", file]
            else:
                callList = self.callList + ["--clock", clock, "program", memory, "--file", file, "--offset", offsetValue]

        print("programming " +str(callList))

        subprocess.check_call(callList)
        subprocess.call("pause")

    def write(self, memory, values, clock):
        callList = self.callList + ["--clock", clock, "write", memory, "--values", values]
        print("writing " + str(callList))

        subprocess.check_call(callList)

    def read(self, memory, format, clock, file, size=False, sizeValue="1", offset=False, offsetValue="0"):

        if size:
            if offset:
                callList = self.callList + ["--clock", clock, "read", memory, "--size", sizeValue, "--offset", offsetValue, "--format", format, file]
            else:
                callList = self.callList + ["--clock", clock, "read", memory, "--size", sizeValue, "--format", format, file]
        else:
            if offset:
                callList = self.callList + ["--clock", clock, "read", memory, "--offset", offsetValue, "--format", format, file]
            else:
                callList = self.callList + ["--clock", clock, "read", memory,  "--format", format, file]

        print("reading " + str(callList))

        subprocess.check_call(callList)

    def verify(self, memory, file, clock="125khz"):
        callList = self.callList + ["--clock", clock, "verify", memory, "--file", file]
        print("verifying " + str(callList))

        subprocess.check_call(callList)

    def chipErase(self, clock="250khz"):
        callList = self.callList + ["--clock", clock, "chiperase"]
        print("erasing chip " + str(callList))

        subprocess.check_call(callList)

    def calibrate(self):
        callList = self.callList + ["calibrate"]
        print("calibrating " + str(callList))

        subprocess.check_call(callList)

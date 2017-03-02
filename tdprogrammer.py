# -*- coding: utf-8 -*-

from atprogramInterface import AtprogramInterface

ai = AtprogramInterface(_tool="atmelice",
                        _device="atmega644pa",
                        _interface="ISP"
                        )

ai.chipErase()
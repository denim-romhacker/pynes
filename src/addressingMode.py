def Zero(cpu):
    address = cpu.dmaRAMRead(cpu.registers['PC']+1)

    return address

def Zero_X(cpu):
    address = cpu.dmaRAMRead(cpu.registers['PC']+1)
    address = (address + cpu.registers['X']) & 0xFF

    return address

def Zero_Y(cpu):
    address = cpu.dmaRAMRead(cpu.registers['PC']+1)
    address = (address + cpu.registers['Y']) & 0xFF

    return address

def Absolute(cpu):
    addr1 = cpu.dmaRAMRead(cpu.registers['PC']+1)
    addr2 = cpu.dmaRAMRead(cpu.registers['PC']+2)
    address = ((addr2 << 8) | addr1) & 0xFFFF

    return address

def Absolute_X(cpu):
    addr1 = cpu.dmaRAMRead(cpu.registers['PC']+1)
    addr2 = cpu.dmaRAMRead(cpu.registers['PC']+2)
    address = (((addr2 << 8) | addr1) + cpu.registers['X']) & 0xFFFF

    return address

def Absolute_Y(cpu):
    addr1 = cpu.dmaRAMRead(cpu.registers['PC']+1)
    addr2 = cpu.dmaRAMRead(cpu.registers['PC']+2)
    address = (((addr2 << 8) | addr1) + cpu.registers['Y']) & 0xFFFF

    return address

def Indirect(cpu):
    addr1 = cpu.dmaRAMRead(cpu.registers['PC']+1)
    addr2 = cpu.dmaRAMRead(cpu.registers['PC']+2)
    addressTmp = addr2 << 8
    addressTmp += addr1

    address = cpu.dmaRAMRead(addressTmp) | (cpu.dmaRAMRead((addressTmp & 0xFF00) | ((addressTmp + 1) & 0x00FF)) << 8)

    return address

def Indirect_X(cpu):
    value = (cpu.dmaRAMRead(cpu.registers['PC']+1))
    addr1 = (cpu.dmaRAMRead((value + cpu.registers['X']) & 0xFF))
    addr2 = (cpu.dmaRAMRead((value + cpu.registers['X']+1) & 0xFF))
    address = ((addr2 << 8) | addr1) & 0xFFFF

    return address

def Indirect_Y(cpu):
    value = (cpu.dmaRAMRead(cpu.registers['PC']+1))
    addr1 = (cpu.dmaRAMRead(value))
    addr2 = (cpu.dmaRAMRead((value+1) & 0xFF))
    address = (((addr2 << 8) | addr1) + cpu.registers['Y']) & 0xFFFF

    return address
RV32M_INST = [
    {'mnemonic': 'mul', 'handler': 'mul_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulh', 'handler': 'mulh_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulhsu', 'handler': 'mulhsu_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulhu', 'handler': 'mulhu_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'div', 'handler': 'div_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divu', 'handler': 'divu_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'rem', 'handler': 'rem_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remu', 'handler': 'remu_32', 'cost': 1, 'tags': 'M_EXT_32', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
]

RV64M_INST = [
    {'mnemonic': 'mul', 'handler': 'mul_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulh', 'handler': 'mulh_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulhsu', 'handler': 'mulhsu_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulhu', 'handler': 'mulhu_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'div', 'handler': 'div_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divu', 'handler': 'divu_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'rem', 'handler': 'rem_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remu', 'handler': 'remu_64', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'mulw', 'handler': 'mul_32', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divw', 'handler': 'div_32', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'divuw', 'handler': 'divu_32', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remw', 'handler': 'rem_32', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
    {'mnemonic': 'remuw', 'handler': 'remu_32', 'cost': 1, 'tags': 'M_EXT_64', 'memory': False, 'cof': False, 'vdeleg': False, 'vector': False, 'float': False, 'maskable': False, 'segment': False, 'indexed': False, 'atomic': False, 'crypto': False},
]

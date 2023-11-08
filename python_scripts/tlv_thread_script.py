import python_otbr_api
from python_otbr_api import PENDING_DATASET_DELAY_TIMER, tlv_parser
from python_otbr_api.pskc import compute_pskc
from python_otbr_api.tlv_parser import MeshcopTLVType, MeshcopTLVItem

# Apple
CHANNEL = 25
PANID = "4b28"
EXTPANID = "20d0f9bab1c84eb7"
NETWORK_KEY = "a87099faf2a869a305132e6ff7d881e6"
TIMESTAMP = b'\x00\x00\x00\x00\x00\x03\x00\x00'

channel = MeshcopTLVItem(tag=0, data=CHANNEL.to_bytes(length=3, byteorder='big'))
pan_id= MeshcopTLVItem(tag=1, data=bytes.fromhex(PANID))
ext_pan_id = MeshcopTLVItem(tag=2, data=bytes.fromhex(EXTPANID))
network_key = MeshcopTLVItem(tag=5, data=bytes.fromhex(NETWORK_KEY))
timestamp = MeshcopTLVItem(tag=14, data=TIMESTAMP)

tlv_new = {0: channel, 1: pan_id, 2:ext_pan_id, 4: network_key, 14: timestamp}
tlv  = tlv_parser.encode_tlv(tlv_new)
print(tlv)
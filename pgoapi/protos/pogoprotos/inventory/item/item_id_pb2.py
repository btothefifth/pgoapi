# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/inventory/item/item_id.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/inventory/item/item_id.proto',
  package='pogoprotos.inventory.item',
  syntax='proto3',
  serialized_pb=_b('\n\'pogoprotos/inventory/item/item_id.proto\x12\x19pogoprotos.inventory.item*\x8d\t\n\x06ItemId\x12\x10\n\x0cITEM_UNKNOWN\x10\x00\x12\x12\n\x0eITEM_POKE_BALL\x10\x01\x12\x13\n\x0fITEM_GREAT_BALL\x10\x02\x12\x13\n\x0fITEM_ULTRA_BALL\x10\x03\x12\x14\n\x10ITEM_MASTER_BALL\x10\x04\x12\x15\n\x11ITEM_PREMIER_BALL\x10\x05\x12\x0f\n\x0bITEM_POTION\x10\x65\x12\x15\n\x11ITEM_SUPER_POTION\x10\x66\x12\x15\n\x11ITEM_HYPER_POTION\x10g\x12\x13\n\x0fITEM_MAX_POTION\x10h\x12\x10\n\x0bITEM_REVIVE\x10\xc9\x01\x12\x14\n\x0fITEM_MAX_REVIVE\x10\xca\x01\x12\x13\n\x0eITEM_LUCKY_EGG\x10\xad\x02\x12\x1a\n\x15ITEM_INCENSE_ORDINARY\x10\x91\x03\x12\x17\n\x12ITEM_INCENSE_SPICY\x10\x92\x03\x12\x16\n\x11ITEM_INCENSE_COOL\x10\x93\x03\x12\x18\n\x13ITEM_INCENSE_FLORAL\x10\x94\x03\x12\x13\n\x0eITEM_TROY_DISK\x10\xf5\x03\x12\x12\n\rITEM_X_ATTACK\x10\xda\x04\x12\x13\n\x0eITEM_X_DEFENSE\x10\xdb\x04\x12\x13\n\x0eITEM_X_MIRACLE\x10\xdc\x04\x12\x14\n\x0fITEM_RAZZ_BERRY\x10\xbd\x05\x12\x14\n\x0fITEM_BLUK_BERRY\x10\xbe\x05\x12\x15\n\x10ITEM_NANAB_BERRY\x10\xbf\x05\x12\x15\n\x10ITEM_WEPAR_BERRY\x10\xc0\x05\x12\x15\n\x10ITEM_PINAP_BERRY\x10\xc1\x05\x12\x1b\n\x16ITEM_GOLDEN_RAZZ_BERRY\x10\xc2\x05\x12\x1c\n\x17ITEM_GOLDEN_NANAB_BERRY\x10\xc3\x05\x12\x1c\n\x17ITEM_GOLDEN_PINAP_BERRY\x10\xc4\x05\x12\x18\n\x13ITEM_SPECIAL_CAMERA\x10\xa1\x06\x12#\n\x1eITEM_INCUBATOR_BASIC_UNLIMITED\x10\x85\x07\x12\x19\n\x14ITEM_INCUBATOR_BASIC\x10\x86\x07\x12\x19\n\x14ITEM_INCUBATOR_SUPER\x10\x87\x07\x12!\n\x1cITEM_POKEMON_STORAGE_UPGRADE\x10\xe9\x07\x12\x1e\n\x19ITEM_ITEM_STORAGE_UPGRADE\x10\xea\x07\x12\x13\n\x0eITEM_SUN_STONE\x10\xcd\x08\x12\x14\n\x0fITEM_KINGS_ROCK\x10\xce\x08\x12\x14\n\x0fITEM_METAL_COAT\x10\xcf\x08\x12\x16\n\x11ITEM_DRAGON_SCALE\x10\xd0\x08\x12\x12\n\rITEM_UP_GRADE\x10\xd1\x08\x12!\n\x1cITEM_MOVE_REROLL_FAST_ATTACK\x10\xb1\t\x12$\n\x1fITEM_MOVE_REROLL_SPECIAL_ATTACK\x10\xb2\t\x12\x14\n\x0fITEM_RARE_CANDY\x10\x95\n\x12\x1a\n\x15ITEM_FREE_RAID_TICKET\x10\xf9\n\x12\x1a\n\x15ITEM_PAID_RAID_TICKET\x10\xfa\n\x12\x1f\n\x1aITEM_LEGENDARY_RAID_TICKET\x10\xfb\n\x12\x14\n\x0fITEM_STAR_PIECE\x10\xfc\nb\x06proto3')
)

_ITEMID = _descriptor.EnumDescriptor(
  name='ItemId',
  full_name='pogoprotos.inventory.item.ItemId',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ITEM_UNKNOWN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKE_BALL', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GREAT_BALL', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ULTRA_BALL', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MASTER_BALL', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PREMIER_BALL', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POTION', index=6, number=101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUPER_POTION', index=7, number=102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_HYPER_POTION', index=8, number=103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_POTION', index=9, number=104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_REVIVE', index=10, number=201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MAX_REVIVE', index=11, number=202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_LUCKY_EGG', index=12, number=301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_ORDINARY', index=13, number=401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_SPICY', index=14, number=402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_COOL', index=15, number=403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCENSE_FLORAL', index=16, number=404,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_TROY_DISK', index=17, number=501,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_ATTACK', index=18, number=602,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_DEFENSE', index=19, number=603,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_X_MIRACLE', index=20, number=604,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_RAZZ_BERRY', index=21, number=701,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_BLUK_BERRY', index=22, number=702,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_NANAB_BERRY', index=23, number=703,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_WEPAR_BERRY', index=24, number=704,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PINAP_BERRY', index=25, number=705,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_RAZZ_BERRY', index=26, number=706,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_NANAB_BERRY', index=27, number=707,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_GOLDEN_PINAP_BERRY', index=28, number=708,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SPECIAL_CAMERA', index=29, number=801,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC_UNLIMITED', index=30, number=901,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_BASIC', index=31, number=902,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_INCUBATOR_SUPER', index=32, number=903,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_POKEMON_STORAGE_UPGRADE', index=33, number=1001,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_ITEM_STORAGE_UPGRADE', index=34, number=1002,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_SUN_STONE', index=35, number=1101,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_KINGS_ROCK', index=36, number=1102,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_METAL_COAT', index=37, number=1103,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_DRAGON_SCALE', index=38, number=1104,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_UP_GRADE', index=39, number=1105,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MOVE_REROLL_FAST_ATTACK', index=40, number=1201,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_MOVE_REROLL_SPECIAL_ATTACK', index=41, number=1202,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_RARE_CANDY', index=42, number=1301,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_FREE_RAID_TICKET', index=43, number=1401,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_PAID_RAID_TICKET', index=44, number=1402,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_LEGENDARY_RAID_TICKET', index=45, number=1403,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ITEM_STAR_PIECE', index=46, number=1404,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=71,
  serialized_end=1236,
)
_sym_db.RegisterEnumDescriptor(_ITEMID)

ItemId = enum_type_wrapper.EnumTypeWrapper(_ITEMID)
ITEM_UNKNOWN = 0
ITEM_POKE_BALL = 1
ITEM_GREAT_BALL = 2
ITEM_ULTRA_BALL = 3
ITEM_MASTER_BALL = 4
ITEM_PREMIER_BALL = 5
ITEM_POTION = 101
ITEM_SUPER_POTION = 102
ITEM_HYPER_POTION = 103
ITEM_MAX_POTION = 104
ITEM_REVIVE = 201
ITEM_MAX_REVIVE = 202
ITEM_LUCKY_EGG = 301
ITEM_INCENSE_ORDINARY = 401
ITEM_INCENSE_SPICY = 402
ITEM_INCENSE_COOL = 403
ITEM_INCENSE_FLORAL = 404
ITEM_TROY_DISK = 501
ITEM_X_ATTACK = 602
ITEM_X_DEFENSE = 603
ITEM_X_MIRACLE = 604
ITEM_RAZZ_BERRY = 701
ITEM_BLUK_BERRY = 702
ITEM_NANAB_BERRY = 703
ITEM_WEPAR_BERRY = 704
ITEM_PINAP_BERRY = 705
ITEM_GOLDEN_RAZZ_BERRY = 706
ITEM_GOLDEN_NANAB_BERRY = 707
ITEM_GOLDEN_PINAP_BERRY = 708
ITEM_SPECIAL_CAMERA = 801
ITEM_INCUBATOR_BASIC_UNLIMITED = 901
ITEM_INCUBATOR_BASIC = 902
ITEM_INCUBATOR_SUPER = 903
ITEM_POKEMON_STORAGE_UPGRADE = 1001
ITEM_ITEM_STORAGE_UPGRADE = 1002
ITEM_SUN_STONE = 1101
ITEM_KINGS_ROCK = 1102
ITEM_METAL_COAT = 1103
ITEM_DRAGON_SCALE = 1104
ITEM_UP_GRADE = 1105
ITEM_MOVE_REROLL_FAST_ATTACK = 1201
ITEM_MOVE_REROLL_SPECIAL_ATTACK = 1202
ITEM_RARE_CANDY = 1301
ITEM_FREE_RAID_TICKET = 1401
ITEM_PAID_RAID_TICKET = 1402
ITEM_LEGENDARY_RAID_TICKET = 1403
ITEM_STAR_PIECE = 1404


DESCRIPTOR.enum_types_by_name['ItemId'] = _ITEMID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)

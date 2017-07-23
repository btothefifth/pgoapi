# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/requests/messages/push_notification_registry_message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/requests/messages/push_notification_registry_message.proto',
  package='pogoprotos.networking.requests.messages',
  syntax='proto3',
  serialized_pb=_b('\nPpogoprotos/networking/requests/messages/push_notification_registry_message.proto\x12\'pogoprotos.networking.requests.messages\"\xed\x02\n\x1fPushNotificationRegistryMessage\x12\x64\n\tapn_token\x18\x01 \x01(\x0b\x32Q.pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken\x12\x64\n\tgcm_token\x18\x02 \x01(\x0b\x32Q.pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.GcmToken\x1aY\n\x08\x41pnToken\x12\x17\n\x0fregistration_id\x18\x01 \x01(\t\x12\x19\n\x11\x62undle_identifier\x18\x02 \x01(\t\x12\x19\n\x11payload_byte_size\x18\x03 \x01(\x05\x1a#\n\x08GcmToken\x12\x17\n\x0fregistration_id\x18\x01 \x01(\tb\x06proto3')
)




_PUSHNOTIFICATIONREGISTRYMESSAGE_APNTOKEN = _descriptor.Descriptor(
  name='ApnToken',
  full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_id', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken.registration_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_identifier', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken.bundle_identifier', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_byte_size', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken.payload_byte_size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=454,
)

_PUSHNOTIFICATIONREGISTRYMESSAGE_GCMTOKEN = _descriptor.Descriptor(
  name='GcmToken',
  full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.GcmToken',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='registration_id', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.GcmToken.registration_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=456,
  serialized_end=491,
)

_PUSHNOTIFICATIONREGISTRYMESSAGE = _descriptor.Descriptor(
  name='PushNotificationRegistryMessage',
  full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apn_token', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.apn_token', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gcm_token', full_name='pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.gcm_token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PUSHNOTIFICATIONREGISTRYMESSAGE_APNTOKEN, _PUSHNOTIFICATIONREGISTRYMESSAGE_GCMTOKEN, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=126,
  serialized_end=491,
)

_PUSHNOTIFICATIONREGISTRYMESSAGE_APNTOKEN.containing_type = _PUSHNOTIFICATIONREGISTRYMESSAGE
_PUSHNOTIFICATIONREGISTRYMESSAGE_GCMTOKEN.containing_type = _PUSHNOTIFICATIONREGISTRYMESSAGE
_PUSHNOTIFICATIONREGISTRYMESSAGE.fields_by_name['apn_token'].message_type = _PUSHNOTIFICATIONREGISTRYMESSAGE_APNTOKEN
_PUSHNOTIFICATIONREGISTRYMESSAGE.fields_by_name['gcm_token'].message_type = _PUSHNOTIFICATIONREGISTRYMESSAGE_GCMTOKEN
DESCRIPTOR.message_types_by_name['PushNotificationRegistryMessage'] = _PUSHNOTIFICATIONREGISTRYMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushNotificationRegistryMessage = _reflection.GeneratedProtocolMessageType('PushNotificationRegistryMessage', (_message.Message,), dict(

  ApnToken = _reflection.GeneratedProtocolMessageType('ApnToken', (_message.Message,), dict(
    DESCRIPTOR = _PUSHNOTIFICATIONREGISTRYMESSAGE_APNTOKEN,
    __module__ = 'pogoprotos.networking.requests.messages.push_notification_registry_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.ApnToken)
    ))
  ,

  GcmToken = _reflection.GeneratedProtocolMessageType('GcmToken', (_message.Message,), dict(
    DESCRIPTOR = _PUSHNOTIFICATIONREGISTRYMESSAGE_GCMTOKEN,
    __module__ = 'pogoprotos.networking.requests.messages.push_notification_registry_message_pb2'
    # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.PushNotificationRegistryMessage.GcmToken)
    ))
  ,
  DESCRIPTOR = _PUSHNOTIFICATIONREGISTRYMESSAGE,
  __module__ = 'pogoprotos.networking.requests.messages.push_notification_registry_message_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.requests.messages.PushNotificationRegistryMessage)
  ))
_sym_db.RegisterMessage(PushNotificationRegistryMessage)
_sym_db.RegisterMessage(PushNotificationRegistryMessage.ApnToken)
_sym_db.RegisterMessage(PushNotificationRegistryMessage.GcmToken)


# @@protoc_insertion_point(module_scope)
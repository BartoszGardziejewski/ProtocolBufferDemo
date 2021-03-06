# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Person.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Person.proto',
  package='',
  syntax='proto2',
  serialized_options=_b('\n\031pwr.protocolbuffer.modelsB\rPeopleMessage'),
  serialized_pb=_b('\n\x0cPerson.proto\"L\n\x06Person\x12\r\n\x05\x66Name\x18\x01 \x02(\t\x12\r\n\x05lName\x18\x02 \x02(\t\x12\x0b\n\x03\x61ge\x18\x03 \x01(\x05\x12\x17\n\x08isFamous\x18\x04 \x01(\x08:\x05\x66\x61lse\"!\n\x06People\x12\x17\n\x06person\x18\x01 \x03(\x0b\x32\x07.PersonB*\n\x19pwr.protocolbuffer.modelsB\rPeopleMessage')
)




_PERSON = _descriptor.Descriptor(
  name='Person',
  full_name='Person',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fName', full_name='Person.fName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lName', full_name='Person.lName', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='Person.age', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='isFamous', full_name='Person.isFamous', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=16,
  serialized_end=92,
)


_PEOPLE = _descriptor.Descriptor(
  name='People',
  full_name='People',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person', full_name='People.person', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=94,
  serialized_end=127,
)

_PEOPLE.fields_by_name['person'].message_type = _PERSON
DESCRIPTOR.message_types_by_name['Person'] = _PERSON
DESCRIPTOR.message_types_by_name['People'] = _PEOPLE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Person = _reflection.GeneratedProtocolMessageType('Person', (_message.Message,), {
  'DESCRIPTOR' : _PERSON,
  '__module__' : 'Person_pb2'
  # @@protoc_insertion_point(class_scope:Person)
  })
_sym_db.RegisterMessage(Person)

People = _reflection.GeneratedProtocolMessageType('People', (_message.Message,), {
  'DESCRIPTOR' : _PEOPLE,
  '__module__' : 'Person_pb2'
  # @@protoc_insertion_point(class_scope:People)
  })
_sym_db.RegisterMessage(People)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tecton_proto/args/transformation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tecton_proto.args import user_defined_function_pb2 as tecton__proto_dot_args_dot_user__defined__function__pb2
from tecton_proto.common import spark_schema_pb2 as tecton__proto_dot_common_dot_spark__schema__pb2
from tecton_proto.args import basic_info_pb2 as tecton__proto_dot_args_dot_basic__info__pb2
from tecton_proto.common import id_pb2 as tecton__proto_dot_common_dot_id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tecton_proto/args/transformation.proto',
  package='tecton_proto.args',
  syntax='proto2',
  serialized_options=b'\n\017com.tecton.argsP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n&tecton_proto/args/transformation.proto\x12\x11tecton_proto.args\x1a-tecton_proto/args/user_defined_function.proto\x1a&tecton_proto/common/spark_schema.proto\x1a\"tecton_proto/args/basic_info.proto\x1a\x1ctecton_proto/common/id.proto\"\xa2\x04\n\x12TransformationArgs\x12\x44\n\x11transformation_id\x18\x01 \x01(\x0b\x32\x17.tecton_proto.common.IdR\x10transformationId\x12\x30\n\x04info\x18\x02 \x01(\x0b\x32\x1c.tecton_proto.args.BasicInfoR\x04info\x12>\n\x06inputs\x18\x03 \x03(\x0b\x32&.tecton_proto.args.TransformationInputR\x06inputs\x12H\n\x0btransformer\x18\x04 \x01(\x0b\x32&.tecton_proto.args.UserDefinedFunctionR\x0btransformer\x12V\n\x13transformation_type\x18\x05 \x01(\x0e\x32%.tecton_proto.args.TransformationTypeR\x12transformationType\x12\x1f\n\x0bhas_context\x18\x06 \x01(\x08R\nhasContext\x12J\n\x0frequest_context\x18\x07 \x01(\x0b\x32!.tecton_proto.args.RequestContextR\x0erequestContext\x12\x45\n\routput_schema\x18\x08 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x0coutputSchema\"\x9a\x02\n\x13TransformationInput\x12\x35\n\x13transformation_name\x18\x01 \x01(\tB\x02\x18\x01H\x00R\x12transformationName\x12\x1f\n\x08vds_name\x18\x02 \x01(\tB\x02\x18\x01H\x00R\x07vdsName\x12\x46\n\x11transformation_id\x18\x03 \x01(\x0b\x32\x17.tecton_proto.common.IdH\x01R\x10transformationId\x12N\n\x16virtual_data_source_id\x18\x04 \x01(\x0b\x32\x17.tecton_proto.common.IdH\x01R\x13virtualDataSourceIdB\x07\n\x05inputB\n\n\x08id_input\"J\n\x0eRequestContext\x12\x38\n\x06schema\x18\x01 \x01(\x0b\x32 .tecton_proto.common.SparkSchemaR\x06schema*6\n\x12TransformationType\x12\x07\n\x03SQL\x10\x02\x12\x0b\n\x07PYSPARK\x10\x03\x12\n\n\x06ONLINE\x10\x04\x42\x13\n\x0f\x63om.tecton.argsP\x01'
  ,
  dependencies=[tecton__proto_dot_args_dot_user__defined__function__pb2.DESCRIPTOR,tecton__proto_dot_common_dot_spark__schema__pb2.DESCRIPTOR,tecton__proto_dot_args_dot_basic__info__pb2.DESCRIPTOR,tecton__proto_dot_common_dot_id__pb2.DESCRIPTOR,])

_TRANSFORMATIONTYPE = _descriptor.EnumDescriptor(
  name='TransformationType',
  full_name='tecton_proto.args.TransformationType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SQL', index=0, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PYSPARK', index=1, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ONLINE', index=2, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1124,
  serialized_end=1178,
)
_sym_db.RegisterEnumDescriptor(_TRANSFORMATIONTYPE)

TransformationType = enum_type_wrapper.EnumTypeWrapper(_TRANSFORMATIONTYPE)
SQL = 2
PYSPARK = 3
ONLINE = 4



_TRANSFORMATIONARGS = _descriptor.Descriptor(
  name='TransformationArgs',
  full_name='tecton_proto.args.TransformationArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformation_id', full_name='tecton_proto.args.TransformationArgs.transformation_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transformationId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='info', full_name='tecton_proto.args.TransformationArgs.info', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='info', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inputs', full_name='tecton_proto.args.TransformationArgs.inputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inputs', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transformer', full_name='tecton_proto.args.TransformationArgs.transformer', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transformer', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transformation_type', full_name='tecton_proto.args.TransformationArgs.transformation_type', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transformationType', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='has_context', full_name='tecton_proto.args.TransformationArgs.has_context', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hasContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='request_context', full_name='tecton_proto.args.TransformationArgs.request_context', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='requestContext', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_schema', full_name='tecton_proto.args.TransformationArgs.output_schema', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='outputSchema', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=215,
  serialized_end=761,
)


_TRANSFORMATIONINPUT = _descriptor.Descriptor(
  name='TransformationInput',
  full_name='tecton_proto.args.TransformationInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='transformation_name', full_name='tecton_proto.args.TransformationInput.transformation_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='transformationName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='vds_name', full_name='tecton_proto.args.TransformationInput.vds_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', json_name='vdsName', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='transformation_id', full_name='tecton_proto.args.TransformationInput.transformation_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transformationId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='virtual_data_source_id', full_name='tecton_proto.args.TransformationInput.virtual_data_source_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='virtualDataSourceId', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
    _descriptor.OneofDescriptor(
      name='input', full_name='tecton_proto.args.TransformationInput.input',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='id_input', full_name='tecton_proto.args.TransformationInput.id_input',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=764,
  serialized_end=1046,
)


_REQUESTCONTEXT = _descriptor.Descriptor(
  name='RequestContext',
  full_name='tecton_proto.args.RequestContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='schema', full_name='tecton_proto.args.RequestContext.schema', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='schema', file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=1048,
  serialized_end=1122,
)

_TRANSFORMATIONARGS.fields_by_name['transformation_id'].message_type = tecton__proto_dot_common_dot_id__pb2._ID
_TRANSFORMATIONARGS.fields_by_name['info'].message_type = tecton__proto_dot_args_dot_basic__info__pb2._BASICINFO
_TRANSFORMATIONARGS.fields_by_name['inputs'].message_type = _TRANSFORMATIONINPUT
_TRANSFORMATIONARGS.fields_by_name['transformer'].message_type = tecton__proto_dot_args_dot_user__defined__function__pb2._USERDEFINEDFUNCTION
_TRANSFORMATIONARGS.fields_by_name['transformation_type'].enum_type = _TRANSFORMATIONTYPE
_TRANSFORMATIONARGS.fields_by_name['request_context'].message_type = _REQUESTCONTEXT
_TRANSFORMATIONARGS.fields_by_name['output_schema'].message_type = tecton__proto_dot_common_dot_spark__schema__pb2._SPARKSCHEMA
_TRANSFORMATIONINPUT.fields_by_name['transformation_id'].message_type = tecton__proto_dot_common_dot_id__pb2._ID
_TRANSFORMATIONINPUT.fields_by_name['virtual_data_source_id'].message_type = tecton__proto_dot_common_dot_id__pb2._ID
_TRANSFORMATIONINPUT.oneofs_by_name['input'].fields.append(
  _TRANSFORMATIONINPUT.fields_by_name['transformation_name'])
_TRANSFORMATIONINPUT.fields_by_name['transformation_name'].containing_oneof = _TRANSFORMATIONINPUT.oneofs_by_name['input']
_TRANSFORMATIONINPUT.oneofs_by_name['input'].fields.append(
  _TRANSFORMATIONINPUT.fields_by_name['vds_name'])
_TRANSFORMATIONINPUT.fields_by_name['vds_name'].containing_oneof = _TRANSFORMATIONINPUT.oneofs_by_name['input']
_TRANSFORMATIONINPUT.oneofs_by_name['id_input'].fields.append(
  _TRANSFORMATIONINPUT.fields_by_name['transformation_id'])
_TRANSFORMATIONINPUT.fields_by_name['transformation_id'].containing_oneof = _TRANSFORMATIONINPUT.oneofs_by_name['id_input']
_TRANSFORMATIONINPUT.oneofs_by_name['id_input'].fields.append(
  _TRANSFORMATIONINPUT.fields_by_name['virtual_data_source_id'])
_TRANSFORMATIONINPUT.fields_by_name['virtual_data_source_id'].containing_oneof = _TRANSFORMATIONINPUT.oneofs_by_name['id_input']
_REQUESTCONTEXT.fields_by_name['schema'].message_type = tecton__proto_dot_common_dot_spark__schema__pb2._SPARKSCHEMA
DESCRIPTOR.message_types_by_name['TransformationArgs'] = _TRANSFORMATIONARGS
DESCRIPTOR.message_types_by_name['TransformationInput'] = _TRANSFORMATIONINPUT
DESCRIPTOR.message_types_by_name['RequestContext'] = _REQUESTCONTEXT
DESCRIPTOR.enum_types_by_name['TransformationType'] = _TRANSFORMATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransformationArgs = _reflection.GeneratedProtocolMessageType('TransformationArgs', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMATIONARGS,
  '__module__' : 'tecton_proto.args.transformation_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.TransformationArgs)
  })
_sym_db.RegisterMessage(TransformationArgs)

TransformationInput = _reflection.GeneratedProtocolMessageType('TransformationInput', (_message.Message,), {
  'DESCRIPTOR' : _TRANSFORMATIONINPUT,
  '__module__' : 'tecton_proto.args.transformation_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.TransformationInput)
  })
_sym_db.RegisterMessage(TransformationInput)

RequestContext = _reflection.GeneratedProtocolMessageType('RequestContext', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCONTEXT,
  '__module__' : 'tecton_proto.args.transformation_pb2'
  # @@protoc_insertion_point(class_scope:tecton_proto.args.RequestContext)
  })
_sym_db.RegisterMessage(RequestContext)


DESCRIPTOR._options = None
_TRANSFORMATIONINPUT.fields_by_name['transformation_name']._options = None
_TRANSFORMATIONINPUT.fields_by_name['vds_name']._options = None
# @@protoc_insertion_point(module_scope)

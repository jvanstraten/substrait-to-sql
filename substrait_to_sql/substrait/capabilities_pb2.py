# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: substrait/capabilities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="substrait/capabilities.proto",
    package="substrait",
    syntax="proto3",
    serialized_options=b"\n\022io.substrait.protoP\001\252\002\022Substrait.Protobuf",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b"\n\x1csubstrait/capabilities.proto\x12\tsubstrait\"\xfb\x01\n\x0c\x43\x61pabilities\x12\x1a\n\x12substrait_versions\x18\x01 \x03(\t\x12$\n\x1c\x61\x64vanced_extension_type_urls\x18\x02 \x03(\t\x12\x42\n\x11simple_extensions\x18\x03 \x03(\x0b\x32'.substrait.Capabilities.SimpleExtension\x1a\x65\n\x0fSimpleExtension\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x15\n\rfunction_keys\x18\x02 \x03(\t\x12\x11\n\ttype_keys\x18\x03 \x03(\t\x12\x1b\n\x13type_variation_keys\x18\x04 \x03(\tB+\n\x12io.substrait.protoP\x01\xaa\x02\x12Substrait.Protobufb\x06proto3",
)


_CAPABILITIES_SIMPLEEXTENSION = _descriptor.Descriptor(
    name="SimpleExtension",
    full_name="substrait.Capabilities.SimpleExtension",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="uri",
            full_name="substrait.Capabilities.SimpleExtension.uri",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="function_keys",
            full_name="substrait.Capabilities.SimpleExtension.function_keys",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="type_keys",
            full_name="substrait.Capabilities.SimpleExtension.type_keys",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="type_variation_keys",
            full_name="substrait.Capabilities.SimpleExtension.type_variation_keys",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=194,
    serialized_end=295,
)

_CAPABILITIES = _descriptor.Descriptor(
    name="Capabilities",
    full_name="substrait.Capabilities",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="substrait_versions",
            full_name="substrait.Capabilities.substrait_versions",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="advanced_extension_type_urls",
            full_name="substrait.Capabilities.advanced_extension_type_urls",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="simple_extensions",
            full_name="substrait.Capabilities.simple_extensions",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[
        _CAPABILITIES_SIMPLEEXTENSION,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=44,
    serialized_end=295,
)

_CAPABILITIES_SIMPLEEXTENSION.containing_type = _CAPABILITIES
_CAPABILITIES.fields_by_name[
    "simple_extensions"
].message_type = _CAPABILITIES_SIMPLEEXTENSION
DESCRIPTOR.message_types_by_name["Capabilities"] = _CAPABILITIES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Capabilities = _reflection.GeneratedProtocolMessageType(
    "Capabilities",
    (_message.Message,),
    {
        "SimpleExtension": _reflection.GeneratedProtocolMessageType(
            "SimpleExtension",
            (_message.Message,),
            {
                "DESCRIPTOR": _CAPABILITIES_SIMPLEEXTENSION,
                "__module__": "substrait.capabilities_pb2"
                # @@protoc_insertion_point(class_scope:substrait.Capabilities.SimpleExtension)
            },
        ),
        "DESCRIPTOR": _CAPABILITIES,
        "__module__": "substrait.capabilities_pb2"
        # @@protoc_insertion_point(class_scope:substrait.Capabilities)
    },
)
_sym_db.RegisterMessage(Capabilities)
_sym_db.RegisterMessage(Capabilities.SimpleExtension)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)

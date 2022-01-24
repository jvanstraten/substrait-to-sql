# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: substrait/extensions/extensions.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="substrait/extensions/extensions.proto",
    package="substrait.extensions",
    syntax="proto3",
    serialized_options=b"\n\022io.substrait.protoP\001\252\002\022Substrait.Protobuf",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n%substrait/extensions/extensions.proto\x12\x14substrait.extensions\x1a\x19google/protobuf/any.proto"?\n\x12SimpleExtensionURI\x12\x1c\n\x14\x65xtension_uri_anchor\x18\x01 \x01(\r\x12\x0b\n\x03uri\x18\x02 \x01(\t"\xef\x04\n\x1aSimpleExtensionDeclaration\x12X\n\x0e\x65xtension_type\x18\x01 \x01(\x0b\x32>.substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeH\x00\x12k\n\x18\x65xtension_type_variation\x18\x02 \x01(\x0b\x32G.substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariationH\x00\x12`\n\x12\x65xtension_function\x18\x03 \x01(\x0b\x32\x42.substrait.extensions.SimpleExtensionDeclaration.ExtensionFunctionH\x00\x1aS\n\rExtensionType\x12\x1f\n\x17\x65xtension_uri_reference\x18\x01 \x01(\r\x12\x13\n\x0btype_anchor\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a\x66\n\x16\x45xtensionTypeVariation\x12\x1f\n\x17\x65xtension_uri_reference\x18\x01 \x01(\r\x12\x1d\n\x15type_variation_anchor\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\t\x1a[\n\x11\x45xtensionFunction\x12\x1f\n\x17\x65xtension_uri_reference\x18\x01 \x01(\r\x12\x17\n\x0f\x66unction_anchor\x18\x02 \x01(\r\x12\x0c\n\x04name\x18\x03 \x01(\tB\x0e\n\x0cmapping_type"j\n\x11\x41\x64vancedExtension\x12*\n\x0coptimization\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\x12)\n\x0b\x65nhancement\x18\x02 \x01(\x0b\x32\x14.google.protobuf.AnyB+\n\x12io.substrait.protoP\x01\xaa\x02\x12Substrait.Protobufb\x06proto3',
    dependencies=[
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)


_SIMPLEEXTENSIONURI = _descriptor.Descriptor(
    name="SimpleExtensionURI",
    full_name="substrait.extensions.SimpleExtensionURI",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="extension_uri_anchor",
            full_name="substrait.extensions.SimpleExtensionURI.extension_uri_anchor",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="uri",
            full_name="substrait.extensions.SimpleExtensionURI.uri",
            index=1,
            number=2,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=90,
    serialized_end=153,
)


_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE = _descriptor.Descriptor(
    name="ExtensionType",
    full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionType",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="extension_uri_reference",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionType.extension_uri_reference",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="type_anchor",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionType.type_anchor",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="name",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionType.name",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=483,
    serialized_end=566,
)

_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION = _descriptor.Descriptor(
    name="ExtensionTypeVariation",
    full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariation",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="extension_uri_reference",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariation.extension_uri_reference",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="type_variation_anchor",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariation.type_variation_anchor",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="name",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariation.name",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=568,
    serialized_end=670,
)

_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION = _descriptor.Descriptor(
    name="ExtensionFunction",
    full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="extension_uri_reference",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.extension_uri_reference",
            index=0,
            number=1,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="function_anchor",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.function_anchor",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
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
            name="name",
            full_name="substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction.name",
            index=2,
            number=3,
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
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=672,
    serialized_end=763,
)

_SIMPLEEXTENSIONDECLARATION = _descriptor.Descriptor(
    name="SimpleExtensionDeclaration",
    full_name="substrait.extensions.SimpleExtensionDeclaration",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="extension_type",
            full_name="substrait.extensions.SimpleExtensionDeclaration.extension_type",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="extension_type_variation",
            full_name="substrait.extensions.SimpleExtensionDeclaration.extension_type_variation",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="extension_function",
            full_name="substrait.extensions.SimpleExtensionDeclaration.extension_function",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
        _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE,
        _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION,
        _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION,
    ],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[
        _descriptor.OneofDescriptor(
            name="mapping_type",
            full_name="substrait.extensions.SimpleExtensionDeclaration.mapping_type",
            index=0,
            containing_type=None,
            create_key=_descriptor._internal_create_key,
            fields=[],
        ),
    ],
    serialized_start=156,
    serialized_end=779,
)


_ADVANCEDEXTENSION = _descriptor.Descriptor(
    name="AdvancedExtension",
    full_name="substrait.extensions.AdvancedExtension",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="optimization",
            full_name="substrait.extensions.AdvancedExtension.optimization",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
            name="enhancement",
            full_name="substrait.extensions.AdvancedExtension.enhancement",
            index=1,
            number=2,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
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
    serialized_start=781,
    serialized_end=887,
)

_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE.containing_type = _SIMPLEEXTENSIONDECLARATION
_SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION.containing_type = (
    _SIMPLEEXTENSIONDECLARATION
)
_SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION.containing_type = (
    _SIMPLEEXTENSIONDECLARATION
)
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_type"
].message_type = _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_type_variation"
].message_type = _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_function"
].message_type = _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION
_SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"].fields.append(
    _SIMPLEEXTENSIONDECLARATION.fields_by_name["extension_type"]
)
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_type"
].containing_oneof = _SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"]
_SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"].fields.append(
    _SIMPLEEXTENSIONDECLARATION.fields_by_name["extension_type_variation"]
)
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_type_variation"
].containing_oneof = _SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"]
_SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"].fields.append(
    _SIMPLEEXTENSIONDECLARATION.fields_by_name["extension_function"]
)
_SIMPLEEXTENSIONDECLARATION.fields_by_name[
    "extension_function"
].containing_oneof = _SIMPLEEXTENSIONDECLARATION.oneofs_by_name["mapping_type"]
_ADVANCEDEXTENSION.fields_by_name[
    "optimization"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ADVANCEDEXTENSION.fields_by_name[
    "enhancement"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name["SimpleExtensionURI"] = _SIMPLEEXTENSIONURI
DESCRIPTOR.message_types_by_name[
    "SimpleExtensionDeclaration"
] = _SIMPLEEXTENSIONDECLARATION
DESCRIPTOR.message_types_by_name["AdvancedExtension"] = _ADVANCEDEXTENSION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleExtensionURI = _reflection.GeneratedProtocolMessageType(
    "SimpleExtensionURI",
    (_message.Message,),
    {
        "DESCRIPTOR": _SIMPLEEXTENSIONURI,
        "__module__": "substrait.extensions.extensions_pb2"
        # @@protoc_insertion_point(class_scope:substrait.extensions.SimpleExtensionURI)
    },
)
_sym_db.RegisterMessage(SimpleExtensionURI)

SimpleExtensionDeclaration = _reflection.GeneratedProtocolMessageType(
    "SimpleExtensionDeclaration",
    (_message.Message,),
    {
        "ExtensionType": _reflection.GeneratedProtocolMessageType(
            "ExtensionType",
            (_message.Message,),
            {
                "DESCRIPTOR": _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPE,
                "__module__": "substrait.extensions.extensions_pb2"
                # @@protoc_insertion_point(class_scope:substrait.extensions.SimpleExtensionDeclaration.ExtensionType)
            },
        ),
        "ExtensionTypeVariation": _reflection.GeneratedProtocolMessageType(
            "ExtensionTypeVariation",
            (_message.Message,),
            {
                "DESCRIPTOR": _SIMPLEEXTENSIONDECLARATION_EXTENSIONTYPEVARIATION,
                "__module__": "substrait.extensions.extensions_pb2"
                # @@protoc_insertion_point(class_scope:substrait.extensions.SimpleExtensionDeclaration.ExtensionTypeVariation)
            },
        ),
        "ExtensionFunction": _reflection.GeneratedProtocolMessageType(
            "ExtensionFunction",
            (_message.Message,),
            {
                "DESCRIPTOR": _SIMPLEEXTENSIONDECLARATION_EXTENSIONFUNCTION,
                "__module__": "substrait.extensions.extensions_pb2"
                # @@protoc_insertion_point(class_scope:substrait.extensions.SimpleExtensionDeclaration.ExtensionFunction)
            },
        ),
        "DESCRIPTOR": _SIMPLEEXTENSIONDECLARATION,
        "__module__": "substrait.extensions.extensions_pb2"
        # @@protoc_insertion_point(class_scope:substrait.extensions.SimpleExtensionDeclaration)
    },
)
_sym_db.RegisterMessage(SimpleExtensionDeclaration)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionType)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionTypeVariation)
_sym_db.RegisterMessage(SimpleExtensionDeclaration.ExtensionFunction)

AdvancedExtension = _reflection.GeneratedProtocolMessageType(
    "AdvancedExtension",
    (_message.Message,),
    {
        "DESCRIPTOR": _ADVANCEDEXTENSION,
        "__module__": "substrait.extensions.extensions_pb2"
        # @@protoc_insertion_point(class_scope:substrait.extensions.AdvancedExtension)
    },
)
_sym_db.RegisterMessage(AdvancedExtension)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
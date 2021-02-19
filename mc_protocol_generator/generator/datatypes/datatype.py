from . import (Angle, Array, Bool, Byte, Chat, Compound, Double,
    EntityMetadata, Float, Identifier, Int, Long, NBT, Option, Position,
    Short, Slot, String, Switch, UByte, UShort, UUID, VarInt, VarLong)

integer_types = {Byte, UByte, Short, UShort, Int, Long, VarInt, VarLong}

float_types = {Float, Double}

number_types = integer_types | float_types

bool_types = {Bool}

string_types = {Chat, Identifier, String}

angle_types = {Angle}

metadata_types = {EntityMetadata, NBT, Slot}

position_types = {Position}

id_types = {UUID}

value_types = (
    number_types | bool_types | string_types | angle_types | metadata_types
    | position_types | id_types
)

collection_types = {Array}

compound_types = {Compound}

option_types = {Option}

switch_types = {Switch}

complex_types = collection_types | compound_types | option_types | switch_types

all_types = value_types | complex_types
Module(
    body=[
        Import(names=[alias(name='datatype_length', asname='dl')]),
        ClassDef(
            name='Compound',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self'), arg(arg='string'), arg(arg='int')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='string', ctx=Store()
                                )
                            ],
                            value=Name(id='string', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='int', ctx=Store()
                                )
                            ],
                            value=Name(id='int', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='__len__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Name(id='dl', ctx=Load()),
                                        attr='string_size',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='string',
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='dl', ctx=Load()), attr='int_size', ctx=Load()
                                ),
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='__repr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='Compound(string='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='string',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', int='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='string',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=')'),
                                ]
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='write_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self'), arg(arg='writer')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='string', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_int',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='int', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='read_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='reader')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='string', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_string',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='int', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()), attr='read_int', ctx=Load()
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='Compound', ctx=Load()),
                                args=[Name(id='string', ctx=Load()), Name(id='int', ctx=Load())],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='AllTypesPacket',
            bases=[],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='name', ctx=Store())], value=Constant(value='All Types Packet')
                ),
                Assign(targets=[Name(id='id', ctx=Store())], value=Constant(value=1)),
                Assign(targets=[Name(id='state', ctx=Store())], value=Constant(value='play')),
                Assign(targets=[Name(id='bound_to', ctx=Store())], value=Constant(value='client')),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self'),
                            arg(arg='angle'),
                            arg(arg='array'),
                            arg(arg='bool'),
                            arg(arg='byte'),
                            arg(arg='chat'),
                            arg(arg='compound'),
                            arg(arg='double'),
                            arg(arg='entity_metadata'),
                            arg(arg='float'),
                            arg(arg='identifier'),
                            arg(arg='int'),
                            arg(arg='long'),
                            arg(arg='nbt'),
                            arg(arg='option'),
                            arg(arg='position'),
                            arg(arg='short'),
                            arg(arg='slot'),
                            arg(arg='string'),
                            arg(arg='switch_value'),
                            arg(arg='switch_short'),
                            arg(arg='switch_long'),
                            arg(arg='switch_int'),
                            arg(arg='ubyte'),
                            arg(arg='ushort'),
                            arg(arg='uuid'),
                            arg(arg='varint'),
                            arg(arg='varlong'),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='angle', ctx=Store()
                                )
                            ],
                            value=Name(id='angle', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='array', ctx=Store()
                                )
                            ],
                            value=Name(id='array', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='bool', ctx=Store()
                                )
                            ],
                            value=Name(id='bool', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='byte', ctx=Store()
                                )
                            ],
                            value=Name(id='byte', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='chat', ctx=Store()
                                )
                            ],
                            value=Name(id='chat', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='compound', ctx=Store()
                                )
                            ],
                            value=Name(id='compound', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='double', ctx=Store()
                                )
                            ],
                            value=Name(id='double', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='entity_metadata',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='entity_metadata', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='float', ctx=Store()
                                )
                            ],
                            value=Name(id='float', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='identifier',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='identifier', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='int', ctx=Store()
                                )
                            ],
                            value=Name(id='int', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='long', ctx=Store()
                                )
                            ],
                            value=Name(id='long', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='nbt', ctx=Store()
                                )
                            ],
                            value=Name(id='nbt', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='option', ctx=Store()
                                )
                            ],
                            value=Name(id='option', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='position', ctx=Store()
                                )
                            ],
                            value=Name(id='position', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='short', ctx=Store()
                                )
                            ],
                            value=Name(id='short', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='slot', ctx=Store()
                                )
                            ],
                            value=Name(id='slot', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='string', ctx=Store()
                                )
                            ],
                            value=Name(id='string', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='switch_value',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='switch_value', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='switch_short',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='switch_short', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='switch_long',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='switch_long', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='switch_int',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='switch_int', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='ubyte', ctx=Store()
                                )
                            ],
                            value=Name(id='ubyte', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='ushort', ctx=Store()
                                )
                            ],
                            value=Name(id='ushort', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='uuid', ctx=Store()
                                )
                            ],
                            value=Name(id='uuid', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='varint', ctx=Store()
                                )
                            ],
                            value=Name(id='varint', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='varlong', ctx=Store()
                                )
                            ],
                            value=Name(id='varlong', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='__len__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=BinOp(
                                left=BinOp(
                                    left=BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=BinOp(
                                                    left=BinOp(
                                                        left=BinOp(
                                                            left=BinOp(
                                                                left=BinOp(
                                                                    left=BinOp(
                                                                        left=BinOp(
                                                                            left=BinOp(
                                                                                left=BinOp(
                                                                                    left=BinOp(
                                                                                        left=BinOp(
                                                                                            left=BinOp(
                                                                                                left=BinOp(
                                                                                                    left=BinOp(
                                                                                                        left=BinOp(
                                                                                                            left=BinOp(
                                                                                                                left=BinOp(
                                                                                                                    left=BinOp(
                                                                                                                        left=BinOp(
                                                                                                                            left=BinOp(
                                                                                                                                left=Call(
                                                                                                                                    func=Attribute(
                                                                                                                                        value=Name(
                                                                                                                                            id='dl',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        attr='varint_size',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    args=[
                                                                                                                                        Attribute(
                                                                                                                                            value=Name(
                                                                                                                                                id='AllTypesPacket',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            attr='id',
                                                                                                                                            ctx=Load(),
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                    keywords=[],
                                                                                                                                ),
                                                                                                                                op=Add(),
                                                                                                                                right=Attribute(
                                                                                                                                    value=Name(
                                                                                                                                        id='dl',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    attr='angle_size',
                                                                                                                                    ctx=Load(),
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                            op=Add(),
                                                                                                                            right=BinOp(
                                                                                                                                left=Call(
                                                                                                                                    func=Attribute(
                                                                                                                                        value=Name(
                                                                                                                                            id='dl',
                                                                                                                                            ctx=Load(),
                                                                                                                                        ),
                                                                                                                                        attr='varint_size',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    args=[
                                                                                                                                        Call(
                                                                                                                                            func=Name(
                                                                                                                                                id='len',
                                                                                                                                                ctx=Load(),
                                                                                                                                            ),
                                                                                                                                            args=[
                                                                                                                                                Attribute(
                                                                                                                                                    value=Name(
                                                                                                                                                        id='self',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    attr='array',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                )
                                                                                                                                            ],
                                                                                                                                            keywords=[],
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                    keywords=[],
                                                                                                                                ),
                                                                                                                                op=Add(),
                                                                                                                                right=Call(
                                                                                                                                    func=Name(
                                                                                                                                        id='sum',
                                                                                                                                        ctx=Load(),
                                                                                                                                    ),
                                                                                                                                    args=[
                                                                                                                                        GeneratorExp(
                                                                                                                                            elt=Call(
                                                                                                                                                func=Attribute(
                                                                                                                                                    value=Name(
                                                                                                                                                        id='dl',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    attr='string_size',
                                                                                                                                                    ctx=Load(),
                                                                                                                                                ),
                                                                                                                                                args=[
                                                                                                                                                    Name(
                                                                                                                                                        id='item',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    )
                                                                                                                                                ],
                                                                                                                                                keywords=[],
                                                                                                                                            ),
                                                                                                                                            generators=[
                                                                                                                                                comprehension(
                                                                                                                                                    target=Name(
                                                                                                                                                        id='item',
                                                                                                                                                        ctx=Store(),
                                                                                                                                                    ),
                                                                                                                                                    iter=Attribute(
                                                                                                                                                        value=Name(
                                                                                                                                                            id='self',
                                                                                                                                                            ctx=Load(),
                                                                                                                                                        ),
                                                                                                                                                        attr='array',
                                                                                                                                                        ctx=Load(),
                                                                                                                                                    ),
                                                                                                                                                    ifs=[],
                                                                                                                                                    is_async=0,
                                                                                                                                                )
                                                                                                                                            ],
                                                                                                                                        )
                                                                                                                                    ],
                                                                                                                                    keywords=[],
                                                                                                                                ),
                                                                                                                            ),
                                                                                                                        ),
                                                                                                                        op=Add(),
                                                                                                                        right=Attribute(
                                                                                                                            value=Name(
                                                                                                                                id='dl',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            attr='bool_size',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                    ),
                                                                                                                    op=Add(),
                                                                                                                    right=Attribute(
                                                                                                                        value=Name(
                                                                                                                            id='dl',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='byte_size',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                ),
                                                                                                                op=Add(),
                                                                                                                right=Call(
                                                                                                                    func=Attribute(
                                                                                                                        value=Name(
                                                                                                                            id='dl',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='chat_size',
                                                                                                                        ctx=Load(),
                                                                                                                    ),
                                                                                                                    args=[
                                                                                                                        Attribute(
                                                                                                                            value=Name(
                                                                                                                                id='self',
                                                                                                                                ctx=Load(),
                                                                                                                            ),
                                                                                                                            attr='chat',
                                                                                                                            ctx=Load(),
                                                                                                                        )
                                                                                                                    ],
                                                                                                                    keywords=[],
                                                                                                                ),
                                                                                                            ),
                                                                                                            op=Add(),
                                                                                                            right=Call(
                                                                                                                func=Name(
                                                                                                                    id='len',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[
                                                                                                                    Attribute(
                                                                                                                        value=Name(
                                                                                                                            id='self',
                                                                                                                            ctx=Load(),
                                                                                                                        ),
                                                                                                                        attr='compound',
                                                                                                                        ctx=Load(),
                                                                                                                    )
                                                                                                                ],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ),
                                                                                                        op=Add(),
                                                                                                        right=Attribute(
                                                                                                            value=Name(
                                                                                                                id='dl',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='double_size',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    op=Add(),
                                                                                                    right=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(
                                                                                                                id='dl',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            attr='entity_metadata_size',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Attribute(
                                                                                                                value=Name(
                                                                                                                    id='self',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                attr='entity_metadata',
                                                                                                                ctx=Load(),
                                                                                                            )
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                                op=Add(),
                                                                                                right=Attribute(
                                                                                                    value=Name(
                                                                                                        id='dl',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='float_size',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            op=Add(),
                                                                                            right=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(
                                                                                                        id='dl',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='identifier_size',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[
                                                                                                    Attribute(
                                                                                                        value=Name(
                                                                                                            id='self',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='identifier',
                                                                                                        ctx=Load(),
                                                                                                    )
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ),
                                                                                        op=Add(),
                                                                                        right=Attribute(
                                                                                            value=Name(
                                                                                                id='dl',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='int_size',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                    ),
                                                                                    op=Add(),
                                                                                    right=Attribute(
                                                                                        value=Name(
                                                                                            id='dl',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='long_size',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ),
                                                                                op=Add(),
                                                                                right=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(
                                                                                            id='dl',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='nbt_size',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[
                                                                                        Attribute(
                                                                                            value=Name(
                                                                                                id='self',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            attr='nbt',
                                                                                            ctx=Load(),
                                                                                        )
                                                                                    ],
                                                                                    keywords=[],
                                                                                ),
                                                                            ),
                                                                            op=Add(),
                                                                            right=IfExp(
                                                                                test=Compare(
                                                                                    left=Attribute(
                                                                                        value=Name(
                                                                                            id='self',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='option',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    ops=[Eq()],
                                                                                    comparators=[
                                                                                        Constant(
                                                                                            value=None
                                                                                        )
                                                                                    ],
                                                                                ),
                                                                                body=Constant(
                                                                                    value=0
                                                                                ),
                                                                                orelse=Attribute(
                                                                                    value=Name(
                                                                                        id='dl',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='int_size',
                                                                                    ctx=Load(),
                                                                                ),
                                                                            ),
                                                                        ),
                                                                        op=Add(),
                                                                        right=Attribute(
                                                                            value=Name(
                                                                                id='dl', ctx=Load()
                                                                            ),
                                                                            attr='position_size',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Attribute(
                                                                        value=Name(
                                                                            id='dl', ctx=Load()
                                                                        ),
                                                                        attr='short_size',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                op=Add(),
                                                                right=Call(
                                                                    func=Attribute(
                                                                        value=Name(
                                                                            id='dl', ctx=Load()
                                                                        ),
                                                                        attr='slot_size',
                                                                        ctx=Load(),
                                                                    ),
                                                                    args=[
                                                                        Attribute(
                                                                            value=Name(
                                                                                id='self',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='slot',
                                                                            ctx=Load(),
                                                                        )
                                                                    ],
                                                                    keywords=[],
                                                                ),
                                                            ),
                                                            op=Add(),
                                                            right=Call(
                                                                func=Attribute(
                                                                    value=Name(id='dl', ctx=Load()),
                                                                    attr='string_size',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(
                                                                            id='self', ctx=Load()
                                                                        ),
                                                                        attr='string',
                                                                        ctx=Load(),
                                                                    )
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        op=Add(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='dl', ctx=Load()),
                                                                attr='varint_size',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Attribute(
                                                                    value=Name(
                                                                        id='self', ctx=Load()
                                                                    ),
                                                                    attr='switch_value',
                                                                    ctx=Load(),
                                                                )
                                                            ],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    op=Add(),
                                                    right=IfExp(
                                                        test=Compare(
                                                            left=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='switch_value',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value=0)],
                                                        ),
                                                        body=Attribute(
                                                            value=Name(id='dl', ctx=Load()),
                                                            attr='short_size',
                                                            ctx=Load(),
                                                        ),
                                                        orelse=IfExp(
                                                            test=Compare(
                                                                left=Attribute(
                                                                    value=Name(
                                                                        id='self', ctx=Load()
                                                                    ),
                                                                    attr='switch_value',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Constant(value=1)],
                                                            ),
                                                            body=BinOp(
                                                                left=Attribute(
                                                                    value=Name(id='dl', ctx=Load()),
                                                                    attr='long_size',
                                                                    ctx=Load(),
                                                                ),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Name(id='dl', ctx=Load()),
                                                                    attr='int_size',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            orelse=Constant(value=0),
                                                        ),
                                                    ),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='dl', ctx=Load()),
                                                    attr='ubyte_size',
                                                    ctx=Load(),
                                                ),
                                            ),
                                            op=Add(),
                                            right=Attribute(
                                                value=Name(id='dl', ctx=Load()),
                                                attr='ushort_size',
                                                ctx=Load(),
                                            ),
                                        ),
                                        op=Add(),
                                        right=Attribute(
                                            value=Name(id='dl', ctx=Load()),
                                            attr='uuid_size',
                                            ctx=Load(),
                                        ),
                                    ),
                                    op=Add(),
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='dl', ctx=Load()),
                                            attr='varint_size',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='varint',
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                op=Add(),
                                right=Call(
                                    func=Attribute(
                                        value=Name(id='dl', ctx=Load()),
                                        attr='varlong_size',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='varlong',
                                            ctx=Load(),
                                        )
                                    ],
                                    keywords=[],
                                ),
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='__repr__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=JoinedStr(
                                values=[
                                    Constant(value='ComplexPacket(angle='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='angle',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', array='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='array',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', bool='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='bool',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', byte='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='byte',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', chat='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='chat',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', compound='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='compound',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', double='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='double',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', entity_metadata='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='entity_metadata',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', float='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='float',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', identifier='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='identifier',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', int='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='int',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', long='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='long',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', nbt='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='nbt',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', option='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='option',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', position='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='position',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', short='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='short',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', slot='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='slot',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', string='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='string',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', switch_value='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='switch_value',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', switch_short='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='switch_short',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', switch_long='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='switch_long',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', switch_int='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='switch_int',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', ubyte='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ubyte',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', ushort='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ushort',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', uuid='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='uuid',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', varint='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='varint',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', varlong='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='varlong',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=')'),
                                ]
                            )
                        )
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='write_packet',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self'), arg(arg='writer')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_varint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='AllTypesPacket', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_angle',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='angle', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_varint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='len', ctx=Load()),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='array',
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()), attr='array', ctx=Load()
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='write_string',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='item', ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_bool',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='bool', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_byte',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='byte', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_chat',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='chat', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='compound',
                                        ctx=Load(),
                                    ),
                                    attr='write_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='writer', ctx=Load())],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_double',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='double', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_entity_metadata',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='entity_metadata',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_float',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='float', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_identifier',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='identifier',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_int',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='int', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_long',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='long', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_nbt',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='nbt', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Assign(
                            targets=[Name(id='option_check', ctx=Store())],
                            value=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()), attr='option', ctx=Load()
                                ),
                                ops=[NotEq()],
                                comparators=[Constant(value=None)],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_bool',
                                    ctx=Load(),
                                ),
                                args=[Name(id='option_check', ctx=Load())],
                                keywords=[],
                            )
                        ),
                        If(
                            test=Name(id='option_check', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='write_int',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='option',
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_position',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='position',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_short',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='short', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_slot',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='slot', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='string', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_varint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='switch_value',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='switch_value',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=0)],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='write_short',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='switch_short',
                                                ctx=Load(),
                                            )
                                        ],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='switch_value',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='write_long',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='switch_long',
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            )
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='writer', ctx=Load()),
                                                    attr='write_int',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='switch_int',
                                                        ctx=Load(),
                                                    )
                                                ],
                                                keywords=[],
                                            )
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='switch_value',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value=2)],
                                            ),
                                            body=[Pass()],
                                            orelse=[],
                                        )
                                    ],
                                )
                            ],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_ubyte',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='ubyte', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_ushort',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='ushort', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_uuid',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='uuid', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_varint',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()), attr='varint', ctx=Load()
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='writer', ctx=Load()),
                                    attr='write_varlong',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='varlong',
                                        ctx=Load(),
                                    )
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[],
                ),
                FunctionDef(
                    name='read_packet',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='reader')],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='angle', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_angle',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='array', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='reader', ctx=Load()),
                                        attr='read_string',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='_', ctx=Store()),
                                        iter=Call(
                                            func=Name(id='range', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Attribute(
                                                        value=Name(id='reader', ctx=Load()),
                                                        attr='read_varint',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    )
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='bool', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_bool',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='byte', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_byte',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='chat', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_chat',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='compound', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='Compound', ctx=Load()),
                                    attr='read_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='reader', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='double', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_double',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='entity_metadata', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_entity_metadata',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='float', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_float',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='identifier', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_identifier',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='int', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()), attr='read_int', ctx=Load()
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='long', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_long',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='nbt', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()), attr='read_nbt', ctx=Load()
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='option', ctx=Store())],
                            value=IfExp(
                                test=Call(
                                    func=Attribute(
                                        value=Name(id='reader', ctx=Load()),
                                        attr='read_bool',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='reader', ctx=Load()),
                                        attr='read_int',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                orelse=Constant(value=None),
                            ),
                        ),
                        Assign(
                            targets=[Name(id='position', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_position',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='short', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_short',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='slot', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_slot',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='string', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_string',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='switch_value', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_varint',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='switch_value', ctx=Load()),
                                ops=[Eq()],
                                comparators=[Constant(value=0)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='switch_short', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='reader', ctx=Load()),
                                            attr='read_short',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                                Assign(
                                    targets=[Name(id='switch_long', ctx=Store())],
                                    value=Constant(value=None),
                                ),
                                Assign(
                                    targets=[Name(id='switch_int', ctx=Store())],
                                    value=Constant(value=None),
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Compare(
                                        left=Name(id='switch_value', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value=1)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='switch_short', ctx=Store())],
                                            value=Constant(value=None),
                                        ),
                                        Assign(
                                            targets=[Name(id='switch_long', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='reader', ctx=Load()),
                                                    attr='read_long',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                        Assign(
                                            targets=[Name(id='switch_int', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='reader', ctx=Load()),
                                                    attr='read_int',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                )
                            ],
                        ),
                        Assign(
                            targets=[Name(id='ubyte', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_ubyte',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='ushort', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_ushort',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='uuid', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_uuid',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='varint', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_varint',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='varlong', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()),
                                    attr='read_varlong',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='AllTypesPacket', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(arg='angle', value=Name(id='angle', ctx=Load())),
                                    keyword(arg='array', value=Name(id='array', ctx=Load())),
                                    keyword(arg='bool', value=Name(id='bool', ctx=Load())),
                                    keyword(arg='byte', value=Name(id='byte', ctx=Load())),
                                    keyword(arg='chat', value=Name(id='chat', ctx=Load())),
                                    keyword(arg='compound', value=Name(id='compound', ctx=Load())),
                                    keyword(arg='double', value=Name(id='double', ctx=Load())),
                                    keyword(
                                        arg='entity_metadata',
                                        value=Name(id='entity_metadata', ctx=Load()),
                                    ),
                                    keyword(arg='float', value=Name(id='float', ctx=Load())),
                                    keyword(
                                        arg='identifier', value=Name(id='identifier', ctx=Load())
                                    ),
                                    keyword(arg='int', value=Name(id='int', ctx=Load())),
                                    keyword(arg='long', value=Name(id='long', ctx=Load())),
                                    keyword(arg='nbt', value=Name(id='nbt', ctx=Load())),
                                    keyword(arg='option', value=Name(id='option', ctx=Load())),
                                    keyword(arg='position', value=Name(id='position', ctx=Load())),
                                    keyword(arg='short', value=Name(id='short', ctx=Load())),
                                    keyword(arg='slot', value=Name(id='slot', ctx=Load())),
                                    keyword(arg='string', value=Name(id='string', ctx=Load())),
                                    keyword(
                                        arg='switch_value',
                                        value=Name(id='switch_value', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='switch_short',
                                        value=Name(id='switch_short', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='switch_long', value=Name(id='switch_long', ctx=Load())
                                    ),
                                    keyword(
                                        arg='switch_int', value=Name(id='switch_int', ctx=Load())
                                    ),
                                    keyword(arg='ubyte', value=Name(id='ubyte', ctx=Load())),
                                    keyword(arg='ushort', value=Name(id='ushort', ctx=Load())),
                                    keyword(arg='uuid', value=Name(id='uuid', ctx=Load())),
                                    keyword(arg='varint', value=Name(id='varint', ctx=Load())),
                                    keyword(arg='varlong', value=Name(id='varlong', ctx=Load())),
                                ],
                            )
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)

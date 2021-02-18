Module(
    body=[
        ClassDef(
            name='SimplePacket',
            bases=[],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='name', ctx=Store())], value=Constant(value='Simple Packet')
                ),
                Assign(targets=[Name(id='id', ctx=Store())], value=Constant(value=0)),
                Assign(targets=[Name(id='state', ctx=Store())], value=Constant(value='play')),
                Assign(targets=[Name(id='bound_to', ctx=Store())], value=Constant(value='server')),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self'),
                            arg(arg='int1'),
                            arg(arg='str1'),
                            arg(arg='varint1'),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='int1', ctx=Store()
                                )
                            ],
                            value=Name(id='int1', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='str1', ctx=Store()
                                )
                            ],
                            value=Name(id='str1', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='varint1', ctx=Store()
                                )
                            ],
                            value=Name(id='varint1', ctx=Load()),
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
                                    left=Attribute(
                                        value=Name(id='dl', ctx=Load()), attr='int_size', ctx=Load()
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
                                                value=Name(id='self', ctx=Load()),
                                                attr='str1',
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
                                            value=Name(id='self', ctx=Load()),
                                            attr='varint1',
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
                                    Constant(value='SimplePacket(int1='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='int1',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', str1='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='str1',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', varint1='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='varint1',
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
                                        value=Name(id='self', ctx=Load()), attr='id', ctx=Load()
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
                                        value=Name(id='self', ctx=Load()), attr='int1', ctx=Load()
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
                                        value=Name(id='self', ctx=Load()), attr='str1', ctx=Load()
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
                                        attr='varint1',
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
                            targets=[Name(id='int1', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='reader', ctx=Load()), attr='read_int', ctx=Load()
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='str1', ctx=Store())],
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
                            targets=[Name(id='varint1', ctx=Store())],
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
                        Return(
                            value=Call(
                                func=Name(id='SimplePacket', ctx=Load()),
                                args=[
                                    Name(id='int1', ctx=Load()),
                                    Name(id='str1', ctx=Load()),
                                    Name(id='varint1', ctx=Load()),
                                ],
                                keywords=[],
                            )
                        ),
                    ],
                    decorator_list=[Name(id='staticmethod', ctx=Load())],
                ),
            ],
            decorator_list=[],
        )
    ],
    type_ignores=[],
)

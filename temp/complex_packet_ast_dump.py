Module(
    body=[
        Import(names=[alias(name='datatype_length', asname='dl')]),
        ClassDef(
            name='ArrayCompItem',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self'), arg(arg='string'), arg(arg='int_val')],
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
                                    value=Name(id='self', ctx=Load()), attr='int_val', ctx=Store()
                                )
                            ],
                            value=Name(id='int_val', ctx=Load()),
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
                                    Constant(value='ArrayCompItem(string='),
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
                                    Constant(value=', int_val='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='int_val',
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
                                        value=Name(id='self', ctx=Load()),
                                        attr='int_val',
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
                            targets=[Name(id='int_val', ctx=Store())],
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
                                func=Name(id='ArrayCompItem', ctx=Load()),
                                args=[
                                    Name(id='string', ctx=Load()),
                                    Name(id='int_val', ctx=Load()),
                                ],
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
            name='CompoundVar',
            bases=[],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self'),
                            arg(arg='string'),
                            arg(arg='varlong'),
                            arg(arg='short'),
                        ],
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
                                    value=Name(id='self', ctx=Load()), attr='varlong', ctx=Store()
                                )
                            ],
                            value=Name(id='varlong', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='short', ctx=Store()
                                )
                            ],
                            value=Name(id='short', ctx=Load()),
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
                                    right=Call(
                                        func=Attribute(
                                            value=Name(id='dl', ctx=Load()),
                                            attr='varlong',
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
                                ),
                                op=Add(),
                                right=Attribute(
                                    value=Name(id='dl', ctx=Load()), attr='short_size', ctx=Load()
                                ),
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
                        Return(
                            value=Call(
                                func=Name(id='CompoundVar', ctx=Load()),
                                args=[
                                    Name(id='string', ctx=Load()),
                                    Name(id='varlong', ctx=Load()),
                                    Name(id='short', ctx=Load()),
                                ],
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
            name='ComplexPacket',
            bases=[],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='name', ctx=Store())], value=Constant(value='Complex Packet')
                ),
                Assign(targets=[Name(id='id', ctx=Store())], value=Constant(value=1)),
                Assign(targets=[Name(id='state', ctx=Store())], value=Constant(value='play')),
                Assign(targets=[Name(id='bound_to', ctx=Store())], value=Constant(value='server')),
                FunctionDef(
                    name='__init__',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self'),
                            arg(arg='array_comp'),
                            arg(arg='array_int'),
                            arg(arg='array_varint'),
                            arg(arg='compound_var'),
                        ],
                        kwonlyargs=[],
                        kw_defaults=[],
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='array_comp',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='array_comp', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()), attr='array_int', ctx=Store()
                                )
                            ],
                            value=Name(id='array_int', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='array_varint',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='array_varint', ctx=Load()),
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='compound_var',
                                    ctx=Store(),
                                )
                            ],
                            value=Name(id='compound_var', ctx=Load()),
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
                                        left=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Call(
                                                        func=Name(id='len', ctx=Load()),
                                                        args=[Name(id='item', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='item', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='array_comp',
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
                                        op=Add(),
                                        right=Call(
                                            func=Name(id='sum', ctx=Load()),
                                            args=[
                                                GeneratorExp(
                                                    elt=Attribute(
                                                        value=Name(id='dl', ctx=Load()),
                                                        attr='int_size',
                                                        ctx=Load(),
                                                    ),
                                                    generators=[
                                                        comprehension(
                                                            target=Name(id='item', ctx=Store()),
                                                            iter=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='array_int',
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
                                    op=Add(),
                                    right=Call(
                                        func=Name(id='sum', ctx=Load()),
                                        args=[
                                            GeneratorExp(
                                                elt=Call(
                                                    func=Attribute(
                                                        value=Name(id='dl', ctx=Load()),
                                                        attr='varint_size',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='item', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                generators=[
                                                    comprehension(
                                                        target=Name(id='item', ctx=Store()),
                                                        iter=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='array_varint',
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
                                op=Add(),
                                right=Call(
                                    func=Name(id='len', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='compound_var',
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
                                    Constant(value='ComplexPacket(array_comp='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='array_comp',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', array_int='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='array_int',
                                                    ctx=Load(),
                                                )
                                            ],
                                            keywords=[],
                                        ),
                                        conversion=-1,
                                    ),
                                    Constant(value=', array_varint='),
                                    FormattedValue(
                                        value=Call(
                                            func=Name(id='repr', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='array_varint',
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
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()), attr='array_comp', ctx=Load()
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='item', ctx=Load()),
                                            attr='write_data',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='writer', ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()), attr='array_int', ctx=Load()
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='write_int',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='item', ctx=Load())],
                                        keywords=[],
                                    )
                                )
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='item', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='self', ctx=Load()), attr='array_varint', ctx=Load()
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='writer', ctx=Load()),
                                            attr='write_varint',
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
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='compound_var',
                                        ctx=Load(),
                                    ),
                                    attr='write_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='writer', ctx=Load())],
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
                            targets=[Name(id='array_comp', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='ArrayCompItem', ctx=Load()),
                                        attr='read_data',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='reader', ctx=Load())],
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
                            targets=[Name(id='array_int', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='reader', ctx=Load()),
                                        attr='read_int',
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
                            targets=[Name(id='array_varint', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Attribute(
                                        value=Name(id='reader', ctx=Load()),
                                        attr='read_varint',
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
                            targets=[Name(id='compound_var', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='CompoundVar', ctx=Load()),
                                    attr='read_data',
                                    ctx=Load(),
                                ),
                                args=[Name(id='reader', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Name(id='ComplexPacket', ctx=Load()),
                                args=[
                                    Name(id='array_comp', ctx=Load()),
                                    Name(id='array_int', ctx=Load()),
                                    Name(id='array_varint', ctx=Load()),
                                    Name(id='compound_var', ctx=Load()),
                                ],
                                keywords=[],
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

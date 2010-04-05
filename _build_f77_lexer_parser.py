import ply.lex as lex
import ply.yacc as yacc
import edit_descriptors

def _build_f77_lexer_parser():
    # == Build a lexer ==
    # Define a category of tokens here
    tokens = (
        'H_EDIT_DESCRIPTOR',
        'OPEN_PARENS',
        'CLOSE_PARENS',
        'SEPERATOR',
        'REPEATABLE_EDIT_DESCRIPTOR',
        'NON_REPEATABLE_EDIT_DESCRIPTOR',
        'NUMBER',
        'DOT',
        'STRING_LITERAL',
    )
    # Define what each category of tokens contains
    print 'g'
    t_H_EDIT_DESCRIPTOR = r'97[Hh].{97}|96[Hh].{96}|95[Hh].{95}|94[Hh].{94}|93[Hh].{93}|92[Hh].{92}|91[Hh].{91}|90[Hh].{90}|89[Hh].{89}|88[Hh].{88}|87[Hh].{87}|86[Hh].{86}|85[Hh].{85}|84[Hh].{84}|83[Hh].{83}|82[Hh].{82}|81[Hh].{81}|80[Hh].{80}|79[Hh].{79}|78[Hh].{78}|77[Hh].{77}|76[Hh].{76}|75[Hh].{75}|74[Hh].{74}|73[Hh].{73}|72[Hh].{72}|71[Hh].{71}|70[Hh].{70}|69[Hh].{69}|68[Hh].{68}|67[Hh].{67}|66[Hh].{66}|65[Hh].{65}|64[Hh].{64}|63[Hh].{63}|62[Hh].{62}|61[Hh].{61}|60[Hh].{60}|59[Hh].{59}|58[Hh].{58}|57[Hh].{57}|56[Hh].{56}|55[Hh].{55}|54[Hh].{54}|53[Hh].{53}|52[Hh].{52}|51[Hh].{51}|50[Hh].{50}|49[Hh].{49}|48[Hh].{48}|47[Hh].{47}|46[Hh].{46}|45[Hh].{45}|44[Hh].{44}|43[Hh].{43}|42[Hh].{42}|41[Hh].{41}|40[Hh].{40}|39[Hh].{39}|38[Hh].{38}|37[Hh].{37}|36[Hh].{36}|35[Hh].{35}|34[Hh].{34}|33[Hh].{33}|32[Hh].{32}|31[Hh].{31}|30[Hh].{30}|29[Hh].{29}|28[Hh].{28}|27[Hh].{27}|26[Hh].{26}|25[Hh].{25}|24[Hh].{24}|23[Hh].{23}|22[Hh].{22}|21[Hh].{21}|20[Hh].{20}|19[Hh].{19}|18[Hh].{18}|17[Hh].{17}|16[Hh].{16}|15[Hh].{15}|14[Hh].{14}|13[Hh].{13}|12[Hh].{12}|11[Hh].{11}|10[Hh].{10}|9[Hh].{9}|8[Hh].{8}|7[Hh].{7}|6[Hh].{6}|5[Hh].{5}|4[Hh].{4}|3[Hh].{3}|2[Hh].{2}|1[Hh].{1}|0[Hh].{0}'
    t_OPEN_PARENS = r'\('
    t_CLOSE_PARENS = r'\)'
    t_SEPERATOR = r','
    t_REPEATABLE_EDIT_DESCRIPTOR = r'[IFEDGLA]'
    t_NON_REPEATABLE_EDIT_DESCRIPTOR = r'TR|TL|SP|SS|BN|BZ|[XTSP/:]'
    def t_NUMBER(t):
        r'-?\d+'
        t.value = int(t.value)
        return t
    t_DOT = r'\.'
    t_STRING_LITERAL = r"'(''|[^'])*'"
    # Define which characters to be ignored
    t_ignore = ' \t'
    # Define what to do if a non-parseable sequence is found
    def t_error(t):
        raise TypeError('')
    # Create the lexer
    lexer = lex.lex()
##     lex.input(format)
##     for tok in iter(lex.token, None):
##         print tok.type, tok.value
        
    def p_subformat(p):
        'format : OPEN_PARENS edit_descriptors CLOSE_PARENS'
        p[0] = p[2]

    # == Now build the parser ==
    def p_repeated_subformat(p):
        'edit_descriptors : NUMBER OPEN_PARENS edit_descriptors CLOSE_PARENS'
        p[0] = p[1]*p[3]

    def p_edit_descriptors(p):
        'edit_descriptors : edit_descriptor edit_descriptors'
        p[0] = [p[1]] + p[2]

    def p_edit_descriptors_empty(p):
        'edit_descriptors : empty'
        p[0] = []

    def p_empty(p):
        'empty :'
        pass

    def p_non_repeatable_edit_descriptor(p):
        '''
        edit_descriptor : NON_REPEATABLE_EDIT_DESCRIPTOR
        edit_descriptor : H_EDIT_DESCRIPTOR
        edit_descriptor : NON_REPEATABLE_EDIT_DESCRIPTOR NUMBER 
        edit_descriptor : NUMBER NON_REPEATABLE_EDIT_DESCRIPTOR
        edit_descriptor : STRING_LITERAL
        '''
        if len(p) == 2:
            if p[1] == '/':
                p[0] = edit_descriptors.Slash()
            elif p[1] == ':':
                p[0] = edit_descriptors.Colon()
            elif p[1] == 'S':
                p[0] = edit_descriptors.S()
            elif p[1] == 'SP':
                p[0] = edit_descriptors.SP()
            elif p[1] == 'SS':
                p[0] = edit_descriptors.SS()
            elif p[1] == 'BN':
                p[0] = edit_descriptors.BN()
            elif p[1] == 'BZ':
                p[0] = edit_descriptors.BZ()
            elif p[1].type == 'STRING_LITERAL':
                p[0] = edit_descriptors.StringLiteral()
                p[0].char_string = p[0][1:-1]
            elif p[1].type == 'H_EDIT_DESCRIPTOR':
                p[0] = edit_descriptor.H()
                p[0].num_chars = None
                p[0].char_string = None
            else:
                raise SyntaxError()
        elif (len(p) == 3) and isinstance(p[1], int):
            if p[2] == 'P':
                p[0] = edit_descriptors.P()
                p[0].scale = p[1]
            elif p[2] == 'X':
                p[0] = edit_descriptors.X()
                p[1].num_chars = p[1]
            elif p[2] == 'H':
                # TODO: This needs to be parsed differently
                p[0] = edit_descriptors.H()
                p[0].num_chars = p[1]
            else:
                raise SyntaxError()
        elif (len(p) == 3) and isinstance(p[2], int):
            if p[1] == 'T':
                p[0] = edit_descriptors.T()
                p[0].num_chars = p[2]
            elif p[1] == 'TL':
                p[0] = edit_descriptors.TL()
                p[0].num_chars = p[2]
            elif p[1] == 'TR':
                p[0] = edit_descriptors.TR()
                p[0].num_chars = p[2]
            else:
                raise SyntaxError()
        else:
            raise SyntaxError()


    def p_repeatable_edit_descriptor(p):
        '''
        edit_descriptor : REPEATABLE_EDIT_DESCRIPTOR
        edit_descriptor : REPEATABLE_EDIT_DESCRIPTOR NUMBER 
        edit_descriptor : REPEATABLE_EDIT_DESCRIPTOR NUMBER DOT NUMBER
        edit_descriptor : REPEATABLE_EDIT_DESCRIPTOR NUMBER DOT NUMBER REPEATABLE_EDIT_DESCRIPTOR NUMBER
        '''
        if len(p) == 2:
            if p[1] == 'A':
                p[0] = edit_descriptors.A()
                p[0].repeat = 1
            else:
                raise SyntaxError()
        if len(p) == 3:
            if p[1] == 'I':
                p[0] == edit_descriptors.I()
                p[0].repeat = 1
                p[0].width = p[2]
            elif p[1] == 'L':
                p[0] == edit_descriptors.L()
                p[0].repeat = 1
                p[0].width = p[2]
            elif p[1] == 'A':
                p[0] == edit_descriptors.A()
                p[0].repeat = 1
                p[0].width = p[2]
            else:
                raise SyntaxError()
        if len(p) == 5:
            if p[1] == 'I':
                p[0] == edit_descriptors.I()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].padding = p[4]
            elif p[1] == 'F':
                p[0] == edit_descriptors.F()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
            elif p[1] == 'E':
                p[0] == edit_descriptors.E()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
            elif p[1] == 'D':
                p[0] == edit_descriptors.D()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
            elif p[1] == 'G':
                p[0] == edit_descriptors.G()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
            else:
                raise SyntaxError()
        if len(p) == 7:
            if p[1] == p[5] == 'E':
                p[0] == edit_descriptors.E()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
                p[0].exponent = p[6]
            elif (p[1] == 'G') and (p[5] == 'E'):
                p[0] == edit_descriptors.G()
                p[0].repeat = 1
                p[0].width = p[2]
                p[0].decimal_places = p[4]
                p[0].exponent = p[6]
            else:
                raise SyntaxError()
        else:
            raise SyntaxError()

    def p_repeated_repeatable_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REPEATABLE_EDIT_DESCRIPTOR
        edit_descriptor : NUMBER REPEATABLE_EDIT_DESCRIPTOR NUMBER 
        edit_descriptor : NUMBER REPEATABLE_EDIT_DESCRIPTOR NUMBER DOT NUMBER
        edit_descriptor : NUMBER REPEATABLE_EDIT_DESCRIPTOR NUMBER DOT NUMBER REPEATABLE_EDIT_DESCRIPTOR NUMBER
        '''
        if len(p) == 3:
            if p[2] == 'A':
                p[0] = edit_descriptors.A()
                p[0].repeat = p[1]
            else:
                raise SyntaxError()
        if len(p) == 4:
            if p[2] == 'I':
                p[0] == edit_descriptors.I()
                p[0].repeat = p[1]
                p[0].width = p[3]
            elif p[2] == 'L':
                p[0] == edit_descriptors.L()
                p[0].repeat = p[1]
                p[0].width = p[3]
            elif p[2] == 'A':
                p[0] == edit_descriptors.A()
                p[0].repeat = p[1]
                p[0].width = p[3]
            else:
                raise SyntaxError()
        if len(p) == 6:
            if p[2] == 'I':
                p[0] == edit_descriptors.I()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].padding = p[5]
            elif p[2] == 'F':
                p[0] == edit_descriptors.F()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
            elif p[2] == 'E':
                p[0] == edit_descriptors.E()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
            elif p[2] == 'D':
                p[0] == edit_descriptors.D()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
            elif p[2] == 'G':
                p[0] == edit_descriptors.G()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
            else:
                raise SyntaxError()
        if len(p) == 8:
            if p[2] == p[6] == 'E':
                p[0] == edit_descriptors.E()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
                p[0].exponent = p[7]
            elif (p[2] == 'G') and (p[6] == 'E'):
                p[0] == edit_descriptors.G()
                p[0].repeat = p[1]
                p[0].width = p[3]
                p[0].decimal_places = p[5]
                p[0].exponent = p[7]
            else:
                raise SyntaxError()
        else:
            raise SyntaxError()

    def p_error(p):
        print "Syntax error at '%s'" % p.value

    # == Compile the parser ==
    parser = yacc.yacc()
    # == Return the lexer/parser
    return (lexer, parser)

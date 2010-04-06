import ply.lex as lex
import ply.yacc as yacc
from edit_descriptors import *
import re

def _build_f77_lexer_parser():
    # == Build a lexer ==
    # Define a category of tokens here
    tokens = (
        'OPEN_PARENS',
        'CLOSE_PARENS',
        'SEPERATOR',
        'EDITDESC',
        'PREFIXED_EDITDESC',
        'SUFFIXED_EDITDESC',
        'REP_SUFFIXED_EDITDESC',
        'REP_SUFFIXED_DOT_EDITDESC',
        'REP_OPT_SUFFIXED_EDITDESC',
        'REP_SUFFIXED_OPT_DOT_EDITDESC',
        'REP_SUFFIXED_DOT_OPT_EXP_EDITDESC',
        'NUMBER',
        'DOT',
        'STRING_LITERAL',
        'H_EDIT_DESCRIPTOR',
    )
    # Define what each category of tokens contains
    # Functions are matched depending on the order they are defined

    # This is a hack - see http://stackoverflow.com/questions/2216843/
    def t_H_EDIT_DESCRIPTOR(t):
        r'97[Hh].{97}|96[Hh].{96}|95[Hh].{95}|94[Hh].{94}|93[Hh].{93}|92[Hh].{92}|91[Hh].{91}|90[Hh].{90}|89[Hh].{89}|88[Hh].{88}|87[Hh].{87}|86[Hh].{86}|85[Hh].{85}|84[Hh].{84}|83[Hh].{83}|82[Hh].{82}|81[Hh].{81}|80[Hh].{80}|79[Hh].{79}|78[Hh].{78}|77[Hh].{77}|76[Hh].{76}|75[Hh].{75}|74[Hh].{74}|73[Hh].{73}|72[Hh].{72}|71[Hh].{71}|70[Hh].{70}|69[Hh].{69}|68[Hh].{68}|67[Hh].{67}|66[Hh].{66}|65[Hh].{65}|64[Hh].{64}|63[Hh].{63}|62[Hh].{62}|61[Hh].{61}|60[Hh].{60}|59[Hh].{59}|58[Hh].{58}|57[Hh].{57}|56[Hh].{56}|55[Hh].{55}|54[Hh].{54}|53[Hh].{53}|52[Hh].{52}|51[Hh].{51}|50[Hh].{50}|49[Hh].{49}|48[Hh].{48}|47[Hh].{47}|46[Hh].{46}|45[Hh].{45}|44[Hh].{44}|43[Hh].{43}|42[Hh].{42}|41[Hh].{41}|40[Hh].{40}|39[Hh].{39}|38[Hh].{38}|37[Hh].{37}|36[Hh].{36}|35[Hh].{35}|34[Hh].{34}|33[Hh].{33}|32[Hh].{32}|31[Hh].{31}|30[Hh].{30}|29[Hh].{29}|28[Hh].{28}|27[Hh].{27}|26[Hh].{26}|25[Hh].{25}|24[Hh].{24}|23[Hh].{23}|22[Hh].{22}|21[Hh].{21}|20[Hh].{20}|19[Hh].{19}|18[Hh].{18}|17[Hh].{17}|16[Hh].{16}|15[Hh].{15}|14[Hh].{14}|13[Hh].{13}|12[Hh].{12}|11[Hh].{11}|10[Hh].{10}|9[Hh].{9}|8[Hh].{8}|7[Hh].{7}|6[Hh].{6}|5[Hh].{5}|4[Hh].{4}|3[Hh].{3}|2[Hh].{2}|1[Hh].{1}|0[Hh].{0}'
        matches = re.search(r'(\d+)[Hh](.*)', t.value)
        t.value = matches.group(2)
        return t
    def t_NUMBER(t):
        r'-?\d+'
        t.value = int(t.value)
        return t
    # Regexes strings are matched with longest first
    t_EDITDESC = r'SP|SS|BN|BZ|[S:/]'
    t_PREFIXED_EDITDESC = r'X|P'
    t_SUFFIXED_EDITDESC = r'T|TL|TR'
    t_REP_SUFFIXED_EDITDESC = 'L'
    t_REP_SUFFIXED_DOT_EDITDESC = 'F|D'
    t_REP_OPT_SUFFIXED_EDITDESC = 'A'
    t_REP_SUFFIXED_OPT_DOT_EDITDESC = 'I'
    t_REP_SUFFIXED_DOT_OPT_EXP_EDITDESC = 'E|G'
    t_STRING_LITERAL = r"'(''|[^'])*'"
    t_OPEN_PARENS = r'\('
    t_CLOSE_PARENS = r'\)'
    t_DOT = r'\.'
    t_SEPERATOR = r','
    # Define which characters to be ignored
    t_ignore = ' \t'
    # Define what to do if a non-parseable sequence is found
    def t_error(t):
        raise TypeError('')
    # Create the lexer
    lexer = lex.lex(reflags=re.IGNORECASE)
        

    # == Now build the parser ==

    def p_combine_formats(p):
        '''
        format : format format
        '''
        p[0] = p[1] + p[2]
    
    def p_subformat(p):
        'format : OPEN_PARENS format CLOSE_PARENS'
        p[0] = p[2]

    def p_repeated_format(p):
        '''
        format : NUMBER OPEN_PARENS format CLOSE_PARENS
        '''
        p[0] = p[1]*p[3]


    def p_format(p):
        '''
        format : edit_descriptors
        '''
        p[0] = p[1]


    def p_edit_descriptors(p):
        'edit_descriptors : edit_descriptors edit_descriptor'
        p[0] = p[1] + [p[2]]

    def p_separators(p):
        '''
        edit_descriptors : edit_descriptors SEPERATOR
        '''
        p[0] = p[1]

    def p_gen_edit_descriptors(p):
        'edit_descriptors : edit_descriptor'
        p[0] = [p[1]]

    def p_rep_suffixed_dot_opt_exp_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER DOT NUMBER REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER
                        | NUMBER REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER DOT NUMBER
                        | REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER DOT NUMBER REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER
                        | REP_SUFFIXED_DOT_OPT_EXP_EDITDESC NUMBER DOT NUMBER
        '''
        if len(p) == 8:
            # Has repeat, #.# and exp#
            if p[6].upper() != 'E':
                raise SyntaxError("Exponents needs to be specified with 'E'")
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
            p[0].decimal_places = p[5]
            p[0].exponent = p[7]
        if len(p) == 7:
            # No repeat, #.# and exp#
            if p[5].upper() != 'E':
                raise SyntaxError("Exponents needs to be specified with 'E'")
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]
            p[0].decimal_places = p[4]
            p[0].exponent = p[6]
        if len(p) == 6:
            # Has repeat and #.#
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
            p[0].decimal_places = p[5]
        if len(p) == 5:
            # Has no repeat and #.#
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]
            p[0].decimal_places = p[4]

    def p_rep_suffixed_opt_dot_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REP_SUFFIXED_OPT_DOT_EDITDESC NUMBER DOT NUMBER
                        | NUMBER REP_SUFFIXED_OPT_DOT_EDITDESC NUMBER
                        | REP_SUFFIXED_OPT_DOT_EDITDESC NUMBER DOT NUMBER
                        | REP_SUFFIXED_OPT_DOT_EDITDESC NUMBER
        '''
        if len(p) == 6:
            # Has repeat and #.#
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
            p[0].padding = p[5]
        if len(p) == 5:
            # No repeat and #.#
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]
            p[0].padding = p[4]
        if len(p) == 4:
            # Has repeat and #
            p[0] = get_token(p[2])
            p[0].repeat = p[1] 
            p[0].width = p[3]
        if len(p) == 3:
            # Has no repeat and #
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]


    def p_rep_opt_suffixed_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REP_OPT_SUFFIXED_EDITDESC NUMBER
                        | NUMBER REP_OPT_SUFFIXED_EDITDESC
                        | REP_OPT_SUFFIXED_EDITDESC NUMBER
                        | REP_OPT_SUFFIXED_EDITDESC
        '''
        if len(p) == 4:
            # Has repeat and width
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
        if len(p) == 3:
            if type(p[1]) == int:
                # Has repeat only
                p[0] = get_token(p[2])
                p[0].repeat = p[1]
            else:
                # Has width only
                p[0] = get_token(p[1])
                p[0].repeat = 1
                p[0].width = p[2]
        if len(p) == 2:
            # Has neither repeat nor width
            p[0].repeat = 1


    def p_rep_suffixed_dot_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REP_SUFFIXED_DOT_EDITDESC NUMBER DOT NUMBER
                        | REP_SUFFIXED_DOT_EDITDESC NUMBER DOT NUMBER
        '''
        if len(p) == 6:
            # Has repeat
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
            p[0].decimal_places = p[5]
        elif len(p) == 5:
            # No repeat, set to 1
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]
            p[0].decimal_places = p[4]
        else:
            raise SyntaxError()

    def p_rep_suffixed_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER REP_SUFFIXED_EDITDESC NUMBER
                        | REP_SUFFIXED_EDITDESC NUMBER
        '''
        if len(p) == 4:
            # Has repeat
            p[0] = get_token(p[2])
            p[0].repeat = p[1]
            p[0].width = p[3]
        elif len(p) == 3:
            # No repeat, set to 1
            p[0] = get_token(p[1])
            p[0].repeat = 1
            p[0].width = p[2]
        else:
            raise SyntaxError()

    def p_suffixed_edit_descriptor(p):
        '''
        edit_descriptor : SUFFIXED_EDITDESC NUMBER
        '''
        p[0] = get_token(p[1])
        p[0].num_chars = p[2]

    def p_prefixed_edit_descriptor(p):
        '''
        edit_descriptor : NUMBER PREFIXED_EDITDESC
        '''
        if p[2] == 'X':
            p[0] = X()
            p[0].num_chars = p[1]
        elif p[2] == 'P':
            p[0] = P()
            p[0].scale = p[1]

    def p_edit_descriptor(p):
        '''
        edit_descriptor : EDITDESC
        '''
        p[0] = get_token(p[1])

    def p_string_literal(p):
        '''
        edit_descriptor : STRING_LITERAL
        '''
        p[0] = p[1][1:-1]

    def p_h_edit_descriptor(p):
        '''
        edit_descriptor : H_EDIT_DESCRIPTOR
        '''
        p[0] = H()
        p[0].char_string = p[1]
        p[0].width = len(p[1])

    def p_error(p):
        print "Syntax error at '%s'" % p.value

    # == Compile the parser ==
    parser = yacc.yacc()
    # == Return the lexer/parser
    return (lexer, parser)


def get_token(name):
    name = name.upper()
    if name == 'A':
        return A()
    elif name == 'BN':
        return BN()
    elif name == 'BZ':
        return BZ()
    elif name == ':':
        return Colon()
    elif name == 'D':
        return D()
    elif name == 'E':
        return E()
    elif name == 'F':
        return F()
    elif name == 'G':
        return G()
    elif name == 'H':
        return H()
    elif name == 'I':
        return I()
    elif name == 'L':
        return L()
    elif name == 'P':
        return P()
    elif name =='S':
        return S()
    elif name == '/':
        return Slash()
    elif name == 'SP':
        return SP()
    elif name == 'SS':
        return SS()
    elif name == 'T':
        return T()
    elif name == 'TL':
        return TL()
    elif name == 'TR':
        return TR()
    elif name == 'X':
        return X()
    else:
        return None



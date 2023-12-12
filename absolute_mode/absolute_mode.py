import turtle
import re

def opener(code_file):
    '''
    code_file is the text document where the G-code is stored, you may have to 
    specify the path.
    '''
    assert type(code_file) == str, 'enter valid path'
    fp = open(code_file, 'r')
    code = fp.readlines()
    fp.close()
    return code

file_path = 'C:\\Users\\hello\\OneDrive\\Desktop\\G-code.txt' # enter the G-code file path here
code_list = opener(file_path)

def cleaner(code_list):
    '''
    returns a list that contains the texts with seperated values while also
    deleting the codes that will not be required for visualisation
    
    example:
        G0Z0.1 --> delete
        G0X0.8276Y3.8621 --> (G0, X = '0.8276', Y = '3.8621')
    '''
    
    assert type(code_list) == list, 'make sure the code is in a list format'
    
    valid_definitions = [
        'G0', 'G1', 'G2', 'G3', 'G21', 'G20', 'G90', 'G91', 'G90',
        'G94', 'G53', 'G54']
    
    # the first element of the code_list will consist of definitions, we parse it and take those that we need
    
    header = [i for i in code_list[0].split(' ') if i in valid_definitions]
    new_code_list = [header]
    invalid_letters = 'ZFS'
    for code in code_list[1:]:
        # if code has a Z, F, S, N one letter codes, then remove it
        if any(char in code for char in invalid_letters):
            code_list.remove(code)
        else: # if code looks like G0X0.8276Y3.8621
            pattern = re.compile(r'([A-Z][0-9.]+)')
            result = pattern.findall(code)
            new_code_list.append(result)
    return new_code_list

codes = cleaner(code_list)

def standard_scale(numstr):
    assert type(numstr) == str
    return (float(numstr))*2

def absolute_mode(codes):
    '''
    starting coordinates are (-400, -150)
    '''

    for i in codes[1:]:
        print(i)
        try:
            if i[0] == 'G0' or i[0] == 'G00':
                turtle.penup()
                turtle.goto(standard_scale(i[1][1:]), standard_scale(i[2][1:]))
                turtle.pendown()
            elif i[0] == 'G1' or i[0] == 'G01':
                turtle.goto(standard_scale(i[1][1:]), standard_scale(i[2][1:]))
            elif i[0][0] == 'N':
                turtle.goto(standard_scale(i[1][1:]), standard_scale(i[2][1:]))
        
        except IndexError:
            if i[0] == 'G0' or i[0] == 'G00':
                turtle.penup()
                if i[1].startswith('X-'):
                    turtle.back(standard_scale(i[1][1:]))
                elif i[1].startswith('X'):
                    turtle.forward(standard_scale(i[1][1:]))
                elif i[1].startswith('Y-'):
                    turtle.right(90)
                    turtle.forward(standard_scale(i[1][1:]))
                elif i[1].startswith('Y'):
                    turtle.left(90)
                    turtle.forward(standard_scale(i[1][1:]))
            
            elif i[0] == 'G1' or i[0] == 'G01':
                turtle.pendown()
                if i[1].startswith('X-'):
                    turtle.back(standard_scale(i[1][1:]))
                elif i[1].startswith('X'):
                    turtle.forward(standard_scale(i[1][1:]))
                elif i[1].startswith('Y-'):
                    turtle.right(90)
                    turtle.forward(standard_scale(i[1][1:]))
                elif i[1].startswith('Y'):
                    turtle.left(90)
                    turtle.forward(standard_scale(i[1][1:]))
            


def turtle_set_up(codes):
    '''
    I've defined a canvas (2048,600), to avoid bind and terminator issues the RUNNING parameter is manually set to true.
    
    '''
    
    screen = turtle.Screen()
    screen.title('G-code visualisation')
    screen.setup(width = 2048, height = 600) # width is the x-axis and height is the y-axis
    
    turtle.TurtleScreen._RUNNING = True
    turtle.speed(0)
    turtle.pensize(1)
    
    turtle.penup()
    turtle.setx(-1000)
    turtle.sety(-150)
    turtle.pendown()

    incremental(codes)
    
    screen.exitonclick()

turtle_set_up(codes)




def repeater(interfunction):
    i = 0L;
    while i <= 3:
        if i != 2:
            try:
                interfunction();
            except:
                pass;
        else:
            interfunction();
        i += 1;
            
@repeater
def hello():
    print 'Hello!';
    raise Exception;



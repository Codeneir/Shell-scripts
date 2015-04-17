def repeater(interfunction):
    i = 0L;
    for i in [1,2,3]:
        if i != 3:
            try:
                interfunction();
            except:
                pass;
        else:
            interfunction();
            
@repeater
def hello():
    print 'Hello!';
    raise Exception;



def repeater(interfunction):
    try:
        interfunction();
    except Exception:
        try:
            interfunction();
        except Exception:
            interfunction();
                
@repeater
def hello():
    print 'Hello!';
    raise Exception;



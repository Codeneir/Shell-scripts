def notify(interfunction):
    def catcher():
        for i in range(2):
            try:
                interfunction();
            except:
                pass;
        else:
            interfunction();
    return catcher();
    

@notify
def helloer():
    print 'hello!';
    raise Exception;

helloer();  

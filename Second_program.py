def notify(interfunction):
    def catcher():
        for i in range(3):
            if i != 3:
                try:
                    interfunction();
                except:
                    pass
    return catcher();

@notify
def halloer():
    print 'hello!';
    Exception;

halloer();              

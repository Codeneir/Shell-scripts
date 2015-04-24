#!/usr/bin/python
# coding: utf8
import logging;
import optparse;
import os;
import paramiko;
import progressbar;
import subprocess;
import sys;
import time;


logging.basicConfig( level = logging.DEBUG );

logging.info( u'Checking just has started' );
#bar = progressbar.ProgressBar().start()

#for timestep in xrange(100):
#    bar.update(timestep);
time.sleep(1);    	

current_system = sys.platform
if ( sys.platform != 'linux2' and sys.platform != 'linux3' ):
    print 'Current system: ' + current_system;
    print 'Type of your system is not supported';
    raise SystemExit( 0 );
else:
    print 'Current system: ' + current_system;
logging.info( u'Checking has finished successfully' );

parser = optparse.OptionParser( version ='0.1', description = 'Education script which installs Apache server locally or by using SSH' );

parser.add_option( '-l','--local', action = 'store_const',
	 	   const = 'local', dest = 'mode',
		   help = 'Install the Apache server locally' );

parser.add_option( '-s','--ssh', action = 'store',
		   nargs = 3, dest = 'mode',
		   type = 'str',
                   help = 'Install the Apache server by using ssh
			     -s <servername> <username> <password>' );   

( options, args ) = parser.parse_args( );

logging.debug( type(options.mode) );
if options.mode is str: logging.debug( u'Parsing result=' + options.mode );
mode = options.mode;

if options.mode == 'local':
    logging.info( u'Local mode has selected' );
    logging.info( u'Starting installation..' );
    installation_result = subprocess.call( 'apt-get install Apache2',
                                           shell = True );
    if not installation_result:
        logging.info( u'There are no errors after installatioin' );
#elif options.mode is tuple:
elif len(options.mode) == 3:
    logging.info( u'ssh mode has selected' );
    logging.info( u'Starting ssh...' );
    time.sleep(1);
    ssh = paramiko.SSHClient( );
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy( ) );
#   ssh.set_missing_host_key_policy(paramiko.RejectPolicy( ) );
    try:
	connection_result = ssh.connect( options.mode(1),
		                         username = options.mode(2),
		                         password = options.mode(3) );
	logging.debug( connection_result );
    except:
	logging.info( u'Something goes wrong while connecting throw ssh...' );
	logging.debug( connection_result );  
        raise SystemExit( 1 );
    
    stdinput,stdoutput,stderror = ssh.exec_command( 'apt-get install Apache2' );    			

else:
    print 'Wrong format of input options atguments';



# os.system('cat /etc/network/interfaces');



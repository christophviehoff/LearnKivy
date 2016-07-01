import json
import warnings
from pprint import pprint
import configparser
'''
# using a json file to read and store configuration data
# filter warnings, load the configuration
warnings.filterwarnings("ignore")
conf = json.load(open('conf.json'))

pprint(conf)

#accessing individual elements
print (conf['resolution'])
print (conf["use_dropbox"])
print (conf["camera_warmup_time"])
'''

#using configparser to read a ini file
config = configparser.ConfigParser()

'''#creates the file and writes data to it.:
config['Default']={'use_dropbox':'false'}
config['Camera']={'show_video':'true',
        'use_dropbox':'true',
        'dropbox_key':'YOUR_DROPBOX_KEY',
        'dropbox_secret':'YOUR_DROPBOX_SECRET',
        'dropbox_base_path':'YOUR_DROPBOX_PATH',
        'min_upload_seconds':'3.0',
        'min_motion_frames':'8',
        'camera_warmup_time':'2.5',
        'delta_thresh':'5',
        'resolution':'[640, 480]',
        'fps':'16',
        'min_area':'5000'}

with open('cfg_Camera.ini', 'w') as configfile:
    config.write(configfile)
'''

#read form the existing file
config.read('cfg_Camera.ini')
#available sections in the file
print ('the configuration file has the following sections: {}'.format(config.sections()))

#access parameters
dropbox=config['Default']['use_dropbox']
print (dropbox)
dropbox=config['Camera']['use_dropbox']
print (dropbox)

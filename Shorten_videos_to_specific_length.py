import os
import pandas as pd
from configparser import ConfigParser

config = ConfigParser()
configFile = r"Z:\DeepLabCut\DLC_extract\New_082119\project_folder\project_config.ini"
config.read(configFile)
csv_dir = config.get('General settings', 'csv_path')
csv_dir_in = os.path.join(csv_dir, 'outlier_corrected_movement_location')
use_master = config.get('General settings', 'use_master_config')
filesFound = []
configFilelist = []

########### FIND CSV FILES ###########
if use_master == 'yes':
    for i in os.listdir(csv_dir_in):
        if i.__contains__(".csv"):
            fname = os.path.join(csv_dir_in, i)
            filesFound.append(fname)
if use_master == 'no':
    config_folder_path = config.get('General settings', 'config_folder')
    for i in os.listdir(config_folder_path):
        if i.__contains__(".ini"):
            configFilelist.append(os.path.join(config_folder_path, i))
            iniVidName = i.split(".")[0]
            csv_fn = iniVidName + '.csv'
            file = os.path.join(csv_dir_in, csv_fn)
            filesFound.append(file)

for i in filesFound:
    currentFile = i
    csv_df = pd.read_csv(currentFile)
    new_df = csv_df.head(9300)
    new_df = new_df.loc[:, ~new_df.columns.str.contains('^Unnamed')]
    new_df.to_csv(currentFile, index=False)



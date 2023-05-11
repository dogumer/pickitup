import os
import shutil

def is_folder_existing(folder_path):
	return os.path.isdir(folder_path)

def create_folder(folder_path):
	os.makedirs(folder_path)

def move_file(source_path,target_path):
	shutil.move(source_path,target_path)
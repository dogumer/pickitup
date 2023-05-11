import os
import json

json_file = "extensions.json"

def json_data(file_name):
	with open(file_name) as file:
		return json.load(file)


def extension_of_file(file_name):
	return os.path.splitext(file_name)[1][1:]


def type_of_extension(extension,dictionary):
	return dictionary[extension][0] if extension in dictionary else None


def by_type(files):
	global json_file
	dictionary = json_data(json_file)

	files_by_types = {}

	for file in files:
		file_extension = extension_of_file(file)
		file_type = type_of_extension(file_extension,dictionary)

		if file_extension and file_type:
			files_by_types[file] = file_type

	return files_by_types
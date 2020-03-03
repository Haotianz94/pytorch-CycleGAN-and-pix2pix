import os
import shutil

source_dir = 'test_latest/images' 
target_dir = 'fake_B'
os.makedirs(target_dir, exist_ok=True)

for file in os.listdir(source_dir):
	if 'fake_B' in file:
		shutil.move('{}/{}'.format(source_dir, file), '{}/{}'.format(target_dir, file))

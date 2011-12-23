import subprocess
import os

# use pdftohtml to convert into pdf
# one time script, maybe move to download as we download it?
def convert_to_html():
    cur_dir = os.path.abspath(os.path.curdir)
	html_path = os.path.join(cur_dir,'html/')
	pdf_dir = os.path.join(cur_dir,'files/')
	pdf_content = os.listdir(pdf_dir)
	
	for content in pdf_content:
	    dir_name = content.split('/')[0]
		new_path = os.path.join(html_path,dir_name)
		os.mkdir(new_path)
		os.chdir(new_path)
		pdf_path = os.path.join(pdf_dir,content)
		cmd = ['pdftohtml','-c',pdf_path,dir_name]
		result = subprocess.call(cmd)
		os.chdir(cur_dir)
		
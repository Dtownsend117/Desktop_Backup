import os
import shutil
def copy_desktop_contents(destination_folder, exclusions=None):
   
    if exclusions is None:
        exclusions = []
    
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop") # Gets the path for the desktop
    
    os.makedirs(destination_folder, exist_ok=True) # Checks the destination location
    
    for item in os.listdir(desktop_path):
        item_path = os.path.join(desktop_path, item)
        
        if item in exclusions: # This check for files/folders in the exclusions list
            print(f"Excluding: {item}")
            continue
        
        try:
            if os.path.isdir(item_path):
                
                dest_item_path = os.path.join(destination_folder, item)
                if os.path.exists(dest_item_path):
                    shutil.rmtree(dest_item_path)
                shutil.copytree(item_path, dest_item_path)
            else: # This will overwrite any files already in the destination folder
                shutil.copy2(item_path, destination_folder)
            print(f"Copied: {item}")
        except Exception as e:
            print(f"Error copying {item}: {e}")
if __name__ == "__main__":
    destination = "Add your destination folder Here"
    exclusions = ["Add the folders/files you don't want copied Here"] 
    copy_desktop_contents(destination, exclusions)

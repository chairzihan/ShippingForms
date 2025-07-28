
import shutil as shu
from pathlib import Path
import os

class ExcelCreate(): 

   from saveYaml import get_config_path

   def copyExcel():
        import datetime
        source = r"C:\Code\ShippingForms\Shipping_Request_Template.xlsm"
        home = Path.home()

        config_dir = home / '.shippingForms'
        config_dir.mkdir(exist_ok=True)

        # Create a unique filename using timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        dest_file = config_dir / f"Shipping_Request_{timestamp}.xlsm"
        shu.copy(source, dest_file)
        print(f"created file called: {dest_file}")
        os.startfile(dest_file)
      

    

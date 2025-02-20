# author: yasmim-github
# C:\Users\10724112743\Downloads\exercicio_um
# useful links : https://www.geeksforgeeks.org/working-images-python/

try:
    import pkg_resources
except ImportError as e:
    print(f"pkg_resources module not found: {e}")
    print("Using shell or Bash, run the command : pip install setuptools, make sure the library is properly installed on your enviromnent")

try:
    from PIL import Image
except ImportError as e:
    print(f"PILL module not found: {e}")
    print("Using shell or Bash, run the command : pip install pillow, make sure the library is properly installed on your enviromnent")

path = r"python.png"

try:
    img = Image.open(path)
    img.show()
except IOError as e:
    print(f"Unable to open image: {e}")
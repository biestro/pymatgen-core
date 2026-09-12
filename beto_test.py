"""
Test for the LOCPROJ string
and the OUTCAR magnetic magnetization
"""

# from src.pymatgen.io.vasp import Incar
from pymatgen.io.vasp import Incar
from pymatgen.io.vasp import Outcar

if __name__ == "__main__":
    incar = Incar.from_file("test-files/core/locproj/INCAR")
    print(incar)

    outcar = Outcar

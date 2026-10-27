"""
Test for the LOCPROJ string and WANNIER90_WIN strings

# TODO: Outcar magnetization for LSORBIT=T
"""

# from src.pymatgen.io.vasp import Incar
from src.pymatgen.io.vasp import Incar
# from .pymatgen.io.vasp import Outcar

if __name__ == "__main__":
    incar = Incar.from_file("test-files/core/locproj/INCAR_win")
    # print(incar)
    print(incar)
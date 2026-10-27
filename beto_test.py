"""
Test for the LOCPROJ string and WANNIER90_WIN strings

# TODO: Outcar magnetization for LSORBIT=T
# TODO: Add POTCAR channels for LOCPROJ parsing (e.g. Ps 1)
"""

# from src.pymatgen.io.vasp import Incar
from src.pymatgen.io.vasp import Incar, Vasprun
from collections import defaultdict
from pymatgen.core import Structure
from pymatgen.symmetry.bandstructure import HighSymmKpath
from pathlib import Path
# from .pymatgen.io.vasp import Outcar

if __name__ == "__main__":
    base = Path("test-files/core/locproj/")
    incar = Incar.from_file(Path(base, "INCAR_win"))
    # vasprun = Vasprun(Path(base.parent, "line", "vasprun.xml"))
    print(incar['LOCPROJ'])
    print(incar['WANNIER90_WIN'])

    print("\n New parameters")
    structure = Structure.from_file(Path("test-files/cif/Fe.cif"))
    high_symm  = HighSymmKpath(structure)
    
    params = {
        "kmesh_tol": 1e-5,
        "write_xyz": True,
        # "kpoint_path": high_symm,  # Or high_symm itself
    }

    incar = Incar({'WANNIER90_WIN': params})
    print(incar['WANNIER90_WIN'])
    incar.write_file("test-files/core/locproj/INCAR_out")

    print()
    print("Reading/parsing what we just saved")
    incar = Incar.from_file(Path(base, "INCAR_out"))
    print(incar['WANNIER90_WIN'])




    # incar_new = incar.copy()
    # incar_new['WANNIER90_WIN'] = {'kmesh_tol': 1e-5, 'write_xyz': True}
    # print()
    # print(incar_new)
    # incar_new.write_file("test-files/core/locproj/INCAR_out")

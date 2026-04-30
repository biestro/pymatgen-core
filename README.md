## Why this fork

VASP sometimes requires INCAR inputs that are either multiline strings or plain strings with semicolons `;` splitting prameters.
The defauly `pymatgen` does not account for this, as it treats the INCAR as key-value pairs. However, tags like `LOCPROJ`
need the possibility of semicolons and raw-string utilities, and so this fork fixes the `Incar.from_str` and validates `LOCPROJ` inputs!

## License

Pymatgen is released under the MIT License. The terms of the license are as follows:

```txt
The MIT License (MIT) Copyright (c) 2011-2012 MIT & LBNL

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of
the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

## About the Pymatgen Development Team

Shyue Ping Ong (@shyuep) of the [Materials Virtual Lab] started Pymatgen in 2011 and is still the project lead.
Janosh Riebesell (@janosh) and Matthew Horton (@mkhorton) are co-maintainers.

The [`pymatgen` development team] is the set of all contributors to the `pymatgen` project, including all subprojects.

## Our Copyright Policy

Pymatgen uses a shared copyright model. Each contributor maintains copyright over their contributions to `pymatgen`.
But, it is important to note that these contributions are typically only changes to the repositories. Thus, the
`pymatgen` source code, in its entirety is not the copyright of any single person or institution. Instead, it is the
collective copyright of the entire [`pymatgen` Development Team]. If individual contributors want to maintain a
record of what changes/contributions they have specific copyright on, they should indicate their copyright in the
commit message of the change, when they commit the change to one of the `pymatgen` repositories.

[`pymatgen` docs]: https://pymatgen.org
[materials project]: https://materialsproject.org
[`pymatgen` development team]: https://pymatgen.org/team
[materials virtual lab]: https://materialsvirtuallab.org

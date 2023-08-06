# PyProtWorm
![ProtWorm](http://bioinfo.icb.ufmg.br:9000/static/images/logo2.png)

PyProtWorm is a python package designed to simplify the scientific literature review in protein characterization studies. The package uses the [Europe PMC](https://europepmc.org/) rest API to obtain amino acids residues citations from scientific publications.

To use PyProtWorm, all you need to do is import the Finder class, define the object and perform a query, as can be seen in the example below:

    from PyProtWorm.finder import Finder
    
    finder = Finder("/path/to/output.tsv")
    finder.search("query")

The package also allows performing cross-annotation searches using several external resources identifiers:

    finder = Finder()
    finder.search("P00698", database="uniprot")

The full list of available external resources contains:

| Resource | key |
|--|--|
| UniProtKB | uniprot |
| PDBe | pdb |
| Pfam | pfam |
| ChEMBL | chembl |
| ChEBI | chebi |
| Gene Ontology | go |
| InterPro | interpro |

The *min_year* parameter can be applied to retrieve only recently published papers:

    finder = Finder()
    finder.search("P00698", database="uniprot", min_year=2019)

Stopped jobs can be resumed from the same point when it was aborted. To do it, you need to inform the *cursor* parameter in the search method. The current cursor id can be found in the last row of your result file. Finally, you need to make sure not to overwrite the previous result file.

    finder = Finder()
    finder.search("P00698", database="uniprot", cursor="AoIIPyzELSgyNzg5NjQ3OQ==")

There's no paper to cite right now. For now, if you use this tool please cite:

> da Fonseca, Neli et al., 2021 **ProtWorm: A computational tool to find amino acid residues citations** available at http://bioinfo.icb.ufmg.br/protworm.

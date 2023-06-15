# CanonFotoSorter
A python app that sorts images imported from Canon EOS cameras into date specific folders

Generally, Canon cameras have folder structures {counter}CANON e.g. 247CANON, 248CANON, 249CANON etc

The script traverses a folder structure, reads the image datetime, moves it to a folder with a name matching the pattern: "yyyy-MM-dd"

# Generatív Mesterséges Intelligencia Modellek Összehasonlítása Kódgenerálási Feladatokon  
  
## A projekt célja

A kutatásban használt alap LLM-ek: ChatGPT, Bard, LLaMA kerülnek összehasonlításra kisebb, ingyenesen elérhető modellekkel kód szintézis minőséget vizsgálva.

A modellek több különböző szempontból lesznek kiválasztva, keresésükre és hozzájuk való hozzájutáshoz a [Hugging Face](https://huggingface.co) nevű weboldal lesz igénybe véve. A kiválasztásuk oka lehet népszerűség, frissesség, letöltések száma, lájkok száma és további hasonló jellemzők. 

A kutatás célja a modellek mélyebb megismerése, szemléltetése, köztük lévő betanításbeli megvalósítások megértése és ez okozta generálási minőség összevetése, elemzése. Célnak tekinthető még a legjobb "kis" méretű modell felderítése is.

A generált kódrészletek egy kód szintézis benchmarkon fognak átfutni. A generált programrészek benchmarkolására a PSB2 (The Second Program Synthesis Benchmark Suite) programszintézis benchmarkkészletből kiválasztott feladatok és hozzájuk tartozó tesztek lesznek felhasználva. A mérések során az eredményt az átment tesztek száma, futási ideje fogják alkotni. 


## Fájlok elérése

### Szkriptek 

A szkripteket a `PSB2 Tests` mappán belül lehet élérni.    

- `generate_files.py`: A mappastruktúra kialakításához írt szkript.
- `create_datasets.py`: A PSB2 adathalmazok letöltéséhez szükséges szkript.
- `run_benchmark.py`: Szkript a benchmarkolás futtatásához.
- `run_data_analysis.py`: Az adatelemzés futtatása a benchmark által létrehozott eredményeken.
- `merge_data.py`: Az adatelemzés készítette statisztikák egyesítése.
 

### Modellek által generált forráskódok és eredmények

A `PSB Tests/models (with zipped folders)` mappán belül találhatjuk a modelleket, zippelve túl nagy méretük miatt.
Egy modell mappán belül a `Python/tests` tartalmazza a problémákat és a hozzájuk generált forráskódokat.
Szintén egy modell mappán belül pedig láthatjuk az eredményeket a `results_x` mappákban.  


### Statisztika

A `PSB2 Tests/statistics` mappában elérhetőek.
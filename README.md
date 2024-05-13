# Generatív Mesterséges Intelligencia Modellek Összehasonlítása Kódgenerálási Feladatokon  

# Comparison of Generative Artificial Intelligence Models on Code Generation Tasks  

A kutatásban használt alap LLM-ek: ChatGPT, Bard, LLaMA kerülnek összehasonlításra kisebb, ingyenesen elérhető modellekkel kód szintézis minőséget vizsgálva.

A modellek több különböző szempontból lesznek kiválasztva, keresésükre és hozzájuk való hozzájutáshoz a [Hugging Face](https://huggingface.co) nevű weboldal lesz igénybe véve. A kiválasztásuk oka lehet népszerűség, frissesség, letöltések száma, lájkok száma és további hasonló jellemzők. 

A kutatás célja a modellek mélyebb megismerése, szemléltetése, köztük lévő betanításbeli megvalósítások megértése és ez okozta generálási minőség összevetése, elemzése. Célnak tekinthető még a legjobb "kis" méretű modell felderítése is.

A generált kódrészletek egy kód szintézis benchmarkon fognak átfutni. A generált programrészek benchmarkolására a PSB2 (The Second Program Synthesis Benchmark Suite) programszintézis benchmarkkészletből kiválasztott feladatok és hozzájuk tartozó tesztek lesznek felhasználva. A mérések során az eredményt az átment tesztek száma, futási ideje fogják alkotni. 
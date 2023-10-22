# Tématerv - Sári Norbert



## Személyes adatok

**Név**: Sári Norbert

**Neptun**: BOLZTJ

**E-mail**: h164903@stud.u-szeged.hu

**Szak**: Programtervező informatikus BSc nappali

**Végzés várható ideje**: 2024. nyár

## A szakdolgozat tárgya

Generatív mesterséges intelligencia modellek összehasonlítása kódgenerálási feladatokon.
A kutatásban használt alap LLM-ek: ChatGPT, Bard, LLaMA kerülnek összehasonlításra kisebb, ingyenesen elérhető modellekkel kód szintézis minőséget vizsgálva.

A modellek több különböző szempontból lesznek kiválasztva, keresésükre és hozzájuk való hozzájutáshoz a [Hugging Face](https://huggingface.co) nevű weboldal lesz igénybe véve. A kiválasztásuk oka lehet népszerűség, frissesség, letöltések száma, lájkok száma és további hasonló jellemzők. 

A kutatás célja a modellek mélyebb megismerése, szemléltetése, köztük lévő betanításbeli megvalósítások megértése és ez okozta generálási minőség összevetése, elemzése. Célnak tekinthető még a legjobb "kis" méretű modell felderítése is.

A generált kódrészletek egy kód szintézis benchmarkon fognak átfutni, ahol unit tesztekkel kiértékelésre kerülnek. A generált programrészek benchmarkolására a PSB2 (The Second Program Synthesis Benchmark Suite) programszintézis benchmarkkészletből kiválasztott feladatok és hozzájuk tartozó unit tesztek lesznek felhasználva. A mérések során az eredményt az átment tesztek száma, futási ideje és ezekhez hasonló tulajdonságok fogják alkotni. 


## Használni kívánt technológiák

- [Hugging Face](https://huggingface.co) gépi tanulási platform használata a modellekhez való hozzájutáshoz.
- Hugging Face Hub, Git és Git LFS használata a modellek/adathalmazok menedzseléséhez.
- Python használata a modellek használatához és esetleges szkriptek írásához.
- [Obsidian](https://obsidian.md) jegyzetek használata az eredmények struktúrált fenntartása érdekében.

## Tervezett ütemezés

- **2023. szeptember:** Tématerv kigondolása, megtervezése.
- **2023. október:** Használt modellek kiválasztása, áttekintése, megismerése és kipróbálása. 
- **2023. november:** Hugging Face Hub megismerése. Használni kívánt PSB2 tesztek kiválasztása.
- **2023. december:** Kódgenerálás és tesztek futtatása, eredmények feljegyzése.
- **2024. január:** További kódgenerálás és tesztelemzés. A kapott eredmények vizsgálata.
- **2024. február:** Eredmények vizsgálata.
- **2024. március:** Implementációs fejezet hozzáadása.
- **2024. április:** A szakdolgozat végső hibáinak kijavítása.

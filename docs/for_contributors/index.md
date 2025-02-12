# Jegyzeteléshez

???+ info "Háttértörténet" 
    Szinte az összes tantárgyhoz készült jegyzet$^*$, amik egy privát GitHub repositoryba lettek feltéve. Ezek mind [markdownban](https://en.wikipedia.org/wiki/Markdown) készültek egy bizonyos flavor-rel és egész jól szerepeltek számonkérések során. A repo-nak a megosztása azonban több problémába is ütközött, ezért jött létre egy nyílt alternatíva, ami remélhetőleg több VIK-es hallgató tanulmányait is elősegítheti.
    
    <p style="font-size: 0.8em; font-style: italic">*: A specializációnál ezt már nehezebb volt tartani, ott a szoftverfejlesztés ágazat specifikus tárgyai lettek tárgyalva</p>

## Új jegyzet feltöltése

#### Szerkesztés
Alapvetően a Visual Studio Code-hoz készült [Markdown Preview Enhanced](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced) kiegészítőt használtuk jegyzetek készítésére, ezért az oldalt is igyekeztünk úgy létrehozni, hogy támogassa minden funkcióját. Ezt a [showcase](./showcase.md) odalon részletesebben is megnézheted.

Vagyis elegendő ezt a kiegészítőt használni a `docs` mappán belül, ha csak dokumentációs céljaid vannak. Természetesen azt is szeretnénk, hogy az általad készített dokumentumok elérhetőek legyenek, ezért a gyökérmappában a `mkdocs.yaml` fájlban, a `nav` tulajdonságban fel kell venned a dokumentumaid nevét és elérési módját.

#### Feltöltés
Ahhoz, hogy a dokumentumaid / javításaid megoszd másokkal az alábbi lépéseket javasoljuk:

**For contributors:**

1. Klónozd le a repository-t
    ```bash
    git clone https://github.com/VIK-CE-Notes/vik-ce-notes.github.io
    ```
2. Végezd el a változtatásokat
3. Egy új branch-en töltsd fel
    ```bash
    git checkout -b <MySubjectNotes>
    git add .
    git commit -m "Added notes for Subject"
    ```
4. Nyiss egy pull requestet

**Újonnan csatlakozók:**
- Mivel még nem hozhatsz létre új branch-et, ezért a `gh repo fork` használata javasolt
-  Alternatíva a fentebbi lépések használata VS Code-ban, ami push-nál automatikusan felajánlja a fork elvégzését.

És ha minden jól megy, akkor hamarosan a `main` branchre is kikerülnek a változtatások.

## Az oldal formálása

#### Python környezet használata
Amennyiben nagyobb változtatást szeretnél eszközölni (például új diagram típus támogatása), akkor már valószínűleg szükséged lesz a python környezet használatára.

A projekt [MkDocs](https://www.mkdocs.org/)-ra épül, a témája [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) és Python `3.11`-es verziót használ. Kezdetként az alábbi lépéseket tudom ajánlani:
```bash
git clone https://github.com/VIK-CE-Notes/vik-ce-notes.github.io
cd vik-ce-notes.github.io

# itt hozhatsz létre virtuális környezetet

pip install -r requirements.txt
mkdocs serve
```

Mostmár a [http://127.0.0.1:8000](http://127.0.0.1:8000) url-en el is érheted az oldalt.

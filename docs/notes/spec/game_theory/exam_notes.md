## 1. Kombinatorikus játék fogalma, éles játék, betli játék, nyerő stratégia. Irányított gráf magja, mag egyértelműsége DAG-ban. Játékok, ill. pozíciók típusa

### Kombinatorikus játék

- **Kétszemélyes** és **szekvenciális**: a két játékos felváltva lép
- Adott egy (V, E) irányított gráf. V a lehetséges pozíciók (esetleg végtelen) halmaza. Egy pontból kiinduló élek a lehetséges lépéseknek felelnek meg. Teljesítenie kell a következőket:
- **A játék végesfokú:** gráfban minden pont kifoka véges;
- **A játék véges:** nincs végtelen hosszú irányított séta a gráfban.
- Általában adott egy p0 kezdőállás is, ami lehet egy konkrét állás (mint a sakknál) vagy egy tetszőleges V -beli állás, a játék paramétereként.
- A játéknak kétféle kimenetele van:
- Nyer-veszt
- Döntetlen
- Nyelő típusok:
- $N_W$:Nyerő nyelő(utolsó lépő nyert)
- $N_T$: Döntetlen
- $N_L$: Vesztő nyelő(utolsó lépő veszt)

- Játék típusok
- **Éles**: ha minden nyelő P típusú
- **betli**: ha mindegyik N típusú

$J$ típusa:

- `1-es`, ha a kezdő garantálni tudja, hogy előbb-utóbb $N_W$ beli mezőbe lép
- `*`, ha a kezdő garantálni tudja, hogy az ellenfél nem lép $N_W$ belibe
- `2-es`, ha nem `1-es` és  nem `*`

#### Stratégia

Stratégia alatt egy $V → V$ függvényt értünk, amely minden $V$ -beli helyzethez, amelyik nem nyelő, hozzárendeli az egyik ki-szomszédját: vagyis tetszőleges álláshoz hozzárendelünk egyet a lehetséges lépések közül. Egy játékos követi az adott stratégiát, ha mindig a stratégia által kijelölt pozícióba lép.

**Nyerő** egy stratégia, ha őt követve mindig nyerni tudunk, akármit is lépjen közben a másik játékos.

#### Irányított gráf magja

A $G = (V, E)$ gráf egy $S ⊆ V$ független ponthalmazát magnak nevezzük, ha minden $(V \backslash S)$-beli csúcsnak van $S$-beli szomszédja.

##### Tétel

Ha $G$ DAG, akkor $\exists G$-ben $K$ mag

---

## 2. Játékok összege, az összeg típusa. Grundy-számozás. NIM-összeadás és tulajdonságai

### Játékok összege

A $J$ és $J'$ kombinatorikus játék összegén azt a $J +J '$ kombinatorikus játékot értjük, melyben a két játékos párhuzamosan játssza a $J$ és $J'$ játékokat úgy, hogy a soron következő játékos a $J$ és $J'$játékok közül pontosan az egyikben lép egyet, és a $J + J'$ végeredménye az utoljára befejezett játék eredménye lesz.

### Az összeg típusa

1. $J+J$: 2-es típusú
2. Ha a $J = (V, E, p_0)$ játék $P$ típusú, akkor a $J + J'$ összegjáték tetszőleges J' játékra ugynolyan típusú, mint $J'$.
  **Bizonyítás:**
  Annak a játékosnak, akinek $J'$-ben nyerő stratégiája van, a következő lesz a nyerő stratégiája $J + J'$-ben: lépjen $J'$-ben a stratégiája szerint, kivéve, ha a másik $J$-ben lép, ekkor a $J$-beli nyerő stratégiája szerint lépjen (hiszen $J$-ben a másodiknak van nyerő stratégiája).

3. Tetszőleges $J$ és $J'$ játékokra $J$ és $J + J'+ J'$ típusa megegyezik.
**Bizonyítás:** A $J$-ben nyerő játékos játszon a $J$-beli nyerő stratégiája szerint, kivéve, ha a másik a $J'$ egyik példányában lép, ekkor lépje ugyanezt a másik példányban.




### Grundy-számozás

Egy $G = (V, E)$ gráffal rendelkező éles kombinatorikus játék Grundy-számozása egy olyan $g : V \rightarrow \mathbb{N}$ függvény, melyre tetszőleges $v ∈ V$ esetén $g(v) = mex\{g(w) \space| \space vw \in E\}$ , ahol egy nemnegatív számokból álló halmaz mex (minimum excludant) értékén azt a legkisebb nemnegatív egész számot értjük, ami nincs benne a halmazban.

Minden éles kombinatorikus játéknak létezik Grundy-számozása.

#### NIM összeg

Nim-összeg. Az a, $b ∈ \mathbb{N}$ számok nim-összegét úgy kapjuk meg, hogy mindkét számot felírjuk kettes számrendszerben és az azonos helyiértéken szereplő számjegyeiket modulo 2 összeadjuk. Jele: $a ⊕ b$.

#### Tulajdonságai

1. $a \oplus b = c \iff a \oplus b \oplus c = 0 \iff a \oplus c = b \iff b \oplus c = a$
2. $c < a \oplus b \implies \exists a' < a: a' \oplus b = c$ vagy $\exists b' < b: a \oplus b' = c$

#### Megfigyelések

- $a \oplus b = a \oplus b' \implies b = b'$
- $a \oplus b = a \oplus b' \iff b \oplus b' = a \oplus a = 0$
- $(a \oplus b) \oplus (a \oplus b') = 0 \iff b \oplus b' = 0 \iff b = b'$

---

## 3. Sprague-Grundy-tétel*, Bouton-tétel. Játékok izomorfiája és ekvivalenciája

### Sprague-Grundy-tétel

Ha a $G = (V, E)$ és $G' = (V', E')$ gráfokkal rendelkező éles kombinatorikus
játékok Grundy-számozása rendre $g : V → \mathbb{N}$ és $g' : V' → \mathbb{N}$, akkor a két játék összegének Grundy számozása $$g ⊕ g' : V × V' → \mathbb{N}$$.

### Bouton-tétel

Legyen $k ∈ \mathbb{N}_+$ és tekintsük azt a k-nim játékot, amiben a kupacok méretei $n_1, n_2, . . . , n_k$.
Ekkor a második játékosnak pontosan akkor van nyerő stratégiája, ha $n_1 ⊕ n_2 ⊕ . . . ⊕ n_k = 0$.

### Játékok izomorfiája

A $(G, N_W, N_T, N_L, v_0)$ és $(G', N'_W, N'_T, N'_L, v'_0)$, ha létezik $G$ és $G'$ között olyan gráf izomorfizmus, ami a nyelőket és a kezdőállásokat is megőrzi.

### Játékok ekvivalenciája

A $J_1$ és $J_2$ játékok **eklivalensek**, ha $J_1 + J_2$ egy 2-es típusú játék.

Az alábbi állítások ekvivalensek:

1. $J_1 + J_2$ 2-es típusú
2. $G_{J_1}(u_0) = G_{J_2}(v_0)$
3. Tetszőleges $H$ éles játékra $J_1 + H$ és $J_2 + H$ azonos típusúak.

## 4. Stratégia másolás, stratégialopás. Mérgezett csoki, amőba, hex

### Stratégia másolás

### Stratégia lopás

### Mérgezett csoki

1-es típusú

### Amőba

A k-amőbában az első játékosnak van nem vesztő stratégiája.

### Hex

Adott egy $(n \times n)$-es hatszögrács, ahol $n ∈ \mathbb{N}_+$, és a soron következő játékos kiválasztja ennek egy (korábban még egyik játékos által sem választott) mezejét. A kezdőjátékos akkor nyer, ha keletkezik az általa kiválasztott mezőkből egy út a rács bal szélétől a jobbig, a másik játékos pedig akkor nyer, ha keletkezik az általa kiválasztott mezőkből egy út a rács első szélétől az alsóig.

A hex-ben az első játékosnak van nem vesztő stratégiája.

**Hex tétel** (Hein, Nash, Gale). A hex játék sohasem végződhet döntetlennel.

## 5. Építő-romboló játékok, Erdős-Selfridge-tétel*, hipergráfok 2-színezhetőségének elégséges feltétele

### Építő-romboló játékok, valamint romboló-építő játékok

Adott egy $\mathcal{H} = (V, \varepsilon)$ hipergráf, és a soron következő játékos kiválaszt egy (korábban még egyik játékos által sem választott) $V$ -beli csúcsot. Az építő játékos akkor nyer, ha kiválasztja valamely $\varepsilon$-beli hiperél minden csúcsát, a romboló játékos pedig akkor nyer, ha ezt meg tudja akadályozni. Ha a kezdőjátékos az építő, akkor építő–romboló, ellenkező esetben pedig romboló–építő  átékról beszélünk.

### Erdős-Selfridge-tétel

Ha egy építő-romboló játék $\mathcal{H} = (V, \varepsilon)$ hipergráfjára $\sum_{E \in \varepsilon} 2^{-|E|} < 1/2$ teljesül, akkor a romboló játékosnak mindig van nyerő stratégiája.

### Hipergráfok 2-színezhetőségének elégséges feltétele

**Tétel**:

Ha egy $\varepsilon$ halmazrendszerre a rombolónak van nyerő stratégiája (második játékosként), akkor 2-színezhető.

**Bizonyítás**:
Tudjuk, hogy akkor is a romboló nyerne, ha ő kezdene. Játsszon mindkét játékos a romboló stratégiája szerint, és színezzük a pontokat aszerint, hogy ki foglalja el: az építő pontjait kékkel, a romboló pontjait pirossal. Ekkor mindketten elérik, hogy minden $\varepsilon$-beli halmazból legyen pontjuk, vagyis a kapott színezés jó 2-színezés.


## 6. Stratégiai játékok, fogolydilemma, Pareto-optimális stratégiaválasztás, domináns stratégiák, kevert stratégiák. Stratégiák (iterált) eliminálása és annak hatása a Pareto-optimális stratégiaválasztásokra

### Stratégiai játék

Adott $n ∈ \mathbb{N}_+$ játékos, és tetszőleges $i ∈ \{1, . . . , n\}$ esetén adott az $i$-edik játékoshoz a lehetséges stratégiáinak egy véges $S_i$ halmaza, valamint egy $u_i: S1 × . . . × Sn → \mathbb{R}$ nyereségfüggvény. Minden játékos ismeri a többiek lehetséges stratégiáit és nyereségfüggvényeit. A játék elején a játékosok egymástól függetlenül kiválasztanak egy-egy stratégiát azzal a céllal, hogy maximalizálják a saját nyereségüket.

**Tulajdonságok:**

- **Egy lépéses:** a játékosok egyszerre lépnek
- **Szinkron:** a játékosok egyszerre döntenek, a döntést titkolva egymástól
- **Teljes információ:** minden játékos minden a játékra vonatkozó információt ismer
- **Racionalítás:** minden játékos a saját nyereségét maximalizálja
- **Racionalítás köztudása:** minden játékos felteszi, hogy a többiek racionálisak és hogy `ők is tudják, hogy a többiek racionálisak`
- **Nullösszegű:** a játékosok nyereségének összege nulla

### Fogolydilemma

A fogyoldilemma egy gondolatkísérlet, ahol két racionális ügynök közötti játékot vizsgáljuk. A játékosoknak két lehetősége van: együttműködés vagy árulás. A játékosoknak az a céljuk, hogy a saját nyereségüket maximalizálják. A játék szabályai a következők:

|       | Tagad      | Vall  |
|-------|-----------|--------|
| Tagad |  -1, -1   | -3, 0  |
| Vall  |  0, -3    | -2, -2 |

A játékban az árulás a az erős domináns stratégia, azaz a játékosoknak az a legjobb, ha árulnak. Így a Nash-egyensúlyban mindkét játékos árulni fog. Ez a megoldás azonban nem Pareto-optimális, mert ha mindketten tagadnának, akkor mindketten jobban járnának.

### Pareto-optimális stratégiaválasztás

Pareto-optimális stratégiaválasztás. Az $(s_1,..., s_n) ∈ S_1×. . .×S_n$ stratégiaválasztás Pareto-optimális, ha nem létezik olyan $(s'_1, . . . , s'_n) ∈ S_1 ×...× S_n$ stratégiaválasztás, melyre a következők teljesülnek:

- minden $i ∈ {1, . . . , n}$ esetén $u_i(s_1,..., s_n) ≤ u_i(s'_1,..., s'_n)$, és
- $\exists j ∈ {1, . . . , n}$, amelyre $u_j(s_1,..., s_n) < u_j(s'_1,..., s'_n)$

### Domináns stratégiák

#### Gyenge dominálás

A $z \in S_i$ stratégia gyengén dominálja a $z' \in S_i$ stratégiát, ha tetszőleges $s_1 \in S_1,..., s_{i-1} \in S_{i-1}, s_{i+1} \in S_{i + 1}, ..., s_n \in S_n$ esetén
$$
u_i(s_1,..., s_{i-1}, z, s_{i+1} ..., s_n) \geq u_i(s_1,..., s_{i-1}, z', s_{i+1} ..., s_n)
$$

#### Erős dominálás

A $z \in S_i$ stratégia erősen dominálja a $z' \in S_i$ stratégiát, ha tetszőleges $s_1 \in S_1,..., s_{i-1} \in S_{i-1}, s_{i+1} \in S_{i + 1}, ..., s_n \in S_n$ esetén
$$
u_i(s_1,..., s_{i-1}, z, s_{i+1} ..., s_n) > u_i(s_1,..., s_{i-1}, z', s_{i+1} ..., s_n)
$$

### Kevert stratégiák

Tetszőleges $i ∈ {1, . . . , n}$ esetén egy $S_i$ halmaz feletti valószínűségi eloszlást az $i$-edik játékos kevert stratégiájának nevezünk. Az $i$-edik játékos kevert stratégiáinak halmazát a $∆_i$ szimbólummal jelöljük.

### Stratégiák (iterált) eliminálása

- **Szigorú eliminálás**: Azokat a stratégiákat elimináljuk, amelyek erősen domináltak.
- **Laza eliminálás**: Azokat a stratégiákat elimináljuk, amelyek gyengén domináltak.

Addig ismételjük az eliminálást, amíg lehet.

### Iterált eliminálás hatása a Pareto-optimális stratégiaválasztásokra

1. Szigorú eliminálás után Pareto-optimális kimenetek eltűnhetnek és keletkezhetnek. Tiszta Nash
egyensúlyok nem tűnhetnek el.

2. Laza eliminálás után Pareto-optimális kimenetek ugyan azok maradnak. Ha eliminálás után egy
kimenetel tiszta Nash egyensúly, akkor az aze liminálás előtt is az volt.

`Szigorú eliminálás nem változtat a tiszta Nash egyensúlyok halmazán`

## 7. Iterált szigorú eliminálás sorrend-függetlensége*. Tiszta és kevert Nash-egyensúly, (iterált) eliminálás hatása a Nash-egyensúlyokra*

### Iterált szigorú eliminálás sorrend-függetlensége

Akármilyen sorrendben töröljük a dominált stratégiákat az iterált eliminálás szigorú változatánál,
a megmaradó stratégiák mindig ugyanazok lesznek.

### Tiszta és kevert Nash-egyensúly

Egy $(s_1, s_2, ..., s_n) \in S_1 \times S_2 \times ... \times S_n$ stratégiaválasztás `Nash egyensúly`, ha minden $i \in \{1, ..., n\}$ játékosra teljesül, hogy nincs olyan $s_i' \in S_i$ stratégia, amelyre

$$
u_i(s_1, ..., s_{i-1}, s_i', s_{i+1}, ..., s_n) > u_i(s_1, ..., s_{i-1}, s_i, s_{i+1}, ..., s_n).
$$

Más szóval, egy stratégiaválasztás Nash egyensúly, ha egyetlen játékos sem tudja növelni a saját nyereségét azzal, hogy egyoldalúan megváltoztatja a stratégiáját.

- **Tiszta Nash-egyensúly**:

  Az $(s_1, s_2, ..., s_n) \in S_1 \times S_2 \times ... \times S_n$ tiszta stratégiaválasztás tiszta Nash egyensúly, ha minden $i ∈ {1, ..., n}$ és $s_i' \in S_i$ esetén az $i$-edik játékos várható nyeresége a $(s_1,..., s_{i-1}, s_i, s_{i+1},..., s_n)$ stratégiaválasztás mellett legalább akkora, mint a $(s_1,..., s_{i-1}, s_i', s_{i+1},..., s_n)$ mellett, azaz

$$
u_i(s_1,..., s_{i-1}, s_i, s_{i+1},..., s_n) \geq u_i(s_1,..., s_{i-1}, s_i', s_{i+1},..., s_n)
$$

- **Kevert Nash-egyensúly**:

  Az $(\sigma_1,...,\sigma_n) \in \Delta_1 \times...\times\Delta_n$ kevert stratégiaválasztás kevert Nash egynesúly, ha minden $i ∈ {1,..., n}$ és $\sigma_i' \in S_i$ esetén az $i$-edik játékos várható nyeresége a $(\sigma_1,..., \sigma_{i-1}, \sigma_i, \sigma_{i+1},..., \sigma_n)$ stratégiaválasztás mellett legalább akkora, mint a $(\sigma_1,..., \sigma_{i-1}, \sigma_i', \sigma_{i+1},..., \sigma_n)$ mellett, azaz

$$
u_i(\sigma_1,..., \sigma_{i-1}, \sigma_i, \sigma_{i+1},..., \sigma_n) \geq u_i(\sigma_1,..., \sigma_{i-1}, \sigma_i', \sigma_{i+1},..., \sigma_n)
$$

### (Iterált) eliminálás hatása a Nash-egyensúlyokra

1. Szigorú eliminálással kevert Nash egyensúly nem tűnik el
2. Laza eliminálás után kapott kevert Nash egyensúly az eredeti játékhoz is kevert Nash egyensúly.

## 8. Maximin stratégiák. Kétszemélyes, 0-összegű, véges játékok: maximin stratégia és Nash-egyensúly kapcsolata*, Neumann-tétel (biz. nélkül)

### Maximin stratégiák

Egy játékos olyan kevert stratégiáját, mely maximalizálja számára a lehető legkisebb várható nyereséget a többi játékos bármilyen kevert stratégiái esetén, maximin stratégiának nevezünk.

### Kétszemélyes, 0-összegű, véges játékok: maximin stratégia és Nash-egyensúly kapcsolata

A játékosok maximin stratégiái minden véges, kétszemélyes, 0-összegű mátrixjátékban éppen a kevert Nash-egyensúlyoknak felelnek meg.

### Neumann-tétel

Minden véges, kétszemélyes, 0-összegű mátrixjátékban a sorjátékos minimális várható nyereségének maximuma megegyezik az oszlopjátékos maximális várható veszteségének minimumával.

## 9. Osztozkodási játék, arányos elosztások. Oszt-választ, Fink- és Tasnádi-eljárás

### Osztozkodási játék

### Elosztás

Elosztás alatt egy olyan $(A_1, \dots, A_n)$ rendezett $n$-est értünk, ahol:

- Tetszőleges $i \in \{1, \dots, n\}$ esetén $A_i$ véges sok páronként diszjunkt, balról zárt és jobbról nyílt intervallumoknak az uniója,
- $A_1, \dots, A_n$ halmazok a $[0, 1]$ intervallum egy felosztását alkotják (azaz páronként diszjunktak és az uniójuk $[0,1]$).

### Értékelő eloszlásfüggvény

Tetszőleges $i \in \{1, \dots, n\}$ esetén adott az $i$-edik játékosnak az $f_i$ értékelő eloszlásfüggvénye, melyre a következők teljesülnek:

- $f_i: [0, 1] \to [0, 1]$,
- folytonos,
- monoton növekvő,
- $f_i(0) = 0$,
- $f_i(1) = 1$.

Az $i$-edik játékos értékelő függvénye egy olyan $\mu_i$ függvény, hogy:
$$
\mu_i(0) = 0, \quad \mu_i([a, b]) = f_i(b) - f_i(a),
$$
és tetszőleges $k \in \mathbb{Z}_+$, $0 \leq a_1 < b_1 \leq a_2 < b_2 \leq \dots \leq a_k < b_k \leq 1$ esetén:
$$
\mu_i\left(\bigcup_{j=1}^k [a_j, b_j]\right) = \sum_{j=1}^k \big(f_i(b_j) - f_i(a_j)\big).
$$

### Arányos elosztás

Egy $(A_1, \dots, A_n)$ elosztás `arányos`, ha tetszőleges $i \in \{1, \dots, n\}$ esetén $\mu_i(A_i) \geq 1/n$.

### Irigységmentes elosztás

Egy $(A_1, \dots, A_n)$ elosztás irigységmentes, ha tetszőleges $i, j \in \{1, \dots, n\}$ esetén $\mu_i(A_i) \geq \mu_i(A_j)$.

### Oszt és választ

Két játékos esetén az egyik játékos a saját értékelő függvénye szerint két egyenlő részre osztja az elosztandó halmazt, majd a másik játékos kiválasztja ezek közül a saját értékelő függvénye szerint némirosszabbat.

### Fink-eljárás

Rekurzívan definiáljuk: ha az első $n - 1$ játékos már arányosan megosztozott az $(n - 1)$-személyes Fink-eljárással, akkor felosztják a saját értékelő függvényük szerint a saját részüket $n$ egyenlő  részre, és az $n$-edik játékos mindenkiből választ a saját értékelő függvénye szerint egy-egy legjobb részt.

### Tasnádi-eljárás

Az első játékos a saját értékelő függvénye szerint $n$ egyforma részre osztja az elosztandó halmazt, és mind az $n$ részhez előkészít $n - 1$ darab jegyet. A $k$-adik játékos mindegyik elvessz $n - k$ darab különböző jegyet aszerint, hogy melyik $n - 1$ részt értékeli a saját értékelő függvénye szerint a legjobbra. A fel nem használt $n - 1$ darab jegy az első játékosnál marad. Ezután az $n$ rész mindegyikén $n - 1$ játékos osztozkodik tovább a Tasnádi-eljárásnak megfelelő multiplicitással vesz részt.

## 10. (Diszkrét) mozgó késes és Even-Paz eljárás. Irigységmentes elosztások, Conway-Selfridge-eljárás

### A mozgó késes eljárás diszkrét változata

Minden játékos megjelöli a saját értékelő függvénye szerint az aktuálisan legjobbnak tűnő szeletet, ami neki megfelel. A legjobbnak jelölővel rendelkező játékos megkapja a kért szeletét, és a többi játékos a megmaradt intervallumon folytatja az eljárást.

### Even-Paz-eljárás

Minden játékos megjelöli a saját értékelő függvénye szerint $\lfloor n/2 \rfloor$, $\lceil n/2 \rceil$-ig tartó részt. Vágjuk el az intervallumot a balról számított $\lfloor n/2 \rfloor$-edik osztópontnál (a többi játékos által is megjelölt osztópontokat megfelelő multiplicitással számoljuk). A vágástól balra jelölő játékosok a baloldali részen, a többiek a jobboldali részen osztoznak tovább az Even-Paz-eljárással.

### Conway-Selfridge-eljárás

Három játékos osztozkodik: $A, B, C$

1. $A$ három egyenlő részre osztja az intervallumot.
A szeletek $B$ preferencia sorrendjében legyenek: $X, Y, Z$
2. $B$ $X$-ből levág egy $X^*$ darabot úgy, hogy a maradék $X'$ és $Y$ egyformák legyenek.
3. $X', Y, Z$-ből $C \rightarrow B \rightarrow A$ sorrendben váalsztanak. Ha $B$ választhatja $X'$-t, akkor azt választja.
4. $P(X)$: az $X'$-t megkapó játékos $\in \{B, C\} P(\overline{X'}) = B$ és $C$ az, aki nem $X'$-t kapta.
5. $P(\overline{X'})$ három egyforma részre osztja az $X^*$-ot, majd ebből választanak
$P(X') \rightarrow A \rightarrow P(\overline{X'})$ sorrendben.

## 11. Csődjáték, kelmeszabály, kelmeszabály-konzisztens szétosztás, Kamiński-féle közlekedőedény-rendszer. A csődjáték nukleólusza, Aumann-Maschler-tétel*

### Kelmeszabály

- Ketten osztozkodnak és többet követelnek, mint a vagyon
- Mindketten megkapják a másik által nem követelt részt, míg a vitatott részen egyenlően osztoznak.

### Csődprobléma

Meghal egy ember, aki $E$ nagyságú vagyont és $d_1, d_2,..., d_n$ nagyságú adósságot hagyg hátra. Hogyan kell kifizetni a hitelezőket, ha $\sum_id_i > E$.

#### Formális probléma

A **csődproblémát** az $E$ vagyon nagyság és a $d_1 \leq d_2 \leq \dots \leq d_n$ követelések írják le, ahol $0 \leq E \leq d_1 + d_2 + \dots + d_n$.

**Definíció:**
A csődprobléma esetén `szétosztásnak` egy nemnegatív valós számokból álló olyan $(x_1, x_2, \dots, x_n)$ rendezett $n$-est nevezünk, amire $E = x_1 + x_2 + \dots + x_n$.

Ha $n = 2$, akkor a ksz egy lehetséges szétosztást adó eljárás.

**Definíció**
Az $(x_1, x_2, \dots, x_n)$ szétosztás `ksz-konzisztens`, ha bármely $i, j$-re az $x_i + x_j$ nagyságú vagyon $d_i, d_j$ követelésekhez a ksz szabály $x_i$ és $x_j$ részeket rendel.

**Azaz:** Ha két hitelező az általuk kapott részt a ksz szerint újraosztja, akkor a korábbi jussukat kapják vissza.

**Megfigyelés:**
A Talmudbeli szétosztások ksz-konzisztensek.

**Kínzó kérdés:**
Létezik-e minden csődproblémára ksz-konzisztens szétosztás?

**Részleges válasz:**
Ha van, akkor egyértelmű.

### Kamiński-féle közlekedőedény-rendszer

Tfh mindkét hitelezőhöz tartozik egy-egy azonos keresztmetszetű, $d_1$ ill. $d_2$ térfogatú, hengeres tartály. Vágjuk félbe a tartályokat, kössük össze ezeket vékony csövekkel, és töltsük fel $E$ (vagyon nagyság) mennyiségű folyadékkal az így kapott közlekedőedény-rendszert.

„Könnyen” látható, hogy folyadék épp a ksz szerint oszlik meg az egyes tartályokban.

Így már nem nehéz ksz-konzisztens szétosztást találni: minden hitelezőhöz tartozzon egy-egy követelésnyi térfogatú tartály, kössük össze ezeket vékony csövekkel, és töltsük fel $E$ mennyiségű folyadékkal a kapott rendszert.

### A csődjáték nukleólusza

Egy $S$ koalíció `többlete` annyi amennyit az értéken felül kap.

---

A `töbletvektor` a többletekből áll, növekvő sorrendben.

Például:

$\theta{(x)} = (33.3, 66.6, 66.6, 100, 100, 133.3)$

---

A `nukleolusz` az a szétosztás, ami lexikografikusan maximalizálja a többletvektort. Azaz: az első
koordináta maximális, ezen belül a második, stb.

### Aumann-Maschler-tétel

A ksz-konzisztens szétosztás a csődjáték nukleólusza.

## 12. Szavazási modell. Egyhangú és lényegtelen alternatíváktól független szavazási mechanizmusok. Társadalmi választási függvények és szabályok kapcsolata. Extrém alternatíva, lemma az extrém alternatívákról

### Szavazási modell

Az alábbi szavazási modellben dolgozunk. Adott a szavazók $N = \{1, 2, \dots, n\}$ és az alternatívák $A = \{a_1, \dots, a_k\}$ halmaza, $L$ pedig az $A$ alternatívahalmaz lineáris rendezéseit jelöli.

Feltesszük, hogy minden szavazó preferenciáját egy $L$-beli lineáris rendezés írja le (az $i$-dik szavazóét $\preceq_i$ jelöli), és rögzítjük, hogy a szavazás végeredménye csak ezektől a preferenciáktól függhet, ahol $a \prec_i b$ jelentése az, hogy az $i$-dik szavazó számára a $b$ alternatíva jobb az $a$ alternatívánál. A $\preceq$ preferenciarendezés szerint legjobban preferált alternatívát $Top(\preceq)$ jelöli.

**Választási profil** egy, a szavazók preferenciáit felsoroló $\Pi = (\preceq_1, \dots, \preceq_n)$
vektor. A szavazás kimenetele pedig egy függvény által meghatározott $L$-beli közös preferenciarendezés
 vagy egy $A$-beli alternatíva.

**Társadalmi választási szabály (TVSZ)** alatt egy $F : L^n \to L$ függvényt,  
**Társadalmi választási függvény (TVF)** alatt pedig egy $F : L^n \to A$ leképezést értünk.

### Egyhangú és lényegtelen alternatíváktól független szavazási mechanizmusok

Az $F$ TVSZ `egyhangú`, ha minden $(a,b)$ alternatívapárra igaz az alábbi tulajdonság.
Ha $a \preceq_i b$ minden 1 $i$-re akkor $a \preceq b$ teljesül a $\preceq = F(\Pi)$ közös döntésre.

Az $F$ **TVSZ** `független a lényegtelen alternatíváktól`, ha minden $(a, b)$ alternatívapárra az alábbi tulajdonság teljesül.

Ha $\Pi = (\preceq_1, \dots, \preceq_n)$ és $\Pi' = (\preceq'_1, \dots, \preceq'_n)$ olyan választási profilok, amelyekben minden szavazó egyformán rendezi az $(a, b)$ párt, akkor az $F(\Pi)$ és $F(\Pi')$ közös preferenciák is egyformán rendezik az $(a, b)$ párt.

**Ugyanez formulákkal, precízen:**

Ha $(a \preceq_i b \iff a \preceq'_i b \ \forall i \in N)$ akkor $(a \preceq b \iff a \preceq' b),$ ahol $\preceq = F(\Pi)$ és $\preceq' = F(\Pi')$.

Ilyen mechanizmusok:

- `Jóváhagyásos szavazás:`

 1. **Szavazás:** Minden szavazó tetszőleges számú alternatívát jóváhagyhat
 2. **Győztes:** Az az alternatíva nyer, amelyiket a legtöbben jóváhagyták.

- `Többségi szavazás:`

 1. **Szavazás:** Minden szavazó egy alternatívát választ.
 2. **Győztes:** Az az alternatíva nyer, amelyiket a legtöbben választottak.

- `Borda-szavazás:`

 1. **Rangsorolás:** Minden szavazó rangsorolja az összes alternatívát. Ha van $( k )$ alternatíva, akkor az első helyezett $(k-1)$ pontot kap, a második helyezett $(k-2 )$ pontot, és így tovább, az utolsó helyezett 0 pontot kap.

 2. **Pontok összesítése:** Az összes szavazó által adott pontokat összeadják minden alternatívára.

 3. **Győztes meghatározása:** Az az alternatíva nyer, amelyik a legtöbb pontot kapta.

- `Copeland-szavazás`

 1. **Páros összehasonlítások:** Minden alternatívát összehasonlítanak minden más alternatívával egy-egy páros versenyben. Az egyes páros versenyekben az az alternatíva nyer, amelyik több szavazatot kap.

 2. **Pontozás:** Minden alternatíva kap egy pontot minden egyes nyert páros versenyért, és fél pontot minden döntetlenért.

 3. **Győztes meghatározása:** Az az alternatíva nyer, amelyik a legtöbb pontot gyűjtötte össze a páros versenyek során.

- `Condorcet-szavazás`

 1. **Páros összehasonlítások:** Minden alternatívát összehasonlítanak minden más alternatívával egy-egy páros versenyben. Az egyes páros versenyekbennaz az alternatíva nyer, amelyik több szavazatot kap.

 2. **Győztes meghatározása:** Az az alternatíva nyer, amelyik minden más alternatívával szemben nyer.

### Extrém alternatíva

Az alternatívák egy $\preceq$ rendezésében a $\preceq$ szerinti legjobb és legrosszabb alternatívát `extrémnek` nevezzük.

### Lemma az extrém alternatívákról

Tegyük fel, hogy az $F$ TVSZ független a lényegtelen alternatíváktól. Ha ekkor T extrém alternatíva a $\Pi$ választási profilban szereplő minden $\preceq_i$ preferenciarendezésben, akkor T extrém alternatíva a közös $F(\Pi)$ rendezésben is.

## 13. Jóváhagyásos, többségi, diktatórikus szavazás. Borda- és Copeland-szavazások. Condorcet-győztes, Condorcet-konzisztencia. Arrow-tétel*

- `Jóváhagyásos szavazás:`

 1. **Szavazás:** Minden szavazó tetszőleges számú alternatívát jóváhagyhat
 2. **Győztes:** Az az alternatíva nyer, amelyiket a legtöbben jóváhagyták.

- `Többségi szavazás:`

 1. **Szavazás:** Minden szavazó egy alternatívát választ.
 2. **Győztes:** Az az alternatíva nyer, amelyiket a legtöbben választottak.

- `Borda-szavazás:`

 1. **Rangsorolás:** Minden szavazó rangsorolja az összes alternatívát. Ha van $( k )$ alternatíva, akkor az első helyezett $(k-1)$ pontot kap, a második helyezett $(k-2 )$ pontot, és így tovább, az utolsó helyezett 0 pontot kap.

 2. **Pontok összesítése:** Az összes szavazó által adott pontokat összeadják minden alternatívára.

 3. **Győztes meghatározása:** Az az alternatíva nyer, amelyik a legtöbb pontot kapta.

- `Diktatórikus szavazás:`

 1. **Szavazás:** Egy diktátor minden szavazásban egy alternatívát választ.
 2. **Győztes:** Az a alternatíva nyer, amelyiket a diktátor választott.

- `Copeland-szavazás`(*Concordet konzisztens*)

 1. **Páros összehasonlítások:** Minden alternatívát összehasonlítanak minden más alternatívával egy-egy páros versenyben. Az egyes páros versenyekben az az alternatíva nyer, amelyik több szavazatot kap.

 2. **Pontozás:** Minden alternatíva kap egy pontot minden egyes nyert páros versenyért, és fél pontot minden döntetlenért.

 3. **Győztes meghatározása:** Az az alternatíva nyer, amelyik a legtöbb pontot gyűjtötte össze a páros versenyek során.

### Condorcet-győztes

Az az alternatíva, amelyik minden más alternatívával szemben nyer a páros versenyekben.

- `Condorcet-szavazás`

 1. **Páros összehasonlítások:** Minden alternatívát összehasonlítanak minden más alternatívával egy-egy páros versenyben. Az egyes páros versenyekben az az alternatíva nyer, amelyik több szavazatot kap.

 2. **Győztes meghatározása:** Az az alternatíva nyer, amelyik minden más alternatívával szemben nyer.

### Condorcet-konzisztencia

Egy szavazási mechanizmus `Condorcet-konzisztens`, ha a Condorcet-győztes nem veszíthet.

### Arrow-tétel

Ha $|A| > 2$, továbbá az $F$ TVSZ egyhangú és független a lényegtelen alternatíváktól, akkor $F$ diktatórikus.

## 14. Szavazási mechanizmusok manipulálhatósága és taktikázásbiztossága. Gibbard-Satterthwaite-tétel*

### Manipulálhatóság

Az $f : L^n \rightarrow A$ TVF manipulálható, ha van olyan $\Pi = (\preceq_1,...,\preceq_n)$ választási profil és $\preceq_i'$ preferenciarendezés, amire $f(\Pi) \preceq_i f(\Pi_{-i}, \preceq_i')$ teljesül. Ha egy $f$ TVF nem manipulálható, akkor $f$-et taktikázásbiztosnak is nevezzük.

### Szürjektívítás

Az $f : L^n \rightarrow A$ TVF szürjektív, ha minden $a \in A$ alternatíva esetén van olyan $\Pi = (\preceq_1,...,\preceq_n)$ választási profil, amire $f(\Pi) = a$.

Vagyis szurjektivitás a szavazási elméletben azt jelenti, hogy az alternatívák halmazában ($A$) minden lehetséges kimenetelhez (alternatívához) létezik legalább egy olyan szavazási profil ($\Pi$), amelyben az adott kimenetel kerül kiválasztásra. Ez biztosítja, hogy a szavazási függvény ($f$) bármilyen lehetséges kimenetelt elő tud állítani a megfelelő szavazói preferenciák megadása esetén.

### Gibbard-Satterthwaite-tétel

Ha az $f$ TVF taktikázásbiztos, szürjektív és $|A| \geq 3$, akkor $f$ diktatórikus.

## 15. Árverési mechanizmusok, taktikázásbiztosság, szubvenció- és veszteségmentesség. Második áras árverés, Clarke-szabállyal definiált Vickrey-Clarke-Groves-mechanizmus, és annak taktikázásbiztossága*

Adott a licitálók $N = \{1, 2, \dots, n\}$ és az alternatívák $A$ halmaza. Az $i$-edik licitáló számára az $a \in A$ alternatíva értékét $\hat{v_i}(a) \in \mathbb{R}$ jelöli. Ennyi pénzt ér meg az $i$-edik licitáló számára az a kimenet, hogy a végső döntés az alternatíva kiválasztása. Az árverés során minden licitálónak meg kell adnia egy licitet. A licit nem más, mint minden alternatívához egy licitérték hozzárendelése. Az $i$-edik licitáló licitje tehát egy $v_i : A \to \mathbb{R}$ függvény, ahol $v_i(a)$ jelenti az $i$-edik licitálónak az $ a $ alternatívára vonatkozó licitjét. Az $i$-edik licitáló lehetséges licitjeinek halmazát $S_i$ jelöli, $S = S_1 \times S_2 \times \cdots \times S_n$ pedig a lehetséges licitprofilok halmaza: ha $v \in S$, akkor $v = (v_1, \dots, v_n)$. (Itt is elkövettük a jelölésrendszer korábban megszokott abúzusát, és $(v_{-i}, \hat{v}_i)$-val ezt a licitprofilt jelöljük, amit $v$-ből úgy kapunk, hogy az $i$-edik licitjét $v_i$-ből $\hat{v}_i$-re cseréljük.)

### Árverési mechanizmusok

Az árverési mechanizmus egy $\mathcal{M} = (f, p_1, \dots, p_n)$ $(n + 1)$-es, ahol $f : S \to A$ és $p_i : S \to \mathbb{R}$ függvények. Az $\mathcal{M}$ árverési mechanizmus a következőképp működik: a licitálók licitjei alapján az $f$ licitprofil független alternatívát választ ki, azaz $f(v) \in A$, és ezért a licitálók kifizetéseit a $p$ függvények írják le, azaz $i$-edik konkrétan $p_i(v)$ összeget fizet. Miután ez az árverés lezajlott, az $i$-edik licitáló nyeresége a kimeneti alternatíva értéke az $i$-edik licitáló számára különbsége a kifizetése és a választott alternatíva értéke között :

$$
u_i(v) = v_i(f(v)) - p_i(v).
$$

### Taktikázásbiztosság

Egy fontos tulajdonság, a **taktikázásbiztosság** azt jelenti, hogy az $i$-edik licitáló úgy ér el maximális nyereséget, ha az igazat mondja, azaz valódi értékfüggvényét adja meg licitként, minden esetben, amikor az összes többi licitáló is így tesz. Az ilyen árverési mechanizmusokat taktikázásbiztosnak nevezzük. A pontos definíció a következő:

Az $\mathcal{M} = (f, p_1, \dots, p_n)$ árverési mechanizmus `taktikázásbiztos`, ha

$$
u_i(v_{-i}, \hat{v}_i) \leq u_i(v_{-i}, v_i)
$$

teljesül minden $v \in S$ licitprofilra és minden $i \in N$ licitálóra.

### Szubvenció- és veszteségmentesség

Egy konkrét VCG-mechanizmust akkor nevezünk `szubvenciómentesnek`, ha $p_i(v) ≥ 0$ teljesül minden $v ∈ S$ licitprofil és minden $i ∈ N$ licitáló esetén.

Egy konkrét VCG-mechanizmust akkor nevezünk `veszteségmentesnek`, hogyha egy licitáló őszintén licitál, akkor nem éri veszteség.

### Második áras árverés

Minden licitáló megad egy licitet, és a nyertes az lesz, aki a legtöbbet ajánlja. A nyertes a második legmagasabb licit összegét fizeti.

### Clarke-szabállyal definiált Vickrey-Clarke-Groves-mechanizmus, és annak taktikázásbiztossága*

#### Clarke-szabály

$$
h_i(\underline{V_{-i}}) = max_{a \in A}\sum_{i \neq j}v_j(a)
$$

#### Vickrey-Clarke-Groves-mechanizmus

$\underline{V}_{-i} \in S$-re $f(\underline{V})$ az az $a\in A$ alternatíva, ami maximalizálja a $V_1(a) + V_2(a) + \dots + V_n(a)$ összértéket.

$p_i(\underline{V}) = h_i(\underline{V}_{-i}) - \sum_{j \neq i}v_j(f(\underline{X}))$, ahol $h_i$ egy rögzített függvény.

***taktikázásbiztos***

## 16. Újraosztási feladat, erős mag. Felső körcsere (TTC) algoritmus. Shapley-Scarf-tétel*

### Újraosztási feladat

Az újraelosztási feladatban minden játékos rendelkezik egy-egy jószággal, és bár ennél többre nincs ugyan szüksége, irigyelheti más játékos jószágát. Úgy szeretnénk újraelosztani a játékosok között a javaikat, hogy senki se járjon rosszul (ami önmagában nem nehéz: mindenki tartsa meg a maga jószágát), és emellett mindenki a számára lehető legjobbat kapja a számára elérhető jószágok közül. Az irodalomban lakáspiac néven fut ez a modell, aholis a játékosok $N = \{1,2,..., n\}$ halmazának elemei a lakástulajdonosok, a jószágok pedig a lakásaik. Minden lakástulajdonos rendelkezik egy preferenciarendezéssel a piacon található lakásokon (az i tulajdonosét, jelöli), ami formálisan egy lineáris rendezés az N halmazon: $j \preceq_i k$ azt jelenti, hogy az $i$ tulajdonos számára a $k$ tulajdonos lakása jobb, mint a j tulajdonosé. A probléma inputja tehát a tulajdonosok N halmaza és a $\Pi = (\preceq_1,...,\preceq_n) \in P^n$ preferenciaprofil, ahol $P$ jelöli az $N$ halmaz lineáris rendezéseinek halmazát. Az újraelosztási mechanizmus egy $f: P^n \rightarrow S_N$ leképezés, ahol $S_y$ az $N$ halmaz permutációinak halmazát jelöli. A mechanizmus által szolgáltatott konkrét újraelosztást az $f(\Pi) = \sigma$ output-permutáció írja le: $\sigma(i) = j$ azt jelenti, hogy az $i$ lakástulajdonos a $j$ tulajdonos lakását kapja a sajátjáért cserébe (amit persze a $σ^{-1} (i)$ tulajdonos fog elfoglalni). Az újraelosztási mechanizmussal kap- csolatban természetes az alábbi elvárás.


#### Gyengén blokkoló koalíció

Legyen $σ∈ S_N$ egy rögzített újraelosztás. Lakástulajdonosok egy $B \subseteq N$ halmaza a $\sigma$ újraelosztást gyengén blokkoló koalíciót alkot, ha a $B$-beli tulajdonosok el tudják osztani a saját lakásaikat egymás között úgy, hogy senki se járjon rosszabbul, mint a $\sigma$ újraelosztás mellett, és legalább egy $B$-beli tulajdonos helyzete határozottan javuljon $\sigma$-hoz képest. Formálisan: a $B$ halmaz akkor blokkolja gyengén $\sigma$-t, ha van olyan ∈ S_B permutáció $B$-n és olyan $i ∈ B$ tulajdonos, hogy $\sigma(i) \preceq_i π(i)$ mellett $\sigma(j) \preceq_j π(j)$ teljesül minden $j ∈ B$ lakástulajdonosra.
Az erős mag mindazon $\sigma∈ S_N$ újraelosztásokból áll, amelyeket egyetlen koalíció sem blokkol gyengén.

### Erős mag

Az erős mag azon $\sigma \in S_N$ újraelosztások halmaza, amelyeket egyetlen koalíció sem blokkol gyengén.

### TTC algoritmus

Minden tulajdonos rámutat a számára legjobb lakásra(akár a sajátjára). Gráfként ábrázolva minden ki-fok = 1 --> létezik kör.

$N_1$: Kör mentén a $\rightarrow$ lakástulajdonosok halmaza

$N_1$ Cserél egymás közt a kör mentén és az eljárást $N - N_1$-en folytatjuk.

Az eljárárás végén kapjuk a $\sigma$ szétosztást.

### Shapley-Scarf-tétel

A TTC outputja  az erős mag egyetlen eleme.

## 17. Csoportos taktikázásbiztosság fogalma, a felső körcsere algoritmus csoportos taktikázásbiztossága*, Piaci egyensúly létezése és erős magbelisége*

### Csoportos taktikázásbiztosság

Egy mechanizmus akkor `csoportosan taktikázásbiztos`, ha a lakástulajdonosok egyetlen részhalmaza sem képes úgy meghamisítani a preferenciáit, hogy a mechanizmus futtatása után egyikük se járjon rosszabbul, mint a valódi preferenciáik megadásával, de legyen közöttük legalább egy olyan lakástulajdonos, aki határozottan profitál a hamisításból.

### Felső körcsere algoritmus csoportos taktikázásbiztossága*

A felső körcsere algoritmus csoportosan taktikázásbiztos a lakáspiac-modellben megfogalmazott újraelosztási feladatra.

**Bizonyítás:**

 Tegyük fel, hogy a felső körcsere algoritmus outputja a $\sigma = f(\Pi)$ permutáció, $M \subseteq N$ a lakástulajdonosok egy tetszőleges részhalmaza és és $\Pi_M \in P^{|M|}$ egy preferenciaprofil $M$-en. Futtassuk a felső körcsere algoritmust a $\Pi$ és a $\Pi' = (\Pi_{-M}, \Pi_M)$ profilokon, utóbbi esetben az $M$-beli tulajdonosok $\Pi$-beli preferenciáit cseréljük ki a $\Pi_M$-beliekre. Azt fogjuk igazolni, hogy ha $σ' = f(Π') ≠ 0$, akkor van olyan $M$-beli tulajdonos, aki rosszabb lakást kap az ügyeskedés miatt, azaz $\sigma'(i) \preceq_i \sigma(i)$.

$\Pi$-n ill. $\Pi'$-n futtatott TTC által eliminált közös körökben szereplő tulajdonosok elhagyásával elérhetjük, hogy a felső körcsere algoritmus futtatásával kapott $\sigma$ és $\sigma'$ kimenetekben szereplő körök páronként különbözők legyenek. Legyen tehát $C$ a legelső cserekör, amit a $\Pi$ profilon futtatott felső körcsere algoritmus megtalál. A feltevés miatt C-ben van olyan $i$ tulajdonos, akire $σ(i) ≠ \sigma'$(i), azaz különböző lakást kap, mint ha $\Pi'$-n futtatnánk a TTC-t. Ekkor $σ' (i) \preceq_i σ(i)$, hiszen $σ(i)$ első helyen áll az $i$ tulajdonos preferenciarendezésében. Ez egyúttal azt is jelenti, hogy $\preceq_i'≠ \preceq_i$, azaz az $i$ tulajdonos nem a $\Pi$-beli preferenciáival vesz részt a TTC-ben, ezért aztán $i ∈ M$. Ezek szerint az $M$-beli tulajdonosok nem tudják sikeresen manipulálni a TTC algoritmust, ez pedig a tételben állított csoportos taktikázásbiztosságot igazolja

### Piaci egyensúly létezése és erős magbelisége*

Az $N$ tulajdonsághalmaz és $\Pi = (\preceq_1,...,\preceq_n)$ preferenciaprofil által meghatározott lakáspiacon a $p : N \rightarrow \mathbb{R}_+$ leképezés és $\sigma \in S_N$ együttesét `piaci egyensúlynak` nevezzük, ha $p(\sigma(i)) \leq p(i)$ melett $i \preceq_i j \Rightarrow p(j) > p(i)$ teljesül minden $i, j \in N$ esetén.

#### Lemma

Tegyük fel, hogy $(p, \sigma)$ piaci egyensúly az $(N, \Pi)$ lakáspiacon és $C$ egyolyan kör, aminek a mentén a tulajdonosok lakást cserélnek a $\sigma$ permutációban. Ekkor $p(i) = p(j)$ teljesül minden $i, j \in C$ tulajdonosra, azaz a piaci egyensúlyban szereplő lakáscserék során minden tulajdonos a lakásának teljes vételárát az új lakásra fordítja.

### Erős magbeliség

Tegyük fel, hogy $(p, \sigma)$ piaci egyensúly az $(N, \Pi)$ lakáspiacon. Ekkor $\sigma$ az `erős mag egyik eleme`.

## 18. Stabil párosítások. Éltörlési lemma, lánykérő algoritmus, fiú-optimalitás. Stabil párosítások által fedett csúcshalmaz

### Stabil párosítások

Az általános házassági modellben dolgozunk. A játékosok mindegyike vagy fiú vagy lány és a köztük lehetséges házasságokat egy $G$ páros gráf írja le: ennek színosztályai a fiúk $F$ és a lányok $L$ halmazai, és egy $f$ él jelentése az, hogy $f$ és $l$ között lehetséges a házasság. Minden játékos rendelkezik egy $\preceq_a$ lineáris preferenciarendezéssel az $a$-ra illeszkedő éleken, azaz a potenciális házastársain. A cél egy $M$ párosítás mentén úgy összeházasítani a játékosokat, hogy lehetőleg senki se legyen elégedetlen. Ez utóbbi feltétel most a maghoz tartozást jelenti, azaz ne legyen az $M$ párosítás mellett blokkoló koalíció. Játékosok egy $B$ részhalmaza akkor blokkoló koalíció $M$-re nézve ha a $B$-beli játékosok képesek arra, hogy önerőből javítsák a helyzetüket, azaz ha van olyan $N$ párosítás $B$-n, ami egyetlen $B$-beli játékos számára sem rosszabb $M$-nél, de van legalább egy olyan $B$-beli játékos, aki $N$-nel jobban jár, mint $M$-mel. Utóbbi kitétel azt jelenti, hogy $b$ jobb párt kap $N$-ben, mint $M$-ben, vagy pedig $b$ fedetlen $M$-ben, de van párja $N$-ben.

Vizsgáljuk meg, hogyan is néz ki egy blokkoló koalíció! Tegyük fel, hogy a $B$ koalíció az $N$ párosítás mentén blokkolja az $M$ párosítást. Van tehát egy olyan $ba ∈ N$ él, amivel $b$ jobban jár az $M$-beli helyzetéhez képest. Ez azt jelenti, hogy a nem $b$-val élő párban $M$-ben, és mivel $a ∈ B$ is teljesül, ezért $a$-nak is jobban kell járnia a $ba$ éllel, mint $M$-mel. Ez azt jelenti, hogy tetszőleges $B$ blokkoló koalíció tartalmaz egy kétfős blokkoló koalíciót. Ezért a maghoz tartozás eldöntésekor a fenti definíció helyett elegendő csupán annyit megkövetelni, hogy ne legyen blokkoló él, azaz kétfős blokkoló koalíció.

Adott a $G = (V, E)$ gráf és minden $v ∈ V$ csúcshoz a $v$-re illeszkedő élek $E(v)$ halmaza, ahol a $v$ csúcs preferenciáját leíró $≻v$ lineáris rendezés. Azt mondjuk, hogy $v$ számára az $e$ él jobb az $f$ élénél, ha $f ≻v e$. A $G$ gráf $M$ párosítása mellett az $uv$ él akkor nevezünk tehát blokkoló élnek, ha $u$ és $v$ is jobban jár az $uv$ éllel, mint $M$-mel, azaz ha $M$ alatt nem tartoznak olyan él sem, ami $u$ számára és olyan él sem, ami $v$ számára jobb az $uv$ élénél. Ha az $M$ párosítás mellett nincs blokkoló él, akkor $M$-et `stabil párosításnak` nevezzük.

### Éltörlési lemma

Legyen $G = (V,E)$ irányítatlan gráf és legyen $\preceq_v$ lineáris rendezés a $v$-re illeszkedő élek $E(v)$ halmazán minden $v \in V$ esetén. Tegyük fel, hogy az $u$ csúcs legjobb éle $e = uv$, és $e \succ_v f = wv$, azaz $v$ számára $e$ jobb, mint $f$. Ekkor a $G$ és a $G - f$ gráfoknak ugyan azok a stabil párosításai.

### Lánykérő algoritmus

1. Minden fiú megkéri a számára legszimpatikusabb lányt.
2. Minden lány a legjobb kivételével visszautasítja a kérőit.
3. Ha nem történt elutasítás, akkor vége a folyamatnak.
4. Ha volt elutasítás, akkor a fiúk, akiket elutasítottak, megpróbálják a következő legszimpatikusabb lányt megkérni.

**Output:**

- Stabil párosítás
- `Fiú optimális`, vagyis minden fiú számára a legjobb lányt kapja. Míg minden lány a legrosszabb olyan fiút kapja, aki a párosításban számára elérhető.

### Stabil párosítások által fedett csúcshalmaz

Ha $M_1$ és $M_2$ az élpreferenciákkal ellátott (nem feltétlen páros) $G$ gráf két stabil párosítása, akkor $V(M_1) = V(M_2)$, azaz a $G$ gráf bármelyik stabil párosítását is választjuk, mindig ugyanazok a csúcsok lesznek kipárosítva és ugyanazok maradnak fedetlenek.

## 19. Egyetemi felvételi probléma és annak visszavezetése stabil párosítások keresésére. Ponthatárhúzási feladat, stabil ponthatár. Ponthatárnövelő és -csökkentő algoritmus, valamint azok helyessége*

### Felvételi séma

`Felvételi séma` alatt egy olyan $F ⊆ E$ élhalmazt értünk, amelyikre igaz, hogy minden $t ∈ T$ jelentkező legfeljebb 1, minden $s$ szak pedig legfeljebb $q_s$ $F$-beli élnek csúcsa. Egy felvételi séma tehát jelentkezések egy olyan halmaza, ami megvalósítható: egyetlen jelentkezőnek sem tartalmazza egynél több jelentkezését és egyetlen szak hallgatói létszáma sem haladja meg az adott szak keretszámát.

### Stabil felvételi séma

Egy $F$ felvételi séma akkor `stabil`, ha egyetlen él sem blokkolja. Itt blokkoló élen olyan $e = ts$ él értünk, amivel mindkét végpontja jobban járna, mint a séma szerinti élekkel: egyrészt tehát nincs olyan $f ∈ F$ él amire $e \preceq_t f$, másrészt pedig nincsenek olyan $f₁, ..., fₓ ∈ F$ élek sem, amelyekre $e \preceq_s fᵢ$ teljesül $i = 1, ..., q_s$ esetén. Egy $ts$ él tehát blokkol, ha a $t$ jelentkező felvették az $s$ szaknál preferáltabb szakra vagy ha az $s$ szak a teljes keretszámát egytől egyig tőle gyengébb jelentkezőkkel töltötte fel.

Az egyetemi felvételi probléma esetén a feladat egy stabil felvételi sémát keresése a fent leírt modellben. Világos, hogy ha minden létszámkorlát pontosan 1, akkor az egyetemi felvételi probléma egy páros gráf stabil párosításának keresésével ekvivalens. Megmutatjuk, hogy az egyetemi felvételi probléma 1-nél nagyobb keretszámok esetén is visszavezethető páros gráf stabil párosításának keresésére.

### Stabil párosítások keresésére viszavezetés

A $G = (S ∪ T, E)$ gráf, ${q_s : s ∈ S}$ keretszámok és ${≻ₛ : s ∈ S}$, ${≻ₜ : t ∈ T}$ ill. ${≻ₛ : s ∈ S'}$ preferenciák által definiált egyetemi felvételi problémában $F$ pontosan akkor stabil felvételi séma, ha a $G'$ gráfnak van olyan $F'$ stabil párosítása, amire $F = P(F')$ teljesül.

### Ponthatárhúzási feladat

Az előző részben tárgyalt egyetemi felvételi modell lényeges leegyszerűsítést tartalmaz a valósághoz képest. Magyarországon ugyanis az egyetemi szakok preferenciáját a jelentkezőkön nem egy lineáris rendezés, hanem egy pontszámokon alapuló rangsor határozza meg. Ezért bármely szak jelentkezői között előfordulhat pontszámegyenlőség. A jogi környezet azonban nem engedi meg, hogy ugyanarra a szakra azonos felvételi pontszámmal rendelkező jelentkezők különböző elbírálásban részesüljenek. Ezért nem egy felvételi séma explicit meghatározásával, hanem implicit módon, egy ponthatár megállapítása révén dől el, hogy az egyes jelentkezők melyik szakra nyernek felvételt.

### Stabil ponthatár

Egy $l$ ponthatár pontosan akkor stabil, ha $l$ a $φ$ operátor fixpontja, azaz ha $l = φ(l)$ teljesül. Vagyis ha a minimum ponthatár, amivel még nem lépjük túl a keretszámokat megegyezik a ponthatárral.

### Ponthatárnövelő és -csökkentő algoritmus

Tetszőleges vonalhúzási probléma esetén van stabil ponthatár. A ponthatárnövelő ill. a ponthatárcsökkentő algoritmusok $\underline{ℓ}$ ill. $\overline{ℓ}$ outputjai stabil ponthatárok, és tetszőleges $ℓ$ stabil ponthatárra $ℓ ≤ ℓ ≤ \overline{ℓ}$ teljesül.

Ha $ℓ ≤ ℓ'$ stabil ponthatárok, akkor az $ℓ$ ponthatár alkalmazása esetén legalább annyi jelentkezőt vesznek fel, mint az $ℓ'$ ponthatár alkalmazásával. Következésképp a legtöbb jelentkező a jelentkező-optimalis ponthatár alkalmazása esetén nyer felvételt.

#### $\varphi$ monoton

$0 \leq \varphi(0) \leq \varphi(\varphi(0)) \leq \dots \varphi^{(k)}(0) \leq \dots$

lesz olyan, hogy $\varphi^{(k)}(0) = \varphi^{(k+1)}(0)$, azaz $\underline{ℓ} = \varphi^{(k)}(0)$ stabil ponthatár.

belátható ez a

$500 \geq \varphi(500) \geq \varphi(\varphi(500)) \geq \dots \varphi^{(k)}(500) \geq \dots$ esetre is.

---

$Bizonyítás.$ Csupán a tétel második bekezdése szorul bizonyításra, az első részt még a tétel kimondása előtt igazoltuk. A második részhez pedig mindössze annyit kell megfigyelni, hogy egy jelentkező felvétele pusztán azon múlik, hogy van-e eredményes jelentkezése.

Márpedig ha egy $t$ jelentkezőnek az $s$ szakra történő jelentkezése az $ℓ'$ ponthatár esetén eredményes, akkor ugyanez a jelentkezés $ℓ$ esetén is eredményes. Ezért aztán minden jelentkező, akit az $ℓ'$ ponthatár mellett felvesznek valamelyik szakra, felvételt nyer valahova az $ℓ$ ponthatár alkalmazása esetén is.

## 20. Népszerű párosítások, stabil párosítások népszerűsége, Kavitha-algoritmus, és annak helyessége*

### Népszerű párosítások

M párosítás `népszerűbb` az N párosításnál, ha az M és N közti választás esetében többen szavaznak M-re, mint N-re.

### Stabil párosítások népszerűsége

Ha $M$ stabil, akkor nem létezik $M$-nél kevesebb élt tartalmazó stabil párosítás.

Ha $M'$ a $G = (S ∪ T, E)$ gráf stabil párosítása, akkor $M'$-nek megfelelő $G$-beli élek $M = \{e \in E : \{e^p, e^z\} \cap M' \neq \emptyset \}$

### Kavitha-algoritmus

A Kavitha-algoritmus egy olyan algoritmus, amely népszerű párosításokat talál egy gráfban. Az alábbiakban bemutatom, hogyan működik a Kavitha-algoritmus:

#### Lépések

1. **Kezdeti párosítás**: Kezdjünk egy tetszőleges párosítással $M$ a gráfban $G = (S \cup T, E)$.

2. **Preferenciák meghatározása**: Minden csúcs $s \in S$ és $t \in T$ preferenciákat rendel az élekhez. Azaz, minden csúcs rangsorolja az összes hozzá kapcsolódó élt.

3. **Népszerűségi feltétel ellenőrzése**: Ellenőrizzük, hogy a jelenlegi párosítás $M$ népszerű-e. Egy párosítás akkor népszerű, ha nincs olyan másik párosítás, amelyet több csúcs preferál $M$-hez képest.

4. **Javítási lépések**: Ha $M$ nem népszerű, akkor keressünk egy olyan élt, amely javíthatja a párosítást. Ezt úgy tehetjük meg, hogy egy augmentáló utat keresünk, amely növeli a párosítás méretét vagy javítja a népszerűséget.

5. **Párosítás frissítése**: Frissítsük a párosítást az augmentáló út mentén. Ez azt jelenti, hogy az augmentáló út mentén váltogatjuk a párosított és nem párosított éleket.

6. **Ismétlés**: Ismételjük meg a népszerűségi feltétel ellenőrzését és a javítási lépéseket, amíg nem találunk népszerű párosítást.

A kikosarazott fiúk "személyiségfejlesztő trainingen" vesznek részt, ahonnan a lehető legnépszerűbben térnek vissza. Trainingre csak egyszer lehet menni.

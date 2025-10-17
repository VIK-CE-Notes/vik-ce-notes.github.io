# Matematikai kifejezések

A jegyzetben sok matematikai kifejezéssel találkozhatunk, melyeknek egy részét a tárgy már feltételezi, hogy mindenki ismeri. Ebben a függelékben megpróbáljuk definiálni a legtöbb ilyen kifejezést, illetve egy példát adni rájuk.

## Műveleti tulajdonságok

### Asszociativitás

!!! info Definíció
    Egy (kétváltozós) műveletre (legyen most $\ast$) akkor mondjuk, hogy asszociatív, ha "nem számít az elvégzésének sorrendje", azaz szabadon zárójelezhető:

    $$
    (u * v) * w = u * (v * w) = u * v * w
    $$

Ha egy művelet _nem_ asszociatív, akkor az azt jelenti, hogy $(u * v) * w \neq u * (v * w)$. Egy példa egy nem asszociatív műveletre az osztás:

$$
\frac{1}{6} = \frac{\frac{1}{2}}{3} = \underbrace{(1/2)/3 \neq 1/(2/3)}_{
    \footnotesize (u * v) * w \neq u * (v * w)
} = \frac{1}{\frac{2}{3}} = \frac{3}{2}
$$

### Kommutativitás

!!! info Definíció
    Egy (kétváltozós) műveletre (legyen most $\ast$) akkor mondjuk, hogy kommutatív, ha "nem számít az operandusok sorrendje", azaz:

    $$
    u * v = v * u
    $$

Ha egy művelet _nem_ kommutatív (antikommutatív), akkor az azt jelenti, hogy $u * v \neq v * u$. Egy példa egy nem kommutatív műveletre az kivonás:

$$
-1 = \underbrace{1 - 2 \neq 2 - 1}_{
    \footnotesize u * v \neq v * u
} = 1
$$

### Disztributivitás

Ez a fogalom már egy picit összetettebb, hiszen itt már két különböző műveletünk is van.

!!! info Definíció
    Két (kétváltozós) művelet (legyen most $+$ és $\ast$) esetén akkor mondjuk, hogy a $\ast$ művelet disztributív a $+$ műveletre nézve, ha "felbonthatjuk a zárójelet", azaz:

    $$
    c * (a + b) = (c * a) + (c * b)
    $$

Fontos, hogy az, hogy "az $\ast$ művelet disztributív a $+$ műveletre nézve" nem jelenti azt, hogy "az $+$ művelet disztributív az $\ast$ műveletre nézve". Ezt könnyen láthatjuk, hogy az összeadás és szorzás műveleteit nézzük:

$$
25 = 5 * 5 = \underbrace{5 * (2 + 3) = (5 * 2) + (5 * 3)}_{c * (a + b) = (c * a) + (c * b)} = 10 + 15 = 25
$$

a fenti azt demonstrálja, hogy az $\ast$ művelet disztributív a $+$ műveletre nézve, viszont ha megcserélnénk a műveleteket:

$$
11 = 5 + 6 = \underbrace{5 + (2 * 3) \neq (5 + 2) * (5 + 3)}_{c + (a * b) \neq (c + a) * (c + b)} = 7 * 8 = 56
$$

### Skálázhatóság

Elsősorban vektorok esetén beszélünk róla.


!!! info Definíció
    Egy műveletre (legyen most $\ast$) akkor mondjuk, hogy skálázható, ha $a, b \in \R^n$ és $s \in \R$ esetén:

    $$
    sa \ast b = s(a \ast b)
    $$

    tehát a skálázást "kiemelhetjük", és elvégezhetjük az $\ast$ művelet eredményére is.

Egy példa erre a jegyzetben is említett skaláris szorzás.

## Kombinatorika

### Binomiális tétel

!!! info Tétel
    Két, $a, b \in \R$ és $n \in \N$ esetén:

    $$
    (a + b)^n = \sum_{k=0}^{n} \binom{n}{k} \cdot a^{n-k} \cdot b^{k}
    $$

    ahol a $\binom{n}{k}$ binomiális együtthatót a következő képpen számoljuk:

    $$
    \binom{n}{k} = \frac{n^k}{k! (n-k)!}
    $$

    ahol $n!$ az n szám faktoriálisát jelenti.

Tehát például $n=2$-re:

$$
(x + y)(x + y) = x^2 + 2xy + y^2
$$

a binomiális tételt felhasználva is eljuthatunk ide:

$$
\begin{align*}
(x + y)^2 &= \sum_{k=0}^{2} \binom{2}{k} \cdot x^{2 - k} \cdot y^{k} \\
&= \binom{2}{0} \cdot x^{2} \cdot y^{0} + \binom{2}{1} \cdot x^{1} \cdot y^{1} + \binom{2}{2} \cdot x^{0} \cdot y^{2} \\
&= x^2 + 2xy + y^2
\end{align*}
$$

## Függvénytulajdonságok

### Folytonosság


!!! info Definíció (egyszerűsített...)
    Az $f$ függvény folytonos az $a$ pontban, ha

    $$
    \forall \varepsilon \in \R^{+} \; \exists \delta \in \R^{+} \; \forall x \in \text{Dom}(f) : \big( |x - a| < \delta \implies |f(x) - f(a)| < \varepsilon \big)
    $$

    Az $f$ függvény _folytonos_, ha az értelmezési tartományának összes pontjában folytonos.

A jegyzetben találkozhatunk $C^1$ és $C^2$ folytonossággal. Azokat az $f$ függvényeket, amelyek a fenti definíciónak eleget tesznek $C^0$ folytonosnak nevezzük. Egy függvényt $C^n$ folytonosnak nevezünk, ha az $n$. deriváltja is folytonos, azaz $f^{(n)}$ folytonos.

Például vegyük az $f: x \mapsto x^2 + 2$ függvényt. [Belátható](https://cdn.discordapp.com/emojis/1394642603701571605.webp?size=240), hogy $C^0$ folytonos. Nézzük a deriváltjait:

$$
\begin{align*}
f'(x) &= 2x \\
f''(x) &= 2 \\
f'''(x) &= 0 \\
&\vdots
\end{align*}
$$

láthatjuk, hogy itt $f$ összes deriváltja továbbra is folytonos, hogy tehát $f$-re igaz az, hogy $C^1$ vagy éppen $C^2$ folytonos.

Nézhetünk egy ellenpéldát is. Legyen $g(x) = \begin{cases} x^2 &\text{ha } x \gt 0 \\ 0 &\text{ha } x \le 0 \end{cases}$. Ez persze $C^0$ folytonos, de ha kétszer deriváljuk, akkor azt kapjuk, hogy:

$$
g''(x) = \begin{cases} 2 &\text{ha } x \gt 0 \\ 0 &\text{ha } x \le 0 \end{cases}
$$

ami már nem egy folytonos függvény, tehát $g$ nem $C^2$ folytonos.

## Absztrakt algebra

### Gyűrűk, testek, csoportok, stb...

(Az alábbi egy egyszerűsítés, akit mélyebben érdekel a téma annak ajánlok pár félévet az [ELTE Matematika BSc. képzésén](https://ttk.elte.hu/content/matematika-bsc.t.7680))

Az absztrakt algebrában elkezdünk elmozdulni a hétköznapi, megszokott rendszerekben való számolásoktól, és inkább magukkal a _rendszerekkel_ akarunk foglalkozni. Sok ezer évig nagyon sok dolgot magától értetődőnek vettek a matematikusok. Ha megkérdeznéd Euklidészt, vagy akár Newtont, akkor nekik valószínűleg gőzük sem lenne ahhoz, hogy mi az a "kommutativitás". Persze tudják, hogy $2 + 1 = 1 + 2$, és hogy $2 - 1 \neq 1 - 2$, hiszen ez "egyértelmű", de ha megkérdeznéd, hogy miért van ez így, akkor ők is csak megvonnák a vállukat.

A huszadik század eleje felé a matematikusokat elkezdte érdekelni, hogy "oké, de most komolyan, miért tudom megcserélni a tényezőkeg az összeadásnál, de a kivonásnál nem?", és még fontosabban "mi lenne, ha mégis meg tudnám?". Nagyon sok áttörés született ebben a korban, az absztrakt algebrán kívül a [halmazelmélet](https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory) pontos definíciója, a [matematikai logika](https://en.wikipedia.org/wiki/Mathematical_logic), [topológia](https://hu.wikipedia.org/wiki/Topol%C3%B3gia), azon belül is a [mértékelmélet](https://hu.wikipedia.org/wiki/M%C3%A9rt%C3%A9k_(matematika)), mind ekkor jöttek létre.

Nézzünk egy példát a gyűrű fogalmára:

!!! example Gyűrű
    Az egész számok $\Z$ halmaza az összeadás ($+$) és szorzás ($\ast$) műveletekkel egy gyűrűt alkot.

Igen, tényleg csak ennyi! Ha fogod az egész számok halmazát, és az általános iskolában tanult összeadás és szorzás műveleteket értelmezed rajta, az egy gyűrű! Nézzük meg pontosabban is:

!!! info Definíció
    Egy $R$ halmazt, két bináris művelettel ($+$, $\ast$) felszerelve egy _gyűrűnek_ nevezünk, ha betartja a _gyűrű axiómákat:_

    1. $R$ az $+$ művelettel együtt egy _Ábel-csoportot_ alkot, ami azt jelenti, hogy:
        - Az $+$ asszociatív $R$-ben.
        - Az $+$ kommutatív $R$-ben.
        - Létezik olyan $0 \in R$, hogy $a + 0 = a$ minden $a \in R$. (additív identitás)
        - Minden $a \in R$-re létezik egy $-a \in R$, melyekre igaz, hogy $a + (-a) = 0$. (additív inverz)
    2. $R$ a $\ast$ művelettel együtt egy _[Monoid](math_appendix.md#monoid)_, ami azt jelenti, hogy:
        - A $\ast$ művelet asszociatív $R$-ben.
        - Létezik olyan $1 \in R$, hogy $1 \ast a = a \ast 1 = a$ minden $a \in R$. (multiplikatív identitás)
    3. A $\ast$ művelet disztributív a $+$ műveletre nézve.

Ezeknek a nagy részére az lehet a reakciónk, hogy "hát persze, ez nem triviális?", és igazunk is lenne, hiszen több ezer évbe telt, mire a matematikusoknak eszébe jutott, hogy ezeket meg kéne fogalmazni, és össze kéne szedni egy listába.

Léteznek további kibővítések is, például a _kommutatív gyűrű_ egy olyan gyűrű, ahol a $\ast$ művelet is kommutatív. A fent említett egész számok halmaza is egy kommutatív gyűrűt alkot.

A jegyzetben amikor gyűrűkről van szó, akkor általában magától értetődő, vagy "megszokott" műveleti tulajdonságokról beszélünk, amiket éppen most soroltunk fel pontosan.

A test (angolul _field_) fogalma is nagyon hasonló mint a gyűrűnek, csak még több "triviális" tulajdonságot köt meg. Vegyük észre például, hogy a fenti gyűrű definíciónkkal nem tudnánk a racionális számok halmazát definiálni. Nem köti meg, hogy kell léteznie multiplikatív inverzeknek, tehát nem tudnánk például definiálni az $1/2$-edet. A testek pont ezért lényegében egy olyan gyűrűk, ahol a $0$-tól különböző elemeknek van multiplikatív inverze. Precízebben a _test axiómák_ határozzák meg, hogy mi egy test, melyeket itt nem sorolnék fel, de online sok helyen elérhetőek[.](https://en.wikipedia.org/wiki/Field_(mathematics)#Classic_definition)

### Monoid

Ez a kifejezés bár nem szerepel a jegyzetben, de nagyon sok relevanciája van az informatika világában is, szóval röviden megemlítem.

A [gyűrű axiómáknál](math_appendix.md#gyűrűk-testek-csoportok-stb) már meg volt említve a Monoid:

!!! info Definíció
    Egy $S$ halmaz egy $\ast$ bináris operátorral együtt egy _Monoidot_ alkot, ha az alábbi két axiómának eleget tesznek:

    1. A $\ast$ művelet asszociatív $S$-ben.
    2. Létezik olyan $e \in S$, melyre $a \ast s = s \ast a = a$ igaz minden $a$-ra $S$-ből.

Első ránézésre semmi köze sincs a programozáshoz, viszont a _funkcionális programozás_ világában egy eléggé fontos fogalom. Vegyük példának a "lista" fogalmát (láncolt lista). Ez vajon egy monoid? Legyen $L$ az összes lista halmaza. Ekkor például `[1,2,3]` $\in L$, vagy `["Almafa", "karika"]` $\in L$. Tudnánk találni egy olyan bináris műveletet, amellyel együtt $L$ teljesíti a monoid axiómákat?

Ennek a műveletnek asszociatívnak kell lennie, és két listából egy listát kell csinálnia. Mi lenne, ha az lenne a műveletünk, hogy két listát egymás után fűzünk. Jelölje ezt a műveletet `++`. Ekkor teljesül, hogy

```hs
[1, 2] ++ ([3, 4] ++ [5, 6]) == ([1, 2] ++ [3, 4]) ++ [5, 6]
```

Eddig jók vagyunk! Létezik vajon identitás elemünk? Igen, az üres lista! Láthatjuk, hogy

```hs
[1, 2, 3] ++ [] == [] ++ [1, 2, 3] == [1, 2, 3]
```

tehát a listák halmaza $L$ és a `++` művelet tényleg egy monoidot alkotnak.

Ez nekünk miért hasznos? Nézzünk egy másik példát. Az egész számok és az $+$ is egy monoidot alkotnak. Ez nekünk azért jó, mert kihasználva a monoid axiómákat egy nagyobb számítást tetszőleges sok kisebb számításra bonthatunk, amelyek részeredményeit a végén összefűzhetünk. Például vegyük ezt, hogy Java-ban van egy listányi számunk, és arra vagyunk kíváncsi, hogy mennyi az összes szám összege:

```java
public static void main(String[] args) {
    // A listánk (halmazunk)
    List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

    // Mennyi a `numbers` listában tárolt számok összege?
}
```

Ehhez egy kezdő programozó egy `for` ciklust használna:

```java
// ...
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

int sum = 0;
for (int i : numbers)
    sum = sum + i;

// ...
```

Az elegáns megoldáshoz használjuk ki, hogy egy monoiddal van dolgunk. Egyszerre mindig csak két számot szeretnénk összeadni, tehát valami olyasmit szeretnénk, ami végigmegy a listánkon, és _akkumulálja_ a részösszegeket, ahogy összeadogatjuk a szomszédos számokat. A Monoid elvén alapuló `reduce` függvény pontosan ezt csinálja nekünk:

```java
// ...
List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

// Párhuzamos feldolgozás
// A stream több részre oszlik, a részek külön-külön akkumulálódnak,
// majd az eredmények összeadódnak.
int sum = numbers.parallelStream().reduce(
    0, // additív identitás
    (a, b) -> a + b, // bináris művelet: két elemet kombinál
    (a, b) -> a + b  // összeadja a párhuzamosan számolt részösszegeket
);

//...
```

Mivel az összeadás asszociatív, a program feldarabolhatja az összeadást. Például az `(1 + 2 + 3) + (4 + 5 + 6)` ugyanazt az eredményt adja, mint az `1 + (2 + 3) + 4 + (5 + 6)`. Így tehát akár több szálon is össze tudjuk adni a listának egy-egy részlistáját, amiket a végén szintén összeadunk. Ennél az elemi példánál persze a `for` ciklus is megfelelő, viszont bonyolultabb számítások esetén az, hogy lényegében "ingyen" kaptuk meg a párhuzamosságot az nagyon kényelmes.

Ha elindulunk ezen az úton, akkor eljuthatunk a _monádok_ fogalmáig, amiket már minden programozó használt életében, és szerette őket, akkor is, ha pontosan nem tudta, hogy azt használta. Ha használtál már Javascriptben `Promise`-t, vagy Kotlinban `?.` operátort, vagy ha [hívtál már meg több függvényt egymás után](https://en.wikipedia.org/wiki/Function_composition_(computer_science)#Composing_function_calls) akkor már használtál monádokat.

A napjainkban egyre több modern nyelvben van sok funkcionális elem (Rust, Kotlin, Swift, Go) és régebbi nyelvek új verziói is sokat tartalmaznak (Java, C++). Az alapképzésben sajnos alig jut idő a funkcionális programozásra, viszont az OO-t a torkunkon is lenyomják. Ha mélyebben érdekel a téma, akkor nagyon tudom ajánlani a [Haskell nyelv](https://learnyouahaskell.github.io/introduction.html) megtanulását, illetve a [Deklaratív programozás](https://portal.vik.bme.hu/kepzes/targyak/VISZAD01/) kötvál és a [Funkcionális programozás C++-ban](https://portal.vik.bme.hu/kepzes/targyak/VITMAV47) szabvál elvégzését.
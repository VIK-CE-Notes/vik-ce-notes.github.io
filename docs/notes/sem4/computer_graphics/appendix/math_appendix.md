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


     

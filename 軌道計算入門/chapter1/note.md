<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
<script type="text/x-mathjax-config">
 MathJax.Hub.Config({
 tex2jax: {
 inlineMath: [['$', '$'] ],
 displayMath: [ ['$$','$$'], ["\\[","\\]"] ]
 }
 });
</script>

# 1章 円錐曲線の幾何学
円錐曲線：放物線、楕円、双曲線などの総称

## 放物線
定義
「一定点と一直線からの距離が等しい点の軌跡」  
### 直交座標
焦点$F(q, 0)$をとる。放物線上の任意の点$P(x, y)$から準線$x=-q$への推薦の足を$N$とすると
$$\overline{PF}=\overline{PN}$$
で定義することができ、これを整理すると
$$y^2=4qx$$
で放物線を表すことができる

また、$x=q$のときの$y$を*半直弦*とよび、放物線の半直弦は
$$l=2q$$
となる。

### 極座標
$$x=q-r\cos\theta, y=r\sin\theta$$
となることから、
$$r=\frac{2q}{1+\cos\theta}$$
または
$$r=\frac{l}{1+\cos\theta}$$
であらわされる。

## 楕円
定義
「二定点からの距離の和が一定である点の軌跡」
### 直交座標
焦点$F(c, 0), F'(-c, 0)$をとる。楕円上の任意の点$P(x, y)$とすると、
$$\overline{PF} + \overline{PF'} = 2a$$
$$(a > 0)$$
で定義することができ、これを整理すると
$$\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$$
$$(b^2 = a^2 - c^2)$$
となり、楕円をあらわすことができる。
このときの$a$を楕円の*半長軸*、$b$を*半短軸*という  

#### 離心率
$$e \equiv \frac{c}{a} = \frac{\sqrt{a^2-b^2}}{a}$$

#### 半直弦
$$l = \frac{a^2-c^2}{a} = a(1-e^2)$$

### 極座標
焦点$F$を極とすると、
$$x = c + r \cos{\theta}, y = r \sin{\theta}$$
となるので、これを整理すると
$$r = \frac{l}{1 + e \cos{\theta}}$$
となる。

## 双曲線
定義
「二定点からの距離の差が一定である点の軌跡」

### 直交座標
焦点$F(c, 0), F'(-c, 0)$をとる。双曲線上の任意の点$P(x, y)$とすると
$$\overline{PF'}-\overline{PF} = 2a$$
$$(a > 0)$$
で定義することができ、これを整理すると
$$\frac{x^2}{a^2} - \frac{y^2}{b^2} = 1$$
$$(a > b > 0)$$
$$(b^2 = c^2 - a^2)$$
となり、双曲線をあらわすことができる。
このときの$2a$を楕円の*交軸*、$2b$を*共役軸*という

#### 漸近線
双曲線をあらわす式は
$$y = \pm \frac{b}{a}\sqrt{x^2-a^2}$$
であらわすことができ、極限をとると
$$\lim_{|x| \to \infty} \pm \frac{b}{a}\sqrt{x^2-a^2} = \pm \frac{b}{a}x$$
となり、*漸近線*を求めることができる

#### 離心率
$$e \equiv \frac{c}{a} = \frac{\sqrt{a^2+b^2}}{a}$$

#### 半直弦
$$l = \frac{c^2-a^2}{a} = a(e^2-1)$$

### 極座標
焦点$F$を極とすると、
$$x = c - r \cos{\theta}, y = r \sin{\theta}$$
となるので、これを整理すると
$$r = \frac{l}{1 + e \cos{\theta}}$$
となる。

## 円錐曲線の極方程式
これまでの結果をまとめると円錐曲線の極方程式は
$$r = \frac{l}{1 + e \cos{\theta}}$$
であらわすことができ、
* $e = 0$の時円
* $0 < e < 1$の時楕円
* $e=1$の時放物線
* $1 > e$の時双曲線
となる。
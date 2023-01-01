# ZFun 2022 Writeup by AsakuraMizu

## 作者的心声&屁话

∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ ∑(ι´Д ン)ノ

莫名其妙就阿克了. 本来是零光找我验一下 FlagJudge 上的那几个题, 于是我也来凑个热闹. CTF 打的少, 应该也就是第二次认真打, 不久之前刚被 THUCTF2022 薄纱然后决定再也不打 CTF 了 () ~~毕竟题目确实水~~

~~既然零光说不用所有题都写那我就不写了吧~~

## 0-入门

### ZFun101

打开题目中的链接, 快速翻到最后, 拿到 flag. ~~内容? 谁看啊! (事后发现原来里边有下一个题的提示)~~

### PlantsVSZombies?

~~注意到这些文件里只有 main.pak 的修改日期是 2022 年肯定是出题人对它动了手脚所以只需要找工具把它拆开再看看出题人到底改了啥就可以了!~~

游玩冒险模式, 获得豌豆射手就可以在下方注意到 flag 的文本.

~~然而我本机上有一个已经一周目通关了的档结果我打了半天的二周目也没找着 flag~~

## 1-软件使用

### 面纱后面藏着什么呢

瞎点, 然后发现有一张白色的图片, 后边好像还有一些空白字符(?). 移开图片得到前半部分, 然后后边的那些只要选中之后把字体颜色改成黑色就可以看到啦!

~~然而如果你使用(较新版本的) Microsoft Word 并且 Word 主题或者系统主题为深色时你就会发现一些神奇的事情~~

## 2-菲林问答

### 1

~~不知道, 也没查, 但是零光沉迷粥, 那答案肯定是粥啦!~~

### 2

~~百度一下~~

### 3

~~零光根我说过一次但是我忘了~~

### 4

一开始我去 bilibili 上搜的, 虽然答案确实没错但是名字上总有一些差别半天没搞出来

### 5

![](https://http.cat/418)

### 6

相关资料不多, 直接查到了 [RFC 原文](https://www.rfc-editor.org/rfc/rfc9226.html). 然后大约就是这样的:

| 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| --- | --- | --- | --- | --- | --- | --- | --- |
| c   | j   | z   | w   | f   | s   | b   | v   |

~~好抽象啊~~

> The mnemonic basis is the shape of the lowercase character.

改写成正常的十六进制然后转一下就好了(x)

## 4-密码学

提示的都很明显了. 前四个分别搜一下凯撒密码 猪笔密码 仿射密码 栅栏密码, 手解一下或者写代码解或者直接用在线工具都可以.

第五个的话, ~~很明显是 md5~~ 但是 md5 并不可逆, 所以我们只能依赖于一些在线的数据库进行反查.

~~但是不知道为什么一开始我 Google 上搜 "md5 reverse lookup" 的时候找到的网站都搞不了这个题, 过了好几天我换搜 "md5 解密" 结果立马就出来了 好几把怪~~

## 5-社会工程学

我也不知道这俩题我怎么做出来的...

### 让我看看你爱不爱国

我一开始还以为小明是正在下飞机的盯着照片看了半天...后来才意识到他应该是拍照的...

然后我一开始还把 EXIF 这个名字给忘了, 查了半天才想起来...

所以查一下 EXIF 就好啦. 在线工具也有很多.

### 盒打击已就绪

EXIF 里边已经有了地点和时间, 然后照片上有飞机编号, 所以只需要查一下航班数据就好啦!

...要是这么简单就好了. 毕竟这方面接触的少, 啥工具啥资源都没有, 搜索了半天也没找到能追溯到 9.13 的免费查询服务. 过了几天好不容易找到了 ADS-B Exchange, 结果发现西安咸阳国际机场那儿没数据... 查这个飞机, 也没有经过那儿的数据...

实在不会做了, 开始瞎蒙. 把这个飞机在 9.13 那天飞的两个航班号拿去搜了一下, 结果发现一个就是福州到西安, 另一个是西安到福州...??????震撼我马一整年. 按格式填上去就对了.

## 6-编码与隐写

### qwq

~~这个题不应该放在密码学里边吗(x)~~ 搜一下kaomoji加密, 贴进去解密一下就得到 flag 啦.

### 我不高兴了

都说了是隐写嘛, `cat` 一下这个文件就不难发现在文件最后以文本形式藏了 flag.

(啊? 跟 hex 有什么关系?)

### 这是什么？失忆喷雾，喷一下。

一开始我看见 mp3 以为是在波形图里搞事情, 结果打都打不开是什么意思...一度弃疗. 过了几天想, 会不会在 metadata 里藏东西啊, 然后打开了属性-详情. 什么都没有啊...尺寸: 1920x1080??? 原来是 PNG 啊.

### 面纱后面藏着还是面纱

"用别的方法打开" 嘛...那也就是当压缩文件打开了. 正确做法是一个文件一个文件的查看, 搜索 `ZFun`, 应该很快就能找到. ~~但是当时不知道为啥我就是没找到于是我还是使用 cat 大法找的~~

## EX1-程序设计入门

1-5 都是很入门的程序设计题目, 也没什么好吐槽的. ~~除了我在验题的时候因为提交框手写 C++ 导致 CE 了好几次结果让零光以为我 WA 了然后怀疑数据错了~~

### LiLang

题目本意是 "用你熟悉的语言实现他", 这里也给出一个 C++ 实现的版本和一个 Python 实现的版本. ~~可是我对 TypeScript 最熟悉怎么办啊~~

```cpp
std::vector<std::string> data;
for (int n = 0; n < 10; n++)
{
    std::string tmp;
    std::cin >> tmp;
    data.push_back(tmp);
}

std::string longest;
int longest_length = 0;
for (const auto &item: data)
{
    int length = item.length();
    if (length > longest_length)
    {
        longest = item;
        longest_length = length;
    }
}

data.clear();
for (int n = 0; n < 10; n++)
{
    std::string tmp;
    std::cin >> tmp;
    data.push_back(tmp);
}

std::string shortest;
int shortest_length = 2147483647;
for (const auto &item: data)
{
    int length = item.length();
    if (length < shortest_length)
    {
        shortest = item;
        shortest_length = length;
    }
}

std::string out;
for (int i = 0; i < longest_length; i++)
{
    if (i % 2 == 0) out.push_back(shortest[(i / 2) % shortest_length]);
    out.push_back(longest[i]);
}
std::cout << out << std::endl;
```

```py
data = []
n = 0
while n < 10:
    tmp = input()
    data.append(tmp)
    n += 1

longest = ""
longest_length = 0
for item in data:
    length = len(item)
    if length > longest_length:
        longest = item
        longest_length = length

data = []
n = 0
while n < 10:
    tmp = input()
    data.append(tmp)
    n += 1

shortest = ""
shortest_length = 2147483647
for item in data:
    length = len(item)
    if length < shortest_length:
        shortest = item
        shortest_length = length

out = ""
i = 0
while i < longest_length:
    if i % 2 == 0:
        out += shortest[(i // 2) % shortest_length]
    out += longest[i]
    i += 1

print(out)
```

但是实际上你会发现这段代码的逻辑也不是很复杂, 进一步的, 你可以进行面向数据编程: 把输入的那一坨东西的前十行的最长的和后十行的最短的手动找出来, 再简单写一下最后的输出过程就行了. ~~实际情况上我都把读入部分写完了才想起来可以这么做~~

## EX2-HTTP 协议基础

推荐工具: [HTTPie](https://github.com/httpie/httpie)

## EX3-网络安全入门

### Web - WeakPassword

就嗯爆破... 用户名倒是没啥好说的, `admin`. 但是这弱密码稍微有点罕见(?)

工具的话我现场搜的(x), 用的[这个](https://github.com/lijiejie/htpwdScan), 感觉还不错. 弱密码字典也是现搜的.

### Misc - 让我康康！

做出这个题来实属意外...之前捣鼓 CTF 的时候从 BlackArch 源瞎安了好多东西, 但是也不会用, 本来想找 stegify 试试的, 结果发现本机上安了个叫 stegsolve 的东西...不知道干啥用的, 启动, 打开文件, 瞎几把点, 我超怎么出来个ミク吓我一跳...

### Reverse - Reverse.NET

~~都给源码了算什么逆向~~ 把变量名简单整理一下, 大约就差不多了(?)

```cs
using System;
using System.Text;
static class Programs
{
    static int[] xjb(int len)
    {
        var tmp = new int[len];
        var last = 0;
        for (int i = 0; i < len; i++)
        {
            last = ((last * 2 + 35) / 3 + i) % 256;
            tmp[i] = last ^ i;
        }
        return tmp;
    }

    static void xor(int[] lhs, int[] rhs)
    {
        for (int i = 0; i < lhs.Length; i++)
        {
            lhs[i] ^= rhs[i];
        }
    }

    static int[] convert(byte[] input)
    {
        var output = new int[input.Length];
        for (int i = 0; i < input.Length; i++)
        {
            output[i] = (int)input[i];
        }
        return output;
    }

    static bool cmp(int[] lhs, int[] rhs)
    {
        for (int i = 0; i < lhs.Length; i++)
        {
            if (lhs[i] != rhs[i])
                return false;
        }
        return true;
    }
    static void Main(string[] args)
    {
        Console.WriteLine("Please give me your flag!");
        var inputraw = Console.ReadLine() ?? throw new Exception("No flag given!");
        var input = Encoding.UTF8.GetBytes(inputraw);
        var xjbr = xjb(input.Length);
        var inputi = convert(input);
        xor(inputi, xjbr);
        var ans = new[] { 81, 83, 108, 77, 90, 94, 78, 65, 94, 77, 64, 82, 108, 46, 20, 55, 41, 48, 36, 53, 34, 34, 20, 0, 9, 22, 7, 3, 22, 1, 52, 5, 34, 0, 192, 212, 203, 206, 217, 199, 228, 214, 192, 232, 197, 234, 249, 254, 196, 250, 226, 244, 250, 242 };

        if (cmp(ans, inputi))
        {
            Console.WriteLine("TTTTTTTTTTQQQQQQQQQQLLLLLLLLLLLL");
        }
        else
        {
            Console.WriteLine("the flag is moectf{Never_gonna_give_you_up_and_never_gonna_let_you_down}");
        }
    }
}
```

然后写代码求解一下就好啦. (以 C++ 为例)

```cpp
#include <bits/stdc++.h>

constexpr int len = 54;
int ans[54] = { 81, 83, 108, 77, 90, 94, 78, 65, 94, 77, 64, 82, 108, 46, 20, 55, 41, 48, 36, 53, 34, 34, 20, 0, 9, 22, 7, 3, 22, 1, 52, 5, 34, 0, 192, 212, 203, 206, 217, 199, 228, 214, 192, 232, 197, 234, 249, 254, 196, 250, 226, 244, 250, 242 };
int tmp[54];

int main()
{
    int last = 0;
    for (int i = 0; i < len; i++)
    {
        last = ((last * 2 + 35) / 3 + i) % 256;
        tmp[i] = last ^ i;
        putchar(ans[i] ^ tmp[i]);
    }
}

```

### Crypto - Signin

~~完了完了 直到我写 write-up 的时候才意识到这题就是个裸的 RSA 呜呜呜 wsfw~~

~~那没啥好说的了 除了我捣鼓了半天才想起来还有 factordb 这种好东西 呜呜呜~~

求解代码：
```python
from Crypto.Util.number import getPrime, inverse, GCD, bytes_to_long, long_to_bytes

p = 96863258250433363013394004205541821945318720448876934681348184177799281458817
q = 107309223444359869012626092578645060845564671687232835115926679931416345607187
n = p * q
# n = 10394321023144488346542992032155806806414680909684392975928580892496643435445514955693895484420645749446606678782710915422663601938326865106010474999717779
e = 65537
c = 6006340278470698080420389403435089961276841055382726375740665082270943510759808217204232813782695963301313497214683115741729078623773424136787230353252712

phi = (p - 1) * (q - 1)
ee = inverse(e, phi)

m = pow(c, ee, n)
flag = long_to_bytes(m)

print(flag)
```

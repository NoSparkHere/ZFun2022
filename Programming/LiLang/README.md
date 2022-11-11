# LiLang

## 题目描述

~~听说某个高校的CTF比赛出了个HeLang(何语言)？不行不行，我们也得整一个！~~

**鲤语言：年轻人的第一个编程语言**

你说的对，但是《鲤语言》是由鲤唐可可自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「ZFun2022」的幻想世界，在这里，被选中的人将被授予「CTFer」的称号，导引Cyber之力。你将扮演一位名为「大黑阔」的神秘角色，在自由的探索中邂逅奇奇怪怪、但是能用的方法，并运用他们一起击败出题人，找回失散的flag——同时，逐步发掘「鲤语言」的真相。

现在你要根据附件中的lilang代码，用你熟悉的语言实现他。然后从服务器获得challenge，并用你的程序结出这个challange，你将得到flag。

## 语法特性

1. `let <variable> [as <type>] <value>` 将变量variable的值设为value，如果变量不存在，则先创建变量
2. `append <value> into <list>` 将变量variable添加到列表list中，并返回index
3. `print <value>` 输出value
4. `input <variable>` 输入值，并赋给变量variable
5. `if <condition> <statement>` 如果condition为真，执行statement
6. `while <condition> <statement>` 如果condition为真，执行statement
7. `foreach <variable> in <list> <statement>` 遍历列表list，将列表中的每个元素赋给变量variable，执行statement
8. `function(parameter)` 调用函数function，参数为parameter
9. `list[index]` 返回列表list中index位置的元素

## 一些用到的api

1. default(type) 返回type类型的默认值
2. list() list类型的构造函数，返回一个空list
3. len(obj) 返回obj的长度

## 改题感想

> 如果有下次，我一定要用一个能用 token、网页终端和动态 flag 的 CTF server。
>
> 我改了多少道 ltkk 的题了？线下一定要锤爆他1111
>
> ——ZeroAurora


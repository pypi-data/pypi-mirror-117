Introduce
=========

| Hi! Thanks for comming my site.
| When you want to delete duplicate sentence from your sentence, Please
  use duplidele.

How to install
==============

pip install duplidele

How to coding
=============

1)Delete one character at a time

| import duplidele as dd
| dd.exduplidelechar(“test sentence test sentence duplicate delete”, 5)

2)Delete word by word

| import duplidele as dd
| dd.exduplidele(“おはよう。猫さん。こんにちは。おはよう。猫さん。こんばんは。”,
  5)

What is exported?
=================

1) sys.argv[1] str: test sentence test sentence duplicate delete
   sys.argv[2] int: 5

export ⇒ test sentence test sentence duplicate delete

2) sys.argv[1] str:
   おはよう。猫さん。こんにちは。おはよう。猫さん。こんばんは。
   sys.argv[2] int: 2

export ⇒ おはよう。猫さん。こんにちは。こんばんは。

License
=======

MIT

# toefl-words
学习托福单词的笔记和搜索程序，目前主要内容是曲根老师的课程和红宝书。

`word_lib.py` 存储了文件 Parse 的几个基本方法。

其中 `search.py ` 是对笔记的搜索程序，会自动 Parser 笔记表格里的单词和解释数据，搜索时通过比较前缀进行搜索，会返回对应的单词和同前缀的单词。

`tran_word_to_xml.py` 能把 markdown 转换成 `有道词典 ` 支持的 xml 格式文件。

`spell.py` 能够对指定的单词笔记进行听写。

`watch_and_update.py` 监听本文件夹，发现新的文件修改之后会自动 commit ，事件间隔是 20 秒。

### Command

* up-

调用 shell 可以在 Command 中 push 到 github 的仓库

* cl-

清理屏幕的指令

* fk-

退出程序

* re-

重新 Parser 所有的笔记




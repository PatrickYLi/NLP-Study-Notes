# Ex:处理布朗语料库的新闻和言情文体，找出一周中最有新闻价值并且是最浪漫的日子。
# 定义一个变量days，包含星期的列表，如['Monday', ...]。
# 然后使用cfd.tabulate(samples=days)为这些词的计数制表。
# 接下来用plot替代tabulate尝试同样的事情。
# 你可以在额外的参数samples=['Monday', ...]的帮助下控制星期输出的顺序。

from nltk.corpus import brown
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in ['news', 'romance']
    for word in brown.words(categories = genre))

cfd.tabulate(samples = days)

cfd.plot(samples = days)
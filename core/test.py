from core.manager import Manager
man = Manager()
# man.append("https://www.yodobashi.com/product/100000001005854974/")
man.append("https://www.example.com/ダミー商品A/")
man.append("https://www.example.com/ダミー商品B/")
man.df

man.start()

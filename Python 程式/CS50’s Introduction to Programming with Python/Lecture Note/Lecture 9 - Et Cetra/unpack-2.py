def f(*args, **kwargs):                                    #使用 * 進行 list 解包，** 進行 dict 解包
    print("Positional:", kwargs)


f(100, 50, 25, 5)

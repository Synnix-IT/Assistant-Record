from typing import Union

fruits : dict [Union[str, int]]= {                                                  # 這個 Dictionary 的資料型態應該是 dict[str, str]，而不是 dict[Union[str, int]]
    "apple" : "130",    "avocado" : "50",    "banana" : "100",                      # dict[Union[str, int]] 代表這個字典只有 Key，Key 可以是 str 或 int。然後這個字典沒有 Value
    "cantaloupe" : "50",    "grapefruit" : "60",    "grapes" : "90",                # dict 的註解會是 dict[<Key>, <Value>]，例如 dict[str, int]，代表 Key 是 str，Value 是 int
    "honeydew melon" : "50",    "kiwifruit" : "90",    "lemon" : "15",              # Union 的用法是，舉例，當你的 Key 是 str，Value 可能是 str 或 int 時，會註解成 dict[str, Union[str, int]]
    "lime" : "20",    "nectarine" : "60",    "orange" : "80",
    "peach" : "60",    "pear" : "100",    "pineapple" : "50",
    "plums" : "70",    "strawberries" : "50",    "sweet cherries" : "100",
    "tangerine" : "50",   "watermelon" : "80"
}

fuirt : str = input("Item: ").lower()                                               # fuirt 可能是拼錯字 ? 應該是 fruit ?

if fuirt in fruits:

    print(f"Calories: {fruits[fuirt]}")


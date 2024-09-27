from unittests import square
import pytest

#def main() -> None:
#    test_square()


def test_square() -> None:                                          #將執行程式拆開為不同的函式，觀察使用 pytest 檢查後的輸出

    assert square(2) == 4
    assert square(3) == 9


def test_square2() -> None:
    assert square(4) == 16
    assert square(5) == 25


def test_square3() -> None:
    assert square(6) == 36


#def test_str() -> None:
#    with pytest.raises(TypeError):
#        square("cat")
#    try:
#        assert square(2) == 4                                       #使用 assert 判斷輸入的數字是否等於預想結果
#    except AssertionError:                                          #若輸入的數字不等於預想結果則印出錯誤訊息
#        print("square(2) was not 4")

#    try:    
#        assert square(3) == 9
#    except AssertionError:  
#        print("square(3) was not 9")
    


#    if square(2) != 4:                                             #使用 if 判斷輸入的數字是否等於預想結果
#        print("square(2) was not 4")

#    if square(3) != 9:
#        print("square(3) was not 9")

#    if square(4) != 16:
#        print("square(4) was not 16")


#if __name__ == "__main__":
#    main()
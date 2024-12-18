---
comments: true
title: 2024.11.06 學習紀錄
date: 2024-11-06
updated: 2024-11-06
tags: [Python, 學習紀錄]
categories: [Python, IT]
keywords: Python, 學習紀錄
description: 2024年11月06日的學習紀錄，涵蓋 Python PyQt6 的學習內容。
copyright_author: 王仁傑
copyright_author_href: https://github.com/Wang-ren-jie
cover: /images/Python_PyQt6_2.jpg
---

# 2024.11.06 學習紀錄

## 今日進度概述

今天的學習主要圍繞 **Python PyQt6** 的相關知識，學習重點圍繞在 `PyQt6 GUI` 開發，使用 `PyQt6` 和 `Qt Creator` 來設計 **多層佈局** 和 **互動功能**。我特別著重於 **介面排版**、**訊號槽機制** 的應用，並熟悉了如何使用 `Python` 控制 `GUI` 元件的 **屬性** 和 **行為**。

---

## 學習重點

### Python PyQt6

- **表單佈局和元件的使用**
    - 利用 `QHBoxLayout` 和 `QVBoxLayout` 將元件分別水平和垂直排列，並組合使用以達到更靈活的佈局。

    - 使用了 `QFormLayout` 來建構表單輸入區，這種設計方式使得 **欄位名稱** 和 **輸入框排列** 清晰，方便用戶操作。
    - 在窗口上添加了 `QLabel`、`QLineEdit` 和 `QPushButton`，如 **「姓名」標籤**和 **「確認」按鈕**。透過 `PyQt` 的 `QtGui` 模組進行細部調整，包括 **設定字體**、**對齊方式** 等，以提升用戶體驗。

- **信號槽機制的應用**
    - 實作了按鈕的點擊事件，如 **「關閉視窗」按鈕**，並將它們連接到相應的 **槽函數**，使應用程式在使用者點擊按鈕時觸發相應的行為。
    - 實作了 **自訂槽函數** 來接收 **按鈕點擊訊號**，如 **「開始」按鈕** 被點擊後，會 **顯示** 當前用戶設定的 **輸入值範圍**。在這部分，我採用了 `@pyqtSlot()` 修飾器，進一步確保信號槽系統的 **穩定性** 和 **可讀性**。

- **菜單欄和工具欄的建立**
    - 使用 `QMenuBar` 和 `QToolBar` 在主窗口上方添加了 **菜單** 和 **工具欄**，包括 **「新建」**、**「開啟」**、**「關閉」** 等常見功能按鈕。這些按鈕的設計模仿了一般軟體的 **標準菜單佈局**，符合用戶操作習慣。
    - 利用 `QFileDialog` 實作了 **「開啟檔案」** 的功能，當使用者點擊該選項時會 **彈出檔案選擇** 對話框，並顯示在 **狀態欄** 上。這種動態的訊息顯示方式提升了應用程式的互動性。

- **靜態圖標和狀態提示**
    - 在 **主界面** 中加入了 **圖像** 和 **圖標顯示**，如通過 `QLabel` **加載圖片** 並調整其 **顯示大小**，使得界面視覺效果更豐富。
    - 設置了 **狀態欄訊息** 提示功能，在滑鼠 **滑過按鈕** 後，**狀態欄** 會顯示一則短暫的 **提醒**，如 **「指標滑過該標籤觸發事件」** 等，並設定為5秒自動消失，這對於即時提醒用戶操作的反饋非常有幫助。

- **使用 Qt Creator 設計 UI 文件**
    - 透過 `Qt Creator` 設計 `.ui` 文件，並利用 `PyQt6` **自動生成** 的 **代碼** 快速構建 `UI`，減少手動編寫佈局代碼的負擔，使 **開發流程** 更有 **效率**。
    - 在學習過程中，我理解了如何將 `.ui` 文件轉換為 `Python` 文件，並根據需求進行 **二次編輯** 和 **功能擴充**，如 **增加按鈕事件** 和 **自定義元件屬性**。
</br>


## 下一步計畫

明日的學習將繼續深入以下領域：

- **Python PyQt6**：持續練習 `PyQt6`，學習更完整的 **基本視窗控制項**，直接從程式上了解 `GUI` 介面的配置，以及 **標籤** 的活用，搭配 **按鈕** 及 **文字輸入框** 做更深入的練習及應用。

### 學習目標

- 在兩個月內完成 **Computer Foundation** 基礎的學習，並嘗試一些進階主題。
- 在一個月內完成 **Python PyQt6** 的基本學習，並嘗試 `GUI` 介面的實際應用。

---

### 結語

今天的練習使我對 `PyQt6` 的 `GUI` 開發有了更深入的理解。透過實作不同的 **佈局結構**、**操作信號與槽**、**添加狀態提示** 和 **菜單功能**，我體會到 `GUI` 設計在用戶體驗中的重要性。同時，`Qt Creator` 的使用讓我能更 **快速** 地搭建 `UI`，從而將更多精力集中在 **核心功能** 上。


_持續學習，不斷進步，為達成目標奠定堅實基礎！_

---

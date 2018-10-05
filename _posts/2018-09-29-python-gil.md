---
layout:     post
title:      Python GIL là gì
date:       2018-09-29 00:00
summary:    Python Global Interpreter Lock là gì?
permalink:	python-gil
tags: python, index
image: images/gil.jpg
---
Python Interpreter Lock (hay GIL) là một thuật ngữ trong lập trình có liên quan đến xử lý Luồng (Thread), là một Khóa (Lock) Tổng (Global) quản lý Thread sao cho tại một thời điểm nhất định, chỉ có 1 Luồng giữ Khóa đóng vai trò truy xuất, chỉnh sửa bộ nhớ.

Điều đó có nghĩa là, các lập trình viên làm việc trên 1 Thread duy nhất sẽ không cảm nhận được sự ảnh hưởng của Khóa Tổng này, tuy nhiên trong lập trình viên có sử dụng các Luồng song song (multi-thread) hay những tác vụ CPU-bound thì GIL **có thể** là nút thắt cổ chai dẫn đến chương trình chạy chậm.

## Tại sao Python lại tồn tại GIL?
Python là ngôn ngữ lập trình hướng đối tượng, trên hết mọi thứ trong Python đều là Object! (Class, function, metaclass, vv..) Mỗi Object đều được gán (tag) cho một địa chỉ trên bộ nhớ và để tiết kiệm bộ nhớ thì thay vì mỗi lần khai báo biến, Python sẽ không lập tức tạo một bộ nhớ mới mà trước hết là xem xét biến đó có được gán với một biến nào đã tồn tại trước chưa, ví dụ:
```python
>>> a = "Hello World"
>>> print(hex(id(a))) # 0x7fed2a63b870
>>> b = a
>>> print(hex(id(b))) # 0x7fed2a63b870

>>> a = "Oops"
>>> print(a) # Oops
>>> print(b) # Hello World
```
biến `b` như trong ví dụ trên được trỏ tới ví trí `0x7fed2a63b870` trong bộ nhớ, và khi `a` thay đổi, `b` do được gán vị trí cố định trên bộ nhớ mà không bị thay đổi.

Tiếp đến, Python sử dụng "reference counting" để quản lý bộ nhớ, tránh việc memory leak. Vậy reference counting là gì? Mỗi khi một object được tạo, Python sẽ gán 1 giá trị để đếm xem số lượng object được gán với địa chỉ đó là bao nhiêu. Và khi số biến được `reference` tới bộ nhớ là 0, vùng bộ nhớ đó sẽ được xóa đi để không gian cho những biến khác giúp tiết kiệm bộ nhớ hơn. Hãy xem 1 ví dụ dưới đây để thấy reference counting hoạt động ra sao:

```python
>>> import sys
>>> a = []
>>> b = []
>>> sys.getrefcount(a)
3
```
list trống [] được reference 3 lần (cho biến a, b và khi truy xuất sys.getrefcount).


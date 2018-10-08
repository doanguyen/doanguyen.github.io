---
layout:     post
title:      Python GIL là gì
date:       2018-09-29 00:00
summary:    Python Global Interpreter Lock là gì?
permalink:	python-gil
tags: python, index
image: images/gil.jpg
---
Python Global Interpreter Lock (hay GIL) là một thuật ngữ trong lập trình có liên quan đến xử lý Luồng (Thread), là một Khóa (Lock) Tổng (Global) quản lý Thread sao cho tại một thời điểm nhất định, chỉ có 1 Luồng giữ Khóa đóng vai trò truy xuất, chỉnh sửa bộ nhớ. Thử tưởng tượng hình bên dưới mô tả quá trình phân phối tài nguyên CPU trong Python, trong đó mỗi cá nhân xếp hàng là 1 Thread, người thu ngân đóng vai trò là Lock (và rõ ràng, chúng ta có 2 Process chạy song song :D). Tại mỗi thời điểm mỗi Lock chỉ làm việc với 1 Thread, khi đó chúng ta coi Thread đó đang giữ Khóa, các Thread còn lại phải ở trong trạng thái chờ Queue.

![](images/queue.png)

Điều đó có nghĩa là, các lập trình viên làm việc trên 1 Thread duy nhất sẽ không cảm nhận được sự ảnh hưởng của Khóa Tổng này, tuy nhiên trong lập trình viên có sử dụng các Luồng song song (multi-thread) hay những tác vụ CPU-bound (các công việc nặng như xử lý Video, ảnh, ...) hoặc IO-bound (các công việc liên quan đến IO: ghi dữ liệu ra file, xử lý 1 socket,...) thì GIL **có thể** là nút thắt cổ chai dẫn đến chương trình chạy chậm. 

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
list trống [] được reference 3 lần (cho biến a, b và khi truy xuất tại sys.getrefcount).

Quay lại với GIL:

Có thể nói việc GIL là thiết yếu trong Python (hay cả Ruby) xuất phát từ việc sử dụng reference counting.  Tại sao vậy? Thử tưởng tượng trong trường hợp 2 Thread cùng tham chiếu tới 1 *variable counting* và cùng tăng hoặc giảm đồng thời giá trị đó, nếu may mắn thì chúng ta sẽ xuất hiện memory leak, tồi tệ hơn khi 1 Thread đã xóa biến `a` khỏi bộ nhớ nhưng vẫn còn 1 Thread khác vẫn sử dụng biến `a`, điều đó sẽ dẫn tới chương trình crash mà lúc đó sẽ rất khó để tìm ra lỗi. Do đó để giải quyết vấn đề trên, 1 Global Lock được tạo ra cho tất cả các Thread.

Ngoài cách sử dụng GIL, các lập trình viên còn có thể tạo ra 1 layer trong quá trình compiler - JIT (Just in time compiler) để giải quyết vấn đề trên. Jpython, IronPython là 2 ví dụ điển hình của interpreter Python mà không sử dụng GIL. Tuy nhiên nhược điểm của JIT là thời gian khởi động lại cực chậm nên không được nhiều lập trình viên Python  sử dụng.

Tụm chung lại:

* Jython và IronPython không tồn tại GIL và hoàn toàn có thể khai thác được các ưu thế của multiprocessor.
* PyPy có tồn tại GIL, và cộng đồng Pypy đang cố gắng loại bỏ GIL bằng cách thực hiện [Software Transactional Memory](http://doc.pypy.org/en/latest/stm.html#id14)
* Cython cũng tồn tại GIL, tuy nhiên lập trình viên có thể tạm thời tắt bằng `with` statement.

## Tại sao Python chọn GIL làm giải pháp?


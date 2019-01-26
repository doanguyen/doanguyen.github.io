---
layout:     post
title:      Python GIL là gì
date:       2018-09-29 00:00
summary:    Python Global Interpreter Lock là gì?
permalink:	python-gil
tags: python, index
---

Python Global Interpreter Lock (hay GIL) là một thuật ngữ trong lập trình có liên quan đến xử lý Luồng (Thread), GIL là một Khóa (Lock) Tổng (Global) quản lý Luồng sao cho tại một thời điểm nhất định, chỉ có 1 Luồng giữ Khóa đóng vai trò truy xuất, chỉnh sửa bộ nhớ. Thử tưởng tượng hình bên dưới mô tả quá trình phân phối tài nguyên CPU trong Python, trong đó mỗi cá nhân xếp hàng là 1 Luồng, người thu ngân đóng vai trò là Khóa (và rõ ràng, chúng ta đang có 2 Process chạy song song). Tại mỗi thời điểm mỗi Khóa chỉ làm việc với 1 Luồng, khi đó chúng ta coi Luồng đó đang giữ Khóa, các Luồng còn lại phải ở trong trạng thái Chờ-Queue.

![](images/queue.png)
*Source: Freepik*

Điều đó có nghĩa là, các lập trình viên lập trình đơn Luồng sẽ không cảm nhận được sự ảnh hưởng của Khóa Tổng (từ bây giờ Khóa Tổng sẽ được nói gọn là Khóa) này. Tuy nhiên trong lập trình có sử dụng các đa Luồng (multi-thread) tồn tại CPU-bound
<label for="sn-extensive-use-of-sidenotes" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-extensive-use-of-sidenotes" class="margin-toggle"/>
<span class="sidenote"><b>CPU-bound</b>: các công việc nặng như xử lý Video, ảnh,.. <br />
<b>IO-bound</b>: các công việc liên quan đến IO: ghi dữ liệu ra file, xử lý 1 socket,...
</span>
thì GIL chỉ cho phép 1 thread hoạt động, do đó không tận dụng được hết ưu thế của máy tính đa nhân, đa luồng hiện tại.

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

Có thể nói việc GIL là thiết yếu trong Python (hay cả Ruby, PHP) xuất phát từ việc sử dụng reference counting.  Tại sao vậy? Thử tưởng tượng trong trường hợp 2 Luồng cùng tham chiếu tới 1 *variable counting* và cùng tăng hoặc giảm đồng thời giá trị đó, nếu may mắn thì chúng ta sẽ xuất hiện memory leak, tồi tệ hơn khi 1 Luồng đã xóa biến `a` khỏi bộ nhớ nhưng vẫn còn 1 Luồng khác vẫn tham chiếu tới biến `a`, điều đó sẽ dẫn tới chương trình crash mà lúc đó sẽ rất khó để tìm ra lỗi. Do đó để giải quyết vấn đề trên, 1 Khóa được tạo ra cho tất cả các Luồng trong 1 Process.

Ngoài cách sử dụng GIL, các lập trình viên còn có thể tạo ra 1 layer trong quá trình compiler - JIT (Just in time compiler) để giải quyết vấn đề trên. Jpython, IronPython là 2 ví dụ điển hình của interpreter Python mà không sử dụng GIL. Tuy nhiên nhược điểm của JIT là thời gian khởi động lại siêu chậm nên không được nhiều lập trình viên Python  sử dụng.

Tụm chung lại:

* Jython và IronPython không tồn tại GIL và hoàn toàn có thể khai thác được các ưu thế của multiprocessor.
* PyPy có tồn tại GIL, và cộng đồng Pypy đang cố gắng loại bỏ GIL bằng cách thực hiện [Software Transactional Memory](http://doc.pypy.org/en/latest/stm.html#id14)
* Cython cũng tồn tại GIL, tuy nhiên lập trình viên có thể tạm thời tắt bằng `with` statement.

## Tại sao Python chọn GIL làm giải pháp?

Vậy tại sao Guido
<label for="sn-guido-van-rossum" class="margin-toggle sidenote-number"></label><input type="checkbox" id="sn-guido-van-rossum" class="margin-toggle"/>
<span class="sidenote"><b>Guido van Rossum</b>, người sáng lập ra ngôn ngữ lập trình Python.
</span>
lại chọn GIL từ những ngày đầu viết CPython? Liệu đó có phải là lựa chọn tồi ngay từ khi Python được hình thành?

Không thể phủ nhận rằng việc chọn GIL có lẽ lại là một trong những quyết định khiến Python trở nên phổ biến như hiện nay. Những ngày đầu Python hình thành, khái niệm về Thread/Multithread trong các hệ điều hành còn chưa được phổ biến [need source?], và Python được thiết kế với mục đích dễ đọc, dễ viết cho người mới làm quen nên tốc độ xử lý không phải là ưu tiên hàng đầu. Và khi Python càng được mở rộng, vô số những thư viện khác nhau được hình thành tư rất nhiều nguồn lập trình viên, vì thế thread-safe memory là điều kiện tiên quyết để có cộng đồng lập trình viên lành mạnh, cho ra những phần mềm an toàn và hạn chế tối thiểu lỗi trong quá trình thực thi. Và cũng từ GIL, tốc độ thực thi của phần mềm single-threaded được tăng cường tốc độ đáng kể, những thư viện C với non thread-safe có thể dễ dàng `port` qua thư viện Python sử dụng Python extension, điều đó càng làm cho cộng đồng Python trở nên phát triển như hiện nay. Do đó, có thể nói rằng GIL là giải pháp an toàn để giải quyết các vấn đề phức tạp mà cộng đồng lập trình viên Python gặp phải hàng ngày.

Điều đó đi cùng với 1 hạn chế: lập trình multithread sẽ ít nhận được lợi ích từ CPython!

## Liệu có thể lập trình Multithread trên Python hay không?

Hoàn toàn có thể, thậm chí Python còn có 1 thư viện chuẩn dành cho multithreading. Hãy xem ví dụ về chương trình đếm ngược sau đây:

```python
# single_threaded.py
import time
from threading import Thread

COUNT = 50000000  # 50.000.000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start)
```

Đoạn code trên là một trong những ví dụ liên quan đến CPU-bound, tức là khi chương trình khởi chạy nó sẽ đẩy CPU tới giới hạn làm việc của CPU.

```powershell
$ python single_threaded.py
Time taken in seconds - 1.7025535106658936
```

Khi sử dụng thư viện multithread, đoạn code được thiết kế lại để chia việc `countdown` ra làm 2 task thực hiện việc đếm ngược:

```python
# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)

```

và kết quả:

```bash
$ python multi_threaded.py
Time taken in seconds - 1.6745080947875977
```

như bạn có thể thấy, ở cả single thread và multi thread, thời gian thực hiện gần như tương đồng. Điều đó có được là do multi-threaded đã bị GIL hạn chế và bạn không thể thực hiện 2 tác vụ cùng 1 thời điểm được.

GIL **không** có nhiều ảnh hưởng đến hiệu suất chương trình có I/O-bound, đơn giản là *thời gian* đợi I/O thông thường lớn hơn so với nhận lại khóa từ GIL. (Nhận định này rất dễ gây nhầm lẫn với sync/async operation).

Tuy nhiên chương trình có thread chạy CPU-bound, ví dụ 1 process trong đó có 1 Luồng xử lý hình ảnh, chương trình sẽ ngay lập tức trở thành đơn luồng, các Luồng còn lại trong process đó sẽ phải đợi khi Luồng xử lý hình ảnh hoàn thành mới nhận được lock từ GIL dẫn tới việc thời gian xử lý tăng lên.

Do đó có rất rất nhiều thảo luận được đưa ra nhằm dỡ bỏ GIL từ Python core.

## Vậy tại sao CPython chưa loại bỏ GIL?

Có rất nhiều lập trình viên phàn nàn về GIL tồn tại trong một thời gian lâu như vậy ở một ngôn ngữ lập trình phổ biến nhất trên thế giới?

Câu trả lời là: Loại bỏ GIL không hề đơn giản, nhóm Python Core đã tìm rất nhiều cách để loại bỏ GIL mà không gây "backward incompatibility", từ những năm 2007 Guido van Rossum đã có [cuộc trao đổi](https://www.artima.com/weblogs/viewpost.jsp?thread=214235) về vấn đề này, nhiều phương án đã được đưa ra những chưa có giải pháp thực sự để loại bỏ.

Tuy nhiên Python 3 đã có một số cải tiến đáng kể để thay đổi nguyên tắc hoạt động của global lock. Từ Python 3, Python **buộc** các thread phải "nhả" khóa trong số thời gian nhất định:

```python
import sys
print(sys.getcheckinterval()) # 100
```

Vậy là sau `100` [instructions](https://en.wikipedia.org/wiki/Instruction_set_architecture) thread nào đang giữ khóa thì sẽ bắt buộc phải "nhả" và nếu không có thread nào đang xếp hàng đợi thì thread đó sẽ được giữ khóa trong 100 instructions tiếp theo. Một số cải tiến nữa được thực hiện từ Python 3 trở đi, ví dụ ở [đây](http://www.dabeaz.com/blog/2010/01/python-gil-visualized.html) và [đây](https://mail.python.org/pipermail/python-dev/2009-October/093321.html).

## Vậy giải pháp là gì

Một số giải pháp có thể sử dụng như sau:

**Muti-processing:** Python GIL chỉ giới hạn trong process mà nó thực thi, với các process khác nhau, vị trí bộ nhớ hoạt động cũng khác nhau nên Python không còn phải lo lắng về reference counting nữa. 

Ví dụ về [multiprocessing](https://docs.python.org/3.4/library/multiprocessing.html?highlight=process).

**Sử dụng các Python Interpreter thay thế:** Như Pypy, IronPython, Jython.

Sử dụng Cython: Rất nhiều người đang rất để tâm tới Cython vì tính tiện lợi và việc di chuyển giữa C/C++, Python API dễ dàng hơn nhiều, việc gỡ bỏ GIL có thể thực hiện trực tiếp bởi [with](https://cython.readthedocs.io/en/latest/src/userguide/external_C_code.html#nogil) statement.

Tham khảo:

[0] Google/Wikipedia/Youtube.

[1][https://mail.python.org/pipermail/python-dev/2009-October/093321.html](https://mail.python.org/pipermail/python-dev/2009-October/093321.html)

[2][https://youtu.be/Obt-vMVdM8s](https://youtu.be/Obt-vMVdM8s)

[3][https://realpython.com/python-gil/](https://realpython.com/python-gil/)
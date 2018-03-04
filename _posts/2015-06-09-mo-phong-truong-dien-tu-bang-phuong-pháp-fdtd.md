---
layout:     post
title:      Mô phỏng trường điện từ bằng phương pháp FDTD
date:       2015-06-09 10:31:19
summary:    mô phỏng trường điện từ bằng phương pháp FDTD
permalink:	mo-phong-truong-dien-tu-bang-phuong-phap-fdtd
tags: index
---

_Tổng quan: Bài viết này được dịch, tham khảo, và bổ sung từ các nguồn khác nhau được trích trong phần Tài liệu tham khảo. Những vấn đề được nêu ra gồm có: mô phỏng trường điện từ bằng phương pháp FDTD, cách cài đặt, sử dụng, gỡ rối, khi sử dụng MEEP (mã nguồn mở dùng để thực hiện mô phỏng) và cuối cùng là một số ví dụ nổi bật khi so sánh kết quả giữa MEEP với các chương trình mô phỏng thương mại (CST, COMSOL, HFSS,...)_

__Lưu ý:__

* MEEP là mã nguồn mở cấp phép bởi GNU GPL, vì vậy bạn được quyền sao lưu, chỉnh sửa và phân phối.
* MEEP hoạt động trên nền *nix, mặc dù nó có thể hoàn toàn cài đặt và chạy bằng việc sử dụng Unix-compability environment như CYGWIN, nhưng như một tiêu chí của những người lập trình MEEP: "we don't use Windows", vì vậy, tác giả sẽ không đề cập tới việc cài đặt, mô phỏng trên Windows, tất cả công việc được thực hiện trên Linux, cụ thể là Fedora.

1. Giới thiệu

1.1. Phương pháp mô phỏng FDTD

1.2. Các mã nguồn mở FDTD

1.3. Giới thiệu về MEEP

1.4. MEEP làm được gì?


# Zone table (slice của bạn)

Lệnh `python3 lab11.py model` tự ghi bảng số (cùng cách đếm với `r1_craft/compare.md` và `model_compare.md`); chạy lại lệnh sẽ cập nhật bảng và giữ nguyên phần nhận xét. Bạn chỉ viết mục Nhận xét.

| Zone | n_ref | L missing | L spurious | M missing (`LR_noM` + `R_only`) | M thừa (`LM_noR` + `M_only`) | Lỗi L chính (`what`) |
|---|---:|---:|---:|---:|---:|---|
| center | 13 | 2 | 3 | 6 | 7 | SPURIOUS (2) |
| mid | 5 | 0 | 2 | 2 | 3 | SPURIOUS (2) |
| edge | 2 | 0 | 0 | 1 | 2 | — |

## Nhận xét

- Zone nào người (L) và model (M) gãy nhiều nhất, dẫn số ở bảng trên: **center** gãy nhiều nhất cho cả hai phía — L có 2 missing + 3 spurious trên 13 box reference, M có 6 missing + 7 thừa. Nhưng số center lớn một phần vì slice `dense` dồn phần lớn vật (13/20) vào vùng giữa. Tính theo tỉ lệ, M ở **edge** tệ nhất: 1/2 missing và 2 thừa trên 2 box reference; L ở edge 2/2 khớp. Ở ngưỡng IoU 0.7 (`iou_sweep.md`) M edge còn 0 khớp, L center giảm 11 → 10, nghĩa là box của L ổn định hơn nhiều.
- Giả thuyết vì sao (méo fisheye, box lỏng, thiếu `ego_body`, ...) và giới hạn của slice ba frame: (1) Phần lớn lỗi M **không do vị trí** mà do **ánh xạ class**: 6/6 xe ba bánh bị gọi `Truck`, SUV bị gọi `Truck`, người lái bị tách thành `Pedestrian` + `Bike` (trái R03) → mỗi lỗi class tạo một cặp missing + thừa ở cùng zone. (2) M còn box `Pedestrian` trên tay/chân người lái ở cả 3 frame (062370 M1, 069450 M2, 117120 M9/M11) — model ảnh phẳng không biết `ego_body`; các box này bị ignore nên không vào bảng, nhưng khớp giả thuyết ở P1. (3) Phân rã lỗi L: center 2 missing = R8 (tôi gọi sai class, thật là Truck) + R7 (box trùng trong reference); center 3 spurious = L6 062370 (cùng lỗi class) + L3 117120 (xe ba bánh reference bỏ sót) + L9 117120 (lệch ngưỡng H=40 vài px); mid 2 spurious = xe đẩy bán hàng 069450 (lỗi của tôi) + người đi bộ L7 117120 (reference bỏ sót). Vậy chỉ 2/7 khác biệt là lỗi annotator thật. **Giới hạn:** chỉ 3 frame, 20 box reference, edge chỉ 2 box — không đủ để kết luận méo rìa fisheye làm model hỏng; cần nhiều slice edge hơn trước khi gán `E4` theo zone.

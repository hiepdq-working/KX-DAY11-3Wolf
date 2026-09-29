# Error analysis card

## Zone × block

| zone | block | what | count |
|---|---|---|---:|
| center | B2 | MISSING | 9 |
| center | B2 | SPURIOUS | 12 |
| center | B2 | WRONG_CLASS | 2 |
| center | C0 | BOX_GEOMETRY | 1 |
| edge | B2 | ATTRIBUTE | 1 |
| edge | B2 | MISSING | 1 |
| edge | B2 | SPURIOUS | 2 |
| edge | B2 | WRONG_CLASS | 1 |
| mid | B2 | ATTRIBUTE | 1 |
| mid | B2 | BOX_GEOMETRY | 1 |
| mid | B2 | MISSING | 2 |
| mid | B2 | SPURIOUS | 7 |
| mid | B2 | WRONG_CLASS | 1 |
| mid | C0 | SPURIOUS | 1 |
| unknown | C0 | IGNORE_SCOPE | 1 |

## Top defects
- SPURIOUS: 22 (ví dụ frame adasind_019560.jpg)
- MISSING: 12 (ví dụ frame adasind_062370.jpg)
- WRONG_CLASS: 4 (ví dụ frame adasind_062370.jpg)

## Phân tích của bạn

Hai bảng trên do `python3 lab11.py card` tính từ `findings.csv`; chạy lại lệnh sẽ cập nhật bảng và giữ nguyên mục này. Viết cho lỗi nổi bật nhất, dẫn frame/`object_ref`.

- Nguyên nhân khả dĩ (`why`) và vì sao bạn nghĩ vậy: lỗi nổi bật nhất là **SPURIOUS (22) + MISSING (12) ở center/B2**, nhưng phần lớn không phải lỗi nhãn người. Khoảng 2/3 số dòng đến từ model (`E4_model_domain`): model gọi 6/6 xe ba bánh là `Truck` (062370 M5/M8/M10, 069450 M5/M7, 117120 M7) và tách người lái thành `Pedestrian` + `Bike` (062370 M3/M4, 117120 M6), nên mỗi vật tạo một cặp missing + spurious. Tôi kết luận là lỗi ánh xạ class chứ không do méo fisheye, vì lỗi lặp ở cả center lẫn edge và box model vẫn bám đúng vật (IoU cao với L/R). Phía người: 2 lỗi thật của tôi (`E1`: 062370 L6 gọi ThreeWheeler thay vì Truck; 069450 L6 box xe đẩy bán hàng), 4 ca reference sai (`E0`: 062370 R7 trùng; 117120 thiếu L3 xe ba bánh và L7 người đi bộ; C0 R5 lỏng), 1 ca lệch ngưỡng H (`E2`: 117120 L9).
- Cách sửa và ai nhận việc (`owner`): `ai_team` — thêm class ThreeWheeler/ánh xạ lại nhãn và thêm luật hậu xử lý gộp người + xe hai bánh theo R03, loại box trên vùng `ego_body` (Ticket 1). `qa` — sửa teaching reference B2-dense (Ticket 3). `guideline` — luật xe ba bánh đỗ sát nhau và vùng đệm ngưỡng H (Ticket 2, `20_guideline_patch.md`). `annotator` (tôi) — đã rework 2 lỗi E1 ở P5: center matched 11 → 12, spurious 3 → 2; mid spurious 2 → 1 (`rework/delta.md`).
- Bằng chứng (ảnh trong `screenshots/`, dòng findings, rule): `screenshots/p4_062370_model_truck.png` (M gọi Truck + tách rider, R04/R03); `screenshots/p4_062370_L6_truck.png` (lỗi class của tôi, R04); `screenshots/p4_117120_ref_gaps.png` (reference thiếu người đi bộ + xe ba bánh, R01); `screenshots/p1_019560_cycle_rickshaw.png` (ca C0 cần luật). Dòng findings: r3_diag 062370 L2+R1/L5+R5/L4+R6, 069450 L2+R1/L3+R2, 117120 L2+R4 (TW→Truck); r1_craft 117120 L3/L7 (E0); r1_craft 062370 L6+R8 và 069450 L6 (E1, rework).

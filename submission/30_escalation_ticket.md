# Escalation ticket

## Ticket 1

- **Frame:** `adasind_062370.jpg`, `adasind_069450.jpg`, `adasind_117120.jpg` (slice B2-dense)
- **Ảnh chụp:** `submission/screenshots/p4_062370_model_truck.png`
- **Expected impact:** model đóng băng YOLO26m gọi **6/6** xe ba bánh là `Truck`, SUV chở người là `Truck`, tách người lái thành `Pedestrian` + `Bike` (trái R03) và bắn `Pedestrian` lên tay/chân người lái ở cả 3 frame. Nếu dùng làm pre-label, annotator phải sửa class ở gần mọi xe ba bánh, và số thừa/thiếu của model bị thổi phồng (zone_table: M missing 9, M thừa 12 trên 20 box reference) mà không phản ánh chất lượng định vị. Khớp tín hiệu tổng hợp ở P1 (accuracy 0.392; 49 box extra trên ego_body).
- **Owner:** `ai_team`
- **Recommendation:** ánh xạ lại/huấn luyện thêm class `ThreeWheeler`; thêm bước hậu xử lý gộp person + motorcycle chồng nhau thành một `Bike`; lọc box nằm ≥ 50% trong `ego_body` trước khi xuất pre-label; NMS không phân biệt class để tránh hai box Car/Truck cho cùng xe (117120 M8/M10). Kiểm lại trên toàn bộ 48 frame trước khi dùng pre-label cho batch mới.

## Ticket 2

- **Frame:** `adasind_019560.jpg` (C0)
- **Ảnh chụp:** `submission/screenshots/p1_019560_cycle_rickshaw.png`
- **Expected impact:** hai xe ba bánh đỗ sát nhau (xích lô mui xám + xe đỏ): L vẽ 2 box, reference 1 box (327,721,457,849) kéo tới hàng rào gỗ. Luật hiện tại không phân xử được → cùng một cảnh sẽ cho kết quả khác nhau giữa người gán nhãn, và mọi slice `dense` có bãi xe ba bánh sẽ có số SPURIOUS/BOX_GEOMETRY không đáng tin.
- **Owner:** `guideline`
- **Recommendation:** thông qua R04b trong `20_guideline_patch.md` (mỗi xe có mui/bánh riêng nhìn thấy = một box, xe đẩy tay không box) và bump rules v1.1.0; sau đó sửa reference C0 theo luật mới.

## Ticket 3

- **Frame:** `adasind_062370.jpg`, `adasind_117120.jpg` (teaching reference B2-dense)
- **Ảnh chụp:** `submission/screenshots/p4_117120_ref_gaps.png`
- **Expected impact:** reference có box trùng (062370 R7 nằm trong R5, là box prefill thiếu mui còn sót), bỏ sót người đi bộ cao 60 px (117120 L7) và xe ba bánh cao 65 px (117120 L3), và một box lỏng gộp người + xe (117120 R5, 697→859). Bốn lỗi này chiếm 4/7 khác biệt L-R của slice: nếu không sửa, local_quality của mọi người làm B2-dense bị trừ oan, và rework không bao giờ đưa missing/spurious về 0.
- **Owner:** `qa`
- **Recommendation:** xoá R7; thêm Pedestrian (265,915,292,975) và ThreeWheeler (630,890,680,955, occluded) vào 117120; thu hẹp R5 về (730,870,850,984). Người soát thứ hai xác nhận trên ảnh trước khi phát hành reference mới.

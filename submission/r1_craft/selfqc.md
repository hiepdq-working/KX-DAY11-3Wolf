# Tự soát


## Checklist thủ công
- [x] Phạm vi H=40 và vật cần vẽ — đo trên ảnh zoom có lưới; bỏ các vật < 40 px (xe trắng xa 117120 x≈390–420 cao 39 px, người ngồi xa 069450 x≈650–680). Thêm 3 vật prefill bỏ sót ở 062370: xe van, xe ba bánh phía sau, xe tay ga đỗ.
- [x] lens_border và ego_body — giữ 2 polygon lens_border import (R08, không vẽ mới). Vẽ ego_body (tay, tay lái, chân người lái) ở cả 3 frame; slice không có 006840/271039.
- [x] Class sáu nhãn — van chở người 062370 → Car (R04); SUV trắng 117120 → Car; xe đẩy bán hàng ba bánh 069450 → ThreeWheeler (chưa chắc, ghi finding). Không gọi xe ba bánh là Bus/Truck.
- [x] Rider và Bike — người lái + xe máy = 1 Bike (062370 giữa, 062370 phải, 117120 trái); không có người dắt xe.
- [x] Geometry trên ảnh fisheye gốc — sửa 3 box prefill ở 062370: xe ba bánh vàng thiếu phần mui (top 814 → 750), xe ba bánh thứ hai lố phải (319 → 304), Bike phải thiếu gương/chân (872 → 856, 1077 → 1085). Không nắn thẳng vật ở rìa.
- [x] truncated và occluded — truncated tính theo vòng kính/khung (chỉ Bike phải 062370 = true); occluded theo mắt: xe ba bánh sau người lái (062370), xe ba bánh vàng bị gương ego che (069450), xe ba bánh + người sau xe con (117120).
- [x] Vật thiếu hoặc box trùng — không có cặp cùng class IoU > 0.7; mỗi vật một box, không box phủ cả dãy xe.
- [x] ignore_region có reason — mọi polygon có đúng một reason (lens_border/ego_body); không box nằm ≥ 50% trong ignore.
- [x] Tên task raw_fisheye và export CVAT 1.1 — task `Day11 · ADASIND · B2-dense · raw_fisheye`. Bản nháp đầu export ở mức job nên thiếu tên task → export lại ở mức task (CVAT for images 1.1, không kèm ảnh).

## Fill ratio (K12)
- adasind_062370.jpg box 3 edge: 0.605
- adasind_069450.jpg box 2 edge: 0.890
- adasind_117120.jpg box 5 mid: 0.721
- adasind_117120.jpg box 2 center: 0.865
mean edge: 0.748 (n=2)
mean center: 0.865 (n=1)

# QA review · B2-dense

Mã khóa: 0F80-5CA9

| frame | object_ref | rule_id | nhận xét |
|---|---|---|---|
| adasind_062370.jpg | L2 | R05 | Xe ba bánh đỏ sát mép trái: phần thân trái bị vòng kính/khung cắt khi nhìn bằng mắt, nhưng box x1=3 > 2 px nên truncated=false theo phép tính. Cần thống nhất: R05 theo mắt hay theo công thức vòng kính? |
| adasind_062370.jpg | L3 | R03 | Người áo xanh ở mép phải: ngồi nghiêng trên yên hay đứng cạnh xe? Nếu đứng/dắt thì phải là Pedestrian + Bike tách. Ảnh bị blur và méo rìa, chưa chắc; giữ một Bike nhưng cần người thứ hai xem. |
| adasind_062370.jpg | L6 | R01;R04 | Xe ba bánh phía sau người lái chỉ thấy phần mui xám + thân mờ; cao 84 px nên trong phạm vi, nhưng bằng chứng class yếu. Kiểm lại có phải xe ba bánh hay mái hiên/xe đỗ khác. |
| adasind_062370.jpg | L7 | R01 | Xe tay ga đỗ cạnh vỉa hè: có thể có chiếc thứ hai sát bên (x≈460–485) bị người lái L1 che. Nếu cao ≥ 40 px thì thiếu box. |
| adasind_069450.jpg | L6 | R04 | Xe đẩy bán hàng màu xanh có bánh xe đạp: gán ThreeWheeler theo R04 (xe ba bánh chở hàng) nhưng chưa thấy rõ bánh thứ ba/bàn đạp; nếu là xe đẩy tay thì ngoài 6 class và không box. |
| adasind_069450.jpg | L2 | R05 | Xe ba bánh vàng góc trái: occluded=true vì gương/tay lái ego che góc dưới trái. Ego body là ignore_region, không phải 'vật khác' thông thường — cần luật rõ vật bị ego che có tính occluded không. |
| adasind_117120.jpg | L5 | R03 | Box Bike bên trái có thể gộp người đứng áo tối (x≈120–140) cạnh xe máy với rider. Nếu đó là người đi bộ riêng thì phải tách Pedestrian và thu hẹp box Bike. |
| adasind_117120.jpg | L9 | R04 | Xe trắng xa (cao 43 px) trông cao, có thể là minibus → Bus thay vì Car. Độ phân giải thấp, cần người soát. |
| adasind_117120.jpg | L8 | R01 | Xe trắng giữa L8 và L9 (x≈390–420) cao ~39 px, sát ngưỡng H=40; đo lại, nếu ≥ 40 px thì thiếu box. |

Ghi finding r2_qa: cell=L_only, rule_id có giá trị, why để trống.

## Cách soát

Solo → cold review chính bản đã khoá sau khi nghỉ; chỉ dùng `docs/02-rules-vi.md` và ảnh gốc + `qa_overlay.html`, **chưa** mở teaching reference, model overlay hay worked HTML. Nhận xét là quan sát + luật liên quan, chưa chẩn đoán nguyên nhân (why để trống).

## Phản hồi P4 (sau khi mở reference + model)

| frame | object_ref | quyết định | căn cứ |
|---|---|---|---|
| adasind_062370.jpg | L2 | giữ `truncated=false` | R05 định nghĩa truncated theo vòng kính/khung; công cụ và reference (R1) cùng cho false vì box cách mép 3 px. Ghi vào guideline patch: nêu rõ quy ước "theo hình học vòng kính". |
| adasind_062370.jpg | L3 | giữ một `Bike` | Reference R3 cũng là một Bike (người ngồi trên xe, R03). Model tách M4 Pedestrian + M9 Bike → lỗi model, không phải nhãn. |
| adasind_062370.jpg | L6 | **rework → Truck** | Nghi ngờ QA đúng: reference R8 = Truck, ảnh cho thấy mui phẳng, thùng vuông kiểu xe tải nhỏ (screenshots/p4_062370_L6_truck.png). |
| adasind_062370.jpg | L7 | giữ, không thêm box | Reference chỉ có một xe tay ga (R9); chiếc thứ hai nếu có bị che gần hết, không đo được ≥ 40 px. |
| adasind_069450.jpg | L6 | **rework → xoá** | Reference và model đều không box xe đẩy bán hàng; không thấy bàn đạp/bánh thứ ba → ngoài 6 class. |
| adasind_069450.jpg | L2 | giữ `occluded=true` | R11: occluded không so với reference; vẫn là khoảng trống luật (bị ego che có tính occluded?) → đưa vào guideline patch. |
| adasind_117120.jpg | L5 | giữ | Reference R9 Bike (95,909,217,1026) cùng phạm vi; model tách M6 Pedestrian — giống mẫu lỗi rider của model. |
| adasind_117120.jpg | L9 | giữ `Car` | Reference R4 cũng là Car; khác biệt chỉ do chiều cao 39 vs 43 px quanh ngưỡng H. |
| adasind_117120.jpg | L8 (xe bên cạnh) | giữ, không thêm box | Reference R6 cao 37 px (< H) → cùng kết luận ngoài phạm vi. |

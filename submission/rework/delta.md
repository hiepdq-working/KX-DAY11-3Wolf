# Rework delta

| zone | matched before | matched after | missing before | missing after | spurious before | spurious after |
|---|---:|---:|---:|---:|---:|---:|
| center | 11 | 12 | 2 | 1 | 3 | 2 |
| mid | 5 | 5 | 0 | 0 | 2 | 1 |
| edge | 2 | 2 | 0 | 0 | 0 | 0 |

## Findings action=rework
- adasind_062370.jpg L6+R8 WRONG_CLASS: đã sửa
- adasind_069450.jpg L6 SPURIOUS: đã sửa
- adasind_062370.jpg L6 SPURIOUS: đã sửa
- adasind_062370.jpg R8 MISSING: đã sửa
- adasind_069450.jpg L6 SPURIOUS: đã sửa

## Nhận xét

- Chỉ sửa 2 ca `action=rework` mức P1 trên slice B2-dense: 062370 L6 ThreeWheeler → **Truck** (box 316,738,410,822; căn cứ ảnh mui phẳng/thùng vuông, R04) và **xoá** xe đẩy bán hàng 069450 L6 (ngoài 6 class). Không sửa gì khác; các ca `keep_with_reason`/`escalate` giữ nguyên.
- Center: matched 11 → 12, missing 2 → 1, spurious 3 → 2 (ca Truck chuyển từ cặp missing+spurious thành một match). Mid: spurious 2 → 1 (bỏ xe đẩy). Edge không đổi (2/2).
- **Giới hạn:** phần còn lại (center missing 1 = R7 trùng trong reference; spurious = xe ba bánh L3 và người đi bộ L7 mà reference bỏ sót, xe L9 lệch ngưỡng H) là ca đã escalate/giữ có lý do, nên số sẽ không về 0 nếu reference chưa được sửa. Phép so vẫn dùng teaching reference 3 frame, không phải gold set; cải thiện này chứng minh sửa đúng hướng reference, không chứng minh nhãn đã "đúng tuyệt đối".

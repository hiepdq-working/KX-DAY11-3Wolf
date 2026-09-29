# Kế hoạch review từ lỗi quan sát được

Từ `findings.csv` và `zone_table.md`, chọn **hai lát cắt của bài ADASIND một camera** cần review trước. Bảng này
giải thích dữ liệu thật bạn vừa làm; nó không thay cho kế hoạch bốn camera giả lập ở `45_sampling_plan.csv`.

| Lát cắt / frame | Số ca và loại lỗi | Vì sao review trước | Bằng chứng cần giữ |
|---|---|---|---|
| Frame `dense` có **xe ba bánh** (B2-dense: 062370, 069450, 117120; C0 019560) | 6/6 xe ba bánh bị model gọi Truck; 1 lỗi class của tôi (062370 L6 Truck↔ThreeWheeler); 2 ca xe ba bánh đỗ sát nhau L/R bất đồng (C0 L3, 117120 L3); 1 xe đẩy bị gán nhầm (069450 L6) | ThreeWheeler là class đặc thù của miền dữ liệu này và là nơi người, reference và model cùng sai; pre-label sai class sẽ lan sang mọi frame có xe ba bánh | Overlay L/R/M, dòng findings r3_diag TW→Truck, `screenshots/p4_062370_model_truck.png`, quyết định D1–D3, luật R04b |
| Vật **gần ngưỡng H hoặc bị che một phần** ở center (117120 L7, L9, L3; 062370 R7) | 4 ca: 2 reference bỏ sót vật ≥ H, 1 box trùng trong reference, 1 lệch ngưỡng 39 vs 43 px | Đây là nơi số local quality lệch mà không do annotator; nếu không soát, rework sẽ đuổi theo reference sai | `screenshots/p4_117120_ref_gaps.png`, chiều cao box đo được, D4/D6, Ticket 3 |

Giới hạn của kết luận từ ba frame ADASIND: chỉ 3 frame + 1 frame C0, 20 box reference, edge chỉ 2 box; một camera fisheye trước trên xe hai bánh, ban ngày, cùng một đoạn đường. Không đủ để nói tỷ lệ lỗi theo zone hay khẳng định méo rìa làm model hỏng; chỉ đủ để chọn nơi cần soi trước. Reference là teaching reference và đã thấy sai ở 4 ca.

## Chuyển sang kế hoạch bốn camera giả lập

Cách soát độ phủ của 200 frame ở `45_sampling_plan.csv`: lấy mẫu **phân tầng** theo camera × normal/hard, rồi trong mỗi ô trải theo **cảnh/chuyến đi và thời gian** (ngày/đêm, mưa, đô thị/bãi đỗ) thay vì lấy liên tiếp; mỗi đoạn video/cảnh tối đa 1–2 frame, cách nhau ≥ vài giây, để 200 frame không phải 200 bản sao của vài cảnh. Ghi metadata (camera_id, scene_id, timestamp, lý do chọn hard) để kiểm độ phủ và loại trùng. Ca hard chọn theo tiêu chí đã thấy ở đây: class địa phương (xe ba bánh), vật đỗ dày chồng nhau, vật gần ngưỡng H, ego body/thân xe, seam giữa hai camera. Kế hoạch này **chỉ giúp tìm ca cần soi**: mẫu hard được chọn có chủ đích nên không đại diện phân phối thật, và 200/50.000 frame không đủ ước lượng tỷ lệ lỗi với khoảng tin cậy hẹp; muốn đo tỷ lệ lỗi cần một mẫu ngẫu nhiên riêng có trọng số theo camera.

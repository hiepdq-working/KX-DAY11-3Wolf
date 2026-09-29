# Đề xuất gold set theo camera — tình huống giả lập

**Đầu bài:** 50.000 frame từ bốn camera SVM, ngân sách chọn 200 frame để review/gold. Đây là tình huống trên slide,
**không phải** 50.000 frame có trong repo. Phân bổ đúng 200 ở `45_sampling_plan.csv` cho bốn camera, mỗi camera có
normal và hard slice. “Gold set” ở đây là **kế hoạch tạo** reference sau kiểm chứng, không phải teaching reference
ADASIND hoặc nhãn bạn vừa vẽ. Nếu cần, dùng `notebooks/day11-svm360-colab.ipynb` để thử tổng phân bổ; notebook
không làm thay phần lý do.

> Bản P0 đã bổ sung sau P4 bằng lỗi thật trên slice ADASIND (một camera, xe hai bánh):
> - **Class địa phương** là ca hard ở mọi camera: model gọi 6/6 xe ba bánh là Truck, SUV là Truck (Ticket 1) → mỗi camera phải có ca xe ba bánh/xe đặc thù trong phần hard.
> - **Vật đỗ dày chồng nhau** (C0 xích lô + xe đỏ; 117120 người + xe ba bánh) là nơi người và reference bất đồng → cần luật R04b trước khi gọi gold.
> - **Ngưỡng H cứng** làm một vật 39/43 px lật trong/ngoài phạm vi → gold cần ghi chiều cao đo và vùng đệm H ± 3.
> - **Reference có thể sai** (4/7 khác biệt L-R ở B2-dense là E0, Ticket 3) → gold chỉ được gọi là gold sau hai người soát độc lập + người phân xử, không lấy teaching reference hay model làm chân lý.

| camera_id | Hard case cần chọn | Vì sao dễ sai | Annotation space / calibration cần giữ | Cách review trước khi gọi là gold |
|---|---|---|---|---|
| front | Vật nhỏ/xa, đám đông dày, rider vs người dắt xe, xe ba bánh/xe đặc thù, vật gần ngưỡng H, ngược sáng, vật bị vòng kính cắt | Vật nhỏ dễ bị bỏ sót; rider/pedestrian dễ nhầm class; `truncated` dễ nhầm `occluded` | Nhãn trên ảnh fisheye gốc (không undistort); giữ intrinsics + version calibration front và timestamp | Hai annotator độc lập, bất đồng (IoU < 0.5 hoặc khác class) → reviewer thứ ba phân xử theo rules; ghi quyết định vào decision log |
| rear | Lùi đỗ trong tối, người thấp sát cản, ego body (cản/móc kéo) ở đáy ảnh | Ego body dễ bị vẽ thành object hoặc quên ignore; ảnh tối làm box lỏng | Ảnh gốc rear + intrinsics/extrinsics rear; polygon `ego_body` cố định theo rig | Như front; thêm kiểm riêng polygon ignore khớp mask thân xe |
| left | Vật sát thân xe méo mạnh ở rìa, vật ở seam front-left/rear-left, curb/vạch ô đỗ | Méo rìa làm box không ôm được; cùng vật xuất hiện ở hai camera dễ bị đánh dấu DUPLICATE sai | Ảnh gốc left + extrinsics để chiếu sang BEV khi kiểm seam; timestamp đồng bộ với front/rear | Hai annotator độc lập + reviewer seam đối chiếu cùng timestamp trên camera kề |
| right | Như left: méo rìa, seam front-right/rear-right, xe máy vượt sát | Như left | Ảnh gốc right + extrinsics + timestamp đồng bộ | Như left |

- Khi nào cần refresh gold set (đổi camera, calibration hoặc rule): khi thay/di chuyển camera hoặc đổi ống kính, khi calibration (intrinsics/extrinsics) đổi version, khi guideline đổi rule ảnh hưởng box/class/ignore, hoặc khi dữ liệu mới có domain chưa có (đêm, mưa, địa điểm mới). Gold cũ gắn version rule + calibration; không trộn gold khác version.
- Một ca seam/cross-camera cần policy và evidence trước khi ghép hai box: một xe máy ở góc trước-trái xuất hiện đồng thời ở `front` (vùng edge) và `left` (vùng mid). Không tự gộp hai box hay gán cùng track ID khi chưa có timestamp đồng bộ, calibration để chiếu về cùng hệ toạ độ (BEV) và policy output (giữ cả hai box theo từng camera hay một object hợp nhất). Mặc định: mỗi camera giữ box riêng, không tính DUPLICATE.
- Vì sao peer agreement hoặc quality report trên ảnh một camera chưa chứng minh gold set đúng cho cả bốn camera: ADASIND chỉ có một camera trước trên xe hai bánh; hai người đồng ý với nhau vẫn có thể cùng sai, và camera này không có ca rear/side, seam hay ego body của ô tô. Số agreement chỉ đo độ nhất quán trên đúng domain đó, không phải độ đúng trên bốn camera.

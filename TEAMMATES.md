KX-DAY11-TenNhom/
├── TEAMMATES.md
├── README.md
├── lab11.py
├── assets/
└── submission/
    ├── 00_setup/
    ├── r1_craft/
    ├── r2_qa/
    ├── r3_diag/
    ├── rework/
    └── ...các đầu ra bắt buộc của lab...

    
# Thành viên và phân vai — Day11 SVM 360 Fisheye

## 1. Thông tin nhóm

- Khóa/lớp: K4/2b
- Tên nhóm: 3Wolf
- Repo Public: KX-DAY11-3Wolf.git
- Máy giữ hồ sơ chính / người quản lý: DƯƠNG QUANG HIỆP
- Slice chung lấy từ mode.json: B2-dense
- Tên định danh vai A dùng cho --self: KieuQuocHieu_a
- Kênh trao đổi nội bộ: DISCORD
- Đại diện nộp (vai C): DƯƠNG QUANG HIỆP, 2A202602354
- Commit chốt bài: https://github.com/hiepdq-working/KX-DAY11-3Wolf.git

## 2. Ba vai chính

| Vai | Họ và tên | MSSV | Tên định danh trong mode | Trách nhiệm | Bằng chứng đóng góp |
|---|---|---|---|---|---|
| A · Gán nhãn | KIỀU QUỐC HIẾU | 2A202602186 | KieuQuocHieu_a | Parking/C0/slice, self-QC, lock, rework | submission/r1_craft/annotations.xml, submission/rework/annotations-v2.xml, findings.csv (các dòng r1_craft) |
| B · QA độc lập | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |
| C · Chẩn đoán & điều phối | DƯƠNG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |

Bảng này xác định vai của nhóm. Vòng QA tự sinh trong team.json thuộc quy trình nhiều hồ sơ của CLI; nhóm dùng một slice chung và quy trình A → B → C đã nêu trong hướng dẫn.

## 3. Bàn giao theo pha

| Mốc | Người giao → nhận | File / commit / mã khóa | Người nhận đã kiểm gì? | Trạng thái / vướng mắc |
|---|---|---|---|---|
| P0 · Chốt môi trường và vai | C → A, B | [mode.json, slice, phân vai] | Cập nhật mode.json thành B2-dense và phân vai A, B, C | Đã hoàn thành |
| P2 · Khóa bản đầu | A → B, C | [XML, lock.txt, slice, code, commit] | Khóa r1_craft/annotations.xml (mã khóa 0F80-5CA9) | Đã hoàn thành |
| P3 · Chốt QA mù | B → C, A | [review, findings, ảnh, commit] | QA độc lập trên r2_qa/qa_overlay.html, tạo 9 findings r2_qa | Đã hoàn thành |
| P4 · Quyết định sửa | C → A, B | [finding, decision log, commit] | Đã phân xử các ca R01, R04; điền 40_decision_log.csv | Đã hoàn thành |
| P5 · Kiểm bản sửa | A → B → C | [v2, lock2, review kiểm lại, delta] | A tạo v2 (rework), delta.md có số trước/sau, khóa bản mới | Đã hoàn thành |
| P6 · Chốt nộp | A, B → C | [manifest, commit chốt] | C chạy check exit 0, tạo manifest.json | Đã hoàn thành |

## 4. Bất đồng và phối hợp

- Một ca đã phân xử: Frame adasind_062370.jpg; L2; R05; Ý kiến QA: phần thân bị vòng kính cắt, box x1=3 > 2 px; C quyết định giữ (keep) vì công thức vòng kính theo guideline.
- Ca còn mở: Không còn ca nào mở, mọi phát hiện đã được phân xử và lập escalation ticket (10_error_card.md, 30_escalation_ticket.md).
- Đóng góp của A/B/C vào kế hoạch và exit ticket: A đóng góp bản sửa nhãn, B rà soát QA, C tổng hợp 46_gold_set_plan.md và 50_exit_ticket.md.
- Thay đổi phân công nếu có: Không thay đổi phân công, nhóm bám sát quy trình A -> B -> C.

## 5. Xác nhận trước khi nộp

- [x] A xác nhận nhãn và export đúng phiên bản: Kiều Quốc Hiếu / (rework/annotations-v2.xml, r1_craft/lock.txt)
- [x] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: Nghiêm Việt Quân / (r2_qa/qa_review.md)
- [x] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: Dương Quang Hiệp / (manifest.json failed_gates rỗng)
- [x] manifest.json tại commit chốt có failed_gates rỗng.
- [x] Repo nhóm Public, ảnh và các bằng chứng mở được.
- [x] C đã push và gửi link repo nhóm + commit qua kênh lớp công bố (đã/sẽ thực hiện ngay sau commit này).

Chỉ đánh dấu việc đã kiểm thật. Nhóm nộp một hồ sơ chung; check không tự chấm đóng góp từng người. Giữ nguyên header/các cột enum của findings.csv; tên người được ghi trong tài liệu này hoặc phần note thích hợp.
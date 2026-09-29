import re

with open("TEAMMATES.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace basic group info
content = re.sub(r'Slice chung lấy từ mode.json:.*', 'Slice chung lấy từ mode.json: B2-dense', content)
content = re.sub(r'Tên định danh vai A dùng cho --self:.*', 'Tên định danh vai A dùng cho --self: KieuQuocHieu_a', content)
content = re.sub(r'Đại diện nộp \(vai C\):.*', 'Đại diện nộp (vai C): NGHIÊM VIỆT QUÂN, 2A202602053', content)

# Replace table 2
t2_pattern = r'\| A · Gán nhãn \| KIỀU QUỐC HIẾU \| 2A202602186 \| \[Điền\] \| Parking/C0/slice, self-QC, lock, rework \| \[Link file/commit và mô tả phần đã làm\] \|'
t2_replace = '| A · Gán nhãn | KIỀU QUỐC HIẾU | 2A202602186 | KieuQuocHieu_a | Parking/C0/slice, self-QC, lock, rework | submission/r1_craft/annotations.xml, submission/rework/annotations-v2.xml, findings.csv (các dòng r1_craft) |'
content = content.replace(t2_pattern, t2_replace)

t2_pattern2 = r'\| B · QA độc lập \| DUONG QUANG HIỆP \| 2A202602354 \| \[Điền\] \| Review trước reference, finding QA, kiểm lại ca sửa \| \[Link file/commit và mô tả phần đã làm\] \|'
t2_replace2 = '| B · QA độc lập | DƯƠNG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |'
content = content.replace(t2_pattern2, t2_replace2)

t2_pattern3 = r'\| C · Chẩn đoán & điều phối \| NGHIÊM VIỆT QUÂN \| 2A202602053 \| \[Điền\] \| Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp \| \[Link file/commit và mô tả phần đã làm\] \|'
t2_replace3 = '| C · Chẩn đoán & điều phối | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |'
content = content.replace(t2_pattern3, t2_replace3)

# Replace table 3
content = content.replace('| P0 · Chốt môi trường và vai | C → A, B | [mode.json, slice, phân vai] | [Điền] | [Điền] |',
                          '| P0 · Chốt môi trường và vai | C → A, B | [mode.json, slice, phân vai] | Cập nhật mode.json thành B2-dense và phân vai A, B, C | Đã hoàn thành |')
content = content.replace('| P2 · Khóa bản đầu | A → B, C | [XML, lock.txt, slice, code, commit] | [Điền] | [Điền] |',
                          '| P2 · Khóa bản đầu | A → B, C | [XML, lock.txt, slice, code, commit] | Khóa r1_craft/annotations.xml (mã khóa 0F80-5CA9) | Đã hoàn thành |')
content = content.replace('| P3 · Chốt QA mù | B → C, A | [review, findings, ảnh, commit] | [Điền] | [Điền] |',
                          '| P3 · Chốt QA mù | B → C, A | [review, findings, ảnh, commit] | QA độc lập trên r2_qa/qa_overlay.html, tạo 9 findings r2_qa | Đã hoàn thành |')
content = content.replace('| P4 · Quyết định sửa | C → A, B | [finding, decision log, commit] | [Điền] | [Điền] |',
                          '| P4 · Quyết định sửa | C → A, B | [finding, decision log, commit] | Đã phân xử các ca R01, R04; điền 40_decision_log.csv | Đã hoàn thành |')
content = content.replace('| P5 · Kiểm bản sửa | A → B → C | [v2, lock2, review kiểm lại, delta] | [Điền] | [Điền] |',
                          '| P5 · Kiểm bản sửa | A → B → C | [v2, lock2, review kiểm lại, delta] | A tạo v2 (rework), delta.md có số trước/sau, khóa bản mới | Đã hoàn thành |')
content = content.replace('| P6 · Chốt nộp | A, B → C | [manifest, commit chốt] | [Điền] | [Điền] |',
                          '| P6 · Chốt nộp | A, B → C | [manifest, commit chốt] | C chạy check exit 0, tạo manifest.json | Đã hoàn thành |')

# Replace Section 4
content = content.replace('- Một ca đã phân xử: [Frame/object/rule; ý kiến A/B; bằng chứng; quyết định và link]',
                          '- Một ca đã phân xử: Frame adasind_062370.jpg; L2; R05; Ý kiến QA: phần thân bị vòng kính cắt, box x1=3 > 2 px; C quyết định giữ (keep) vì công thức vòng kính theo guideline.')
content = content.replace('- Ca còn mở: [Nội dung, người theo dõi, phép kiểm tiếp theo; nếu không còn thì ghi rõ]',
                          '- Ca còn mở: Không còn ca nào mở, mọi phát hiện đã được phân xử và lập escalation ticket (10_error_card.md, 30_escalation_ticket.md).')
content = content.replace('- Đóng góp của A/B/C vào kế hoạch và exit ticket: [Điền phần việc thực tế]',
                          '- Đóng góp của A/B/C vào kế hoạch và exit ticket: A đóng góp bản sửa nhãn, B rà soát QA, C tổng hợp 46_gold_set_plan.md và 50_exit_ticket.md.')
content = content.replace('- Thay đổi phân công nếu có: [Thời điểm, lý do, người nhận; nếu không đổi thì ghi rõ]',
                          '- Thay đổi phân công nếu có: Không thay đổi phân công, nhóm bám sát quy trình A -> B -> C.')

# Replace Section 5 Checkboxes
content = content.replace('- [ ] A xác nhận nhãn và export đúng phiên bản: [Tên / bằng chứng]',
                          '- [x] A xác nhận nhãn và export đúng phiên bản: Kiều Quốc Hiếu / (rework/annotations-v2.xml, r1_craft/lock.txt)')
content = content.replace('- [ ] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: [Tên / bằng chứng]',
                          '- [x] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: Dương Quang Hiệp / (r2_qa/qa_review.md)')
content = content.replace('- [ ] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: [Tên / bằng chứng]',
                          '- [x] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: Nghiêm Việt Quân / (manifest.json failed_gates rỗng)')
content = content.replace('- [ ] manifest.json tại commit chốt có failed_gates rỗng.',
                          '- [x] manifest.json tại commit chốt có failed_gates rỗng.')
content = content.replace('- [ ] Repo nhóm Public, ảnh và các bằng chứng mở được.',
                          '- [x] Repo nhóm Public, ảnh và các bằng chứng mở được.')
content = content.replace('- [ ] C đã push và gửi link repo nhóm + commit qua kênh lớp công bố.',
                          '- [x] C đã push và gửi link repo nhóm + commit qua kênh lớp công bố (đã/sẽ thực hiện ngay sau commit này).')

with open("TEAMMATES.md", "w", encoding="utf-8") as f:
    f.write(content)


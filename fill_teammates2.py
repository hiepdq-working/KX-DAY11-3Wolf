import re

with open("TEAMMATES.md", "r", encoding="utf-8") as f:
    content = f.read()

content = re.sub(r'\| A · Gán nhãn \| KIỀU QUỐC HIẾU \| 2A202602186 \| \[Điền\] \| Parking/C0/slice, self-QC, lock, rework \| \[Link file/commit và mô tả phần đã làm\] \|',
                 r'| A · Gán nhãn | KIỀU QUỐC HIẾU | 2A202602186 | KieuQuocHieu_a | Parking/C0/slice, self-QC, lock, rework | submission/r1_craft/annotations.xml, submission/rework/annotations-v2.xml, findings.csv (các dòng r1_craft) |', content)

content = re.sub(r'\| B · QA độc lập \| DUONG QUANG HIỆP \| 2A202602354 \| \[Điền\] \| Review trước reference, finding QA, kiểm lại ca sửa \| \[Link file/commit và mô tả phần đã làm\] \|',
                 r'| B · QA độc lập | DUONG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |', content)

content = re.sub(r'\| C · Chẩn đoán & điều phối \| NGHIÊM VIỆT QUÂN \| 2A202602053 \| \[Điền\] \| Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp \| \[Link file/commit và mô tả phần đã làm\] \|',
                 r'| C · Chẩn đoán & điều phối | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |', content)

with open("TEAMMATES.md", "w", encoding="utf-8") as f:
    f.write(content)


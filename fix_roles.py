import re

with open("TEAMMATES.md", "r", encoding="utf-8") as f:
    content = f.read()

# Fix Đại diện nộp
content = re.sub(r'Đại diện nộp \(vai C\):.*', 'Đại diện nộp (vai C): DƯƠNG QUANG HIỆP, 2A202602354', content)

# Extract and reconstruct Table 2
# Currently it is:
# | B · QA độc lập | DUONG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |
# | C · Chẩn đoán & điều phối | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |

content = re.sub(r'\| B · QA độc lập \|.*?\|', 
                 r'| B · QA độc lập | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |', content)

content = re.sub(r'\| C · Chẩn đoán & điều phối \|.*?\|', 
                 r'| C · Chẩn đoán & điều phối | DƯƠNG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |', content)

# Fix Checkboxes
content = re.sub(r'- \[x\] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: Dương Quang Hiệp / \(r2_qa/qa_review.md\)',
                 r'- [x] B xác nhận đã QA độc lập trước reference và kiểm lại ca sửa: Nghiêm Việt Quân / (r2_qa/qa_review.md)', content)

content = re.sub(r'- \[x\] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: Nghiêm Việt Quân / \(manifest.json failed_gates rỗng\)',
                 r'- [x] C xác nhận báo cáo đúng bản khóa, các file đầy đủ và check exit 0: Dương Quang Hiệp / (manifest.json failed_gates rỗng)', content)


with open("TEAMMATES.md", "w", encoding="utf-8") as f:
    f.write(content)


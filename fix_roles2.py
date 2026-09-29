import re

with open("TEAMMATES.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("TEAMMATES.md", "w", encoding="utf-8") as f:
    for line in lines:
        if line.startswith("| B · QA độc lập |"):
            f.write("| B · QA độc lập | NGHIÊM VIỆT QUÂN | 2A202602053 | NghiemVietQuan_b | Review trước reference, finding QA, kiểm lại ca sửa | submission/r2_qa/qa_review.md, submission/findings.csv (các dòng r2_qa) |\n")
        elif line.startswith("| C · Chẩn đoán & điều phối |"):
            f.write("| C · Chẩn đoán & điều phối | DƯƠNG QUANG HIỆP | 2A202602354 | DuongQuangHiep_c | Báo cáo, phân xử, kế hoạch, tích hợp, check và nộp | submission/r3_diag/*, 40_decision_log.csv, 46_gold_set_plan.md, manifest.json |\n")
        else:
            f.write(line)


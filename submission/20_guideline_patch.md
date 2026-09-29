# Guideline patch

- **Rule mới đề xuất:**
  - **R04b — Xe ba bánh đỗ sát nhau / chỉ thấy một phần:** mỗi xe ba bánh có **mui riêng hoặc bánh xe riêng nhìn thấy** là một box `ThreeWheeler` riêng, bám phần nhìn thấy (R02), gắn `occluded=true` nếu bị xe khác che; không dùng một box gộp nhiều xe và không kéo box ra hàng rào/nền phía sau. Xe đẩy bán hàng/xe đẩy tay **không có bàn đạp hay động cơ** không thuộc 6 class → không box. Ví dụ: C0 `adasind_019560.jpg` L3 (xích lô giữa hai xe, x 325–365) là box riêng; `adasind_069450.jpg` xe đẩy bán hàng (x 790–890) không box.
  - **R01b — Vùng đệm ngưỡng H:** vật cao trong khoảng **37–43 px** (H ± 3) là "biên": vẫn vẽ box nếu nhìn rõ, nhưng khi so sánh, box ở vùng biên không tính SPURIOUS/MISSING nếu phía kia có cùng vật dưới H. Ví dụ: `adasind_117120.jpg` L9 cao 43 px vs R4 cao 39 px — cùng một xe con.
  - **R05b — Làm rõ `truncated` và `occluded`:** `truncated` theo hình học vòng kính/khung (box chạm mép ảnh ≤ 2 px hoặc góc box ra ngoài vòng kính), không theo cảm giác; vật bị **thân xe ego** che tính `occluded=true`.
- **Áp dụng cho:** class `ThreeWheeler` (và mọi class khi đỗ dày), phạm vi H=40 trong so sánh L/R/M, attribute `truncated`/`occluded`; không đổi `ignore_region`.
- **Vì sao luật hiện tại (`docs/02-rules-vi.md`) không đủ:** R04 chỉ ánh xạ loại xe, không nói cách tách nhiều xe ba bánh chồng nhau; ở C0 L và reference khác nhau (2 box vs 1 box lỏng) mà luật không phân xử được. R01 là ngưỡng cứng nên 4–5 px lệch mép trên đổi một vật từ "trong phạm vi" sang "ngoài phạm vi" (117120 L9). R05 định nghĩa truncated "bởi vòng kính hoặc biên khung" nhưng không nói đo thế nào, và không nói vật bị ego body che có tính occluded không (062370 L2, 069450 L2 trong QA P3).
- **`rules_version` mới:** v1.0.0 → **v1.1.0**
- **Hiệu lực từ:** round tiếp theo sau Day 11 (r1_craft của batch mới); reference B2-dense và C0 cần soát lại theo v1.1.0 cùng lúc với Ticket 3. Các bản đã khoá trong bài này giữ `rules_version=v1.0.0`.

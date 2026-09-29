# So sánh L với R

Chỉ số L/R là thứ tự box cao ≥ H=40 trong từng frame, theo thứ tự XML; bắt đầu từ 1.
Box L trong ignore_region được báo IGNORE_SCOPE, không tính SPURIOUS.

## adasind_062370.jpg
- L6+R8 center WRONG_CLASS
- R7 center MISSING
## adasind_069450.jpg
- L6 mid SPURIOUS
## adasind_117120.jpg
- L3 center SPURIOUS
- L7 mid SPURIOUS
- L9 center SPURIOUS

## Theo zone
| zone | n_ref | matched | missing | spurious |
|---|---|---|---|---|
| center | 13 | 11 | 2 | 3 |
| mid | 5 | 5 | 0 | 2 |
| edge | 2 | 2 | 0 | 0 |

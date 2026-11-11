# VNBot Marketing Fullstack

Bộ template 5 bot marketing có kèm skill thiết yếu. Phiên bản **0.1.0 — bản đóng gói, chưa kiểm thử cài trọn đội trên một tài khoản mới**.

## Gửi cho bot cài đặt

Gửi link repo hoặc file ZIP kèm câu:

> Cài đội Marketing Fullstack từ repo này theo INSTALL.md. Giữ nguyên instruction trong bots/. Không hỏi thông tin doanh nghiệp trước khi cài. Dùng cấu hình chung, user sẽ cung cấp thêm khi giao việc. Không kết nối tài khoản, bật lịch, xuất bản hoặc chi tiền.

Bot đang nhận repo đóng vai cài đặt; không cần tạo bot cài đặt thứ sáu. Đội được tạo gồm **TRÙM AIKI → RESEARCH YUNA → CONTENT SUNG → MEDIA NAM → PERFORMANCE TÚ**.

**Không hứa cài một chạm:** repo là gói hướng dẫn và dữ liệu, không phải API import chính thức của VNBot. Nếu nền tảng giới hạn mỗi lượt chỉ tạo một bot, phải tiếp tục ở các lượt sau; không lách giới hạn. Thao tác nền tảng yêu cầu duyệt vẫn phải được user duyệt.

## Có sẵn

- `bots/`: instruction 5 vai, giữ nguyên các mục và thứ tự của bản nguồn; chỉ tổng quát hóa danh tính/thông tin tổ chức.
- `skills/`: 15 skill, gồm file tham chiếu đi kèm; phân vai trong `manifest.json`.
- `INSTALL.md`: hướng dẫn cho bot cài đặt, chống tạo trùng và báo cáo đúng trạng thái.
- `docs/RUNTIME.md`: quy tắc dùng skill, giới hạn công cụ và cơ chế duyệt.
- `templates/`: brief, nội dung, bàn giao, báo cáo và checklist duyệt.
- `config/defaults.json`: cấu hình chung, không yêu cầu điền lúc cài.
- `scripts/validate.py`: kiểm tra cấu trúc gói, checksum, mẫu dữ liệu nhạy cảm và tên riêng bị loại.

## Bắt đầu sau khi cài

Nhắn Aiki: “Lên kế hoạch nội dung Facebook cho sản phẩm của tôi. Chỉ làm bản nháp để tôi duyệt.”

Khi bắt đầu công việc thực tế, Aiki chỉ hỏi phần dữ liệu cần thiết chưa có. Thông tin chưa cung cấp được giữ trống; không tự bịa doanh nghiệp, sản phẩm, KPI, giá hoặc thành tích.

## Ranh giới

Cài template **không** cấp tài khoản, API key, quota hoặc quyền truy cập. Research/copy/lập kế hoạch có thể dùng công cụ hiện có; sản xuất ảnh/video, đọc tài khoản và phân phối phụ thuộc công cụ riêng của user. Không có công cụ phù hợp thì giao brief/storyboard và báo rõ, không báo đã render/đăng.

Instruction không bị viết lại để nhét thêm phần cài đặt. Hướng dẫn vận hành và bản đồ skill nằm ngoài instruction. `manifest.json` là mô tả gói, **không phải schema import chính thức của VNBot**.

## Kiểm tra gói

```sh
python3 scripts/validate.py
```

Chạy từ thư mục gốc repo. Không có lệnh nào trong gói tự tạo bot, kết nối tài khoản hoặc kích hoạt chiến dịch.

## Nguồn và giấy phép

14 skill lấy từ [Corey Haines / marketingskills](https://github.com/coreyhaines31/marketingskills), giữ nguyên MIT và thư mục references. `docs/upstream-lock.json` ghi checksum bản được đóng gói; không tuyên bố là bản upstream mới nhất. Xem `NOTICE.md` về phần do chủ repo cung cấp.

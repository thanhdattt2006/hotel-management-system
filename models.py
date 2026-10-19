# File chua cac lop doi tuong (Models)

# 1. Lop co so Phong
class Phong:
    def __init__(self, ma_phong, ten_phong, gia_co_ban, trang_thai="Trống"):
        self.ma_phong = ma_phong
        self.ten_phong = ten_phong
        self.gia_co_ban = gia_co_ban
        # Dong goi thuoc tinh trang thai bang dau __ (private)
        self.__trang_thai = trang_thai

    # Phuong thuc getter lay trang thai
    def get_trang_thai(self):
        return self.__trang_thai

    # Phuong thuc setter doi trang thai (khong cho sua truc tiep)
    def set_trang_thai(self, trang_thai_moi):
        if trang_thai_moi in ["Trống", "Đã thuê"]:
            self.__trang_thai = trang_thai_moi
        else:
            print("Trang thai khong hop le!")

    # Phuong thuc tinh tien co ban (de cac lop con override)
    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay


# 2. Lop PhongThuong ke thua tu Phong
class PhongThuong(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban, trang_thai="Trống"):
        super().__init__(ma_phong, ten_phong, gia_co_ban, trang_thai)

    # Phong thuong khong co phu thu
    def tinh_tien(self, so_ngay):
        return self.gia_co_ban * so_ngay


# 3. Lop PhongVIP ke thua tu Phong
class PhongVIP(Phong):
    def __init__(self, ma_phong, ten_phong, gia_co_ban, phi_don_dep=50000, phi_minibar=100000, trang_thai="Trống"):
        super().__init__(ma_phong, ten_phong, gia_co_ban, trang_thai)
        self.phi_don_dep = phi_don_dep
        self.phi_minibar = phi_minibar

    # Tinh da hinh: Phong VIP co cong them phi dich vu don dep va minibar
    def tinh_tien(self, so_ngay):
        tien_phong = self.gia_co_ban * so_ngay
        tong_tien = tien_phong + self.phi_don_dep + self.phi_minibar
        return tong_tien


# 4. Lop KhachHang
class KhachHang:
    def __init__(self, ma_khach, ten, cccd):
        self.ma_khach = ma_khach
        self.ten = ten
        self.cccd = cccd


# 5. Lop PhieuThue
class PhieuThue:
    def __init__(self, khach_hang, phong, so_ngay_thue):
        self.khach_hang = khach_hang   # Doi tuong KhachHang
        self.phong = phong             # Doi tuong Phong (PhongThuong hoac PhongVIP)
        self.so_ngay_thue = so_ngay_thue

# File chua cac logic nghiep vu xu ly khach san
from models import PhongThuong, PhongVIP, KhachHang, PhieuThue
from file_handler import save_data, load_data

class QuanLyKhachSan:
    def __init__(self):
        # Khoi tao cac danh sach va doanh thu
        self.danh_sach_phong = []
        self.danh_sach_phieu = []
        self.tong_doanh_thu = 0

        # Tu dong doc du lieu khi bat dau chay
        self.nap_du_lieu()

    # Doc du lieu tu file json
    def nap_du_lieu(self):
        self.danh_sach_phong, self.danh_sach_phieu, self.tong_doanh_thu = load_data()

    # Luu du lieu ra file json
    def luu_du_lieu(self):
        save_data(self.danh_sach_phong, self.danh_sach_phieu, self.tong_doanh_thu)

    # 1. Hien thi danh sach phong
    def hien_thi_phong(self):
        if len(self.danh_sach_phong) == 0:
            print("Khach san hien chua co phong nao!")
            return

        print("\n" + "=" * 55)
        print(f"{'MA PHONG':<10} | {'TEN PHONG':<15} | {'LOAI':<8} | {'GIA':<10} | {'TRANG THAI'}")
        print("=" * 55)
        for p in self.danh_sach_phong:
            loai = "VIP" if isinstance(p, PhongVIP) else "Thuong"
            print(f"{p.ma_phong:<10} | {p.ten_phong:<15} | {loai:<8} | {p.gia_co_ban:<10} | {p.get_trang_thai()}")
        print("=" * 55)

    # 2. Them phong moi
    def them_phong(self, phong):
        # Kiem tra ma phong co bi trung khong
        for p in self.danh_sach_phong:
            if p.ma_phong == phong.ma_phong:
                print(f"Loi: Ma phong {phong.ma_phong} da ton tai roi!")
                return False

        self.danh_sach_phong.append(phong)
        print(f"Them phong '{phong.ten_phong}' thanh cong!")
        return True

    # 3. Dat phong
    def dat_phong(self, ma_phong, ma_khach, ten_khach, cccd, so_ngay_thue):
        # Tim phong theo ma nhap vao
        phong_can_thue = None
        for p in self.danh_sach_phong:
            if p.ma_phong == ma_phong:
                phong_can_thue = p
                break

        # Neu khong tim thay phong
        if phong_can_thue is None:
            print(f"Loi: Khong tim thay phong co ma '{ma_phong}'!")
            return False

        # Kiem tra xem phong co dang trong khong
        if phong_can_thue.get_trang_thai() != "Trống":
            print(f"Loi: Phong {ma_phong} hien tai da co nguoi thue roi!")
            return False

        # Neu phong trong, tien hanh dat phong
        # Doi trang thai phong sang Da thue qua phuong thuc setter (tinh dong goi)
        phong_can_thue.set_trang_thai("Đã thuê")

        # Tao khach hang va phieu thue
        kh = KhachHang(ma_khach, ten_khach, cccd)
        phieu = PhieuThue(kh, phong_can_thue, so_ngay_thue)
        self.danh_sach_phieu.append(phieu)

        print(f"-> Dat phong {ma_phong} thanh cong cho khach {ten_khach}!")
        return True

    # 4. Tra phong & Tinh tien (The hien tinh da hinh)
    def tra_phong(self, ma_phong):
        # Tim phieu thue cua phong nay
        phieu_can_tra = None
        for phieu in self.danh_sach_phieu:
            if phieu.phong.ma_phong == ma_phong:
                phieu_can_tra = phieu
                break

        if phieu_can_tra is None:
            print(f"Loi: Khong co phieu thue nao dang hoat dong cho phong '{ma_phong}'!")
            return False

        # Tinh da hinh o day:
        # Du phong la PhongThuong hay PhongVIP, ta deu goi .tinh_tien(so_ngay)
        # Python se tu dong biet chay ham tinh_tien cua PhongThuong hay PhongVIP
        so_ngay = phieu_can_tra.so_ngay_thue
        phong = phieu_can_tra.phong
        tong_tien = phong.tinh_tien(so_ngay)

        # In hoa don
        print("\n" + "-" * 35)
        print("          HOA DON THANH TOAN        ")
        print("-" * 35)
        print(f"Khach hang   : {phieu_can_tra.khach_hang.ten} (CCCD: {phieu_can_tra.khach_hang.cccd})")
        print(f"Phong        : {phong.ten_phong} ({phong.ma_phong})")
        loai = "VIP" if isinstance(phong, PhongVIP) else "Thuong"
        print(f"Loai phong   : {loai}")
        print(f"So ngay thue : {so_ngay} ngay")
        print(f"Gia co ban   : {phong.gia_co_ban} / ngay")
        if isinstance(phong, PhongVIP):
            print(f"Phi don dep  : {phong.phi_don_dep}")
            print(f"Phi minibar  : {phong.phi_minibar}")
        print("-" * 35)
        print(f"TONG TIEN PHAI TRA: {tong_tien} VND")
        print("-" * 35)

        # Chuyen trang thai phong ve lai "Trong"
        phong.set_trang_thai("Trống")

        # Cong vao tong doanh thu
        self.tong_doanh_thu += tong_tien

        # Xoa phieu thue khoi danh sach dang thue
        self.danh_sach_phieu.remove(phieu_can_tra)
        print("-> Tra phong va thanh toan thanh cong!")
        return True

    # 5. Bao cao doanh thu & so phong trong
    def bao_cao_doanh_thu(self):
        # Dem so luong phong dang trong
        dem_trong = 0
        ds_phong_trong = []
        for p in self.danh_sach_phong:
            if p.get_trang_thai() == "Trống":
                dem_trong += 1
                ds_phong_trong.append(p.ma_phong)

        print("\n" + "*" * 40)
        print("           BAO CAO DOANH THU           ")
        print("*" * 40)
        print(f"Tong doanh thu da thu duoc : {self.tong_doanh_thu} VND")
        print(f"Tong so phong hien co      : {len(self.danh_sach_phong)} phong")
        print(f"So luong phong dang trong  : {dem_trong} phong")
        if dem_trong > 0:
            print(f"Danh sach ma phong trong   : {', '.join(ds_phong_trong)}")
        print("*" * 40)
